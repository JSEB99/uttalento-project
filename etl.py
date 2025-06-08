import requests
import pandas as pd
import os
import utils.correcciones as cs
from dotenv import load_dotenv

load_dotenv()

DATA_API = os.getenv('URL')
RUTA_RELATIVA = os.getenv('RUTA_RELATIVA')


def obtener_datos(url: str, output_file: str) -> pd.DataFrame:
    print("leyendo datos...")
    response = requests.get(DATA_API)

    if response.status_code == 200:
        print("datos leidos...")
        data = response.json()
        df = pd.DataFrame(data)
        print("datos convertidos en dataframe...")
        df.to_csv(output_file, index=False)
        return df
    else:
        print(f"Error {response.status_code}: No se pudo obtener los datos")


def corregir_valores(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df["area_de_residencia"] = df["area_de_residencia"].replace(
            cs.correciones_area)
        df["seguridad_social"] = df["seguridad_social"].replace(
            cs.correciones_seguridad)
        df["intentos_previos"] = df["intentos_previos"].replace(
            cs.correciones_intentos).astype(bool)
        df["numero_de_intentos"] = df["numero_de_intentos"].replace(
            cs.correciones_num_int).astype(int)
        df["estado_civil"] = df["estado_civil"].replace(cs.correciones_estado)
        df["escolaridad"] = df["escolaridad"].replace(
            cs.correciones_escolaridad)
    except KeyError as e:
        raise KeyError(f"[corregir_valores] Columna faltante: {e}")
    except Exception as e:
        raise Exception(f"[corregir_valores] Error inesperado: {e}")
    return df


def capitalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    try:
        columnas = ["area_de_residencia", "seguridad_social",
                    "barrio_de_residencia", "sexo", "estado_civil", "escolaridad"]
        for col in columnas:
            if col in df.columns:
                df[col] = df[col].str.capitalize()
    except Exception as e:
        raise Exception(f"[capitalizar_columnas] Error al capitalizar: {e}")
    return df


def rellenar_booleanos(df: pd.DataFrame) -> pd.DataFrame:
    try:
        columnas = ["trastorno_depresivo", "trastorno_bipolar",
                    "esquizofrenia", "trastorno_de_personalidad"]
        for col in columnas:
            if col in df.columns:
                df[col] = df[col].fillna(False)
    except Exception as e:
        raise Exception(f"[rellenar_booleanos] Error al rellenar: {e}")
    return df


def corregir_si_no(df: pd.DataFrame) -> pd.DataFrame:
    try:
        for col in cs.columnas_si_no:
            if col in df.columns:
                df[col] = df[col].replace(
                    cs.correciones_booleanas).astype(bool)
    except Exception as e:
        raise Exception(f"[corregir_si_no] Error en columnas 'sí/no': {e}")
    return df


def convertir_fechas(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df["fecha_de_notificacion_del"] = pd.to_datetime(
            df["fecha_de_notificacion_del"], errors='coerce')
        df["fecha_del_hecho"] = pd.to_datetime(
            df["fecha_del_hecho"], errors='coerce')
    except Exception as e:
        raise Exception(f"[convertir_fechas] Error al convertir fechas: {e}")
    return df


def renombrar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.rename(columns={
            "fecha_de_notificacion_del": "fecha_de_notificacion",
            "conflicto_con_pareja_o_ex": "conflictos_pareja",
            "antecedentes_familiares_de": "familiares_cond_suicida"
        }, inplace=True)
    except Exception as e:
        raise Exception(
            f"[renombrar_columnas] Error al renombrar columnas: {e}")
    return df


def eliminar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    try:
        columnas_a_eliminar = ["intentos_previos",
                               "id_ano", "unidad_de_medida_de_la_victima", "escolar_educativa"]
        df.drop(columns=columnas_a_eliminar, inplace=True)
    except Exception as e:
        raise Exception(f"[eliminar_columnas] Error al eliminar columnas: {e}")
    return df


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    print("🔧 Iniciando limpieza de datos...")
    pd.set_option('future.no_silent_downcasting', True)

    try:
        df = corregir_valores(df)
        df = capitalizar_columnas(df)
        df = rellenar_booleanos(df)
        df = corregir_si_no(df)
        df = convertir_fechas(df)
        df = renombrar_columnas(df)
        df = eliminar_columnas(df)
    except Exception as e:
        print(f"❌ Error durante la limpieza de datos: {e}")
        raise  # Puedes comentar esta línea si prefieres que no se interrumpa el flujo

    print("✅ Limpieza de datos completada.")
    return df


if __name__ == "__main__":
    if os.path.exists(RUTA_RELATIVA):
        df = pd.read_csv(RUTA_RELATIVA)
        df = limpiar_datos(df.copy())
        df.to_csv("./data/data_clean.csv", index=False)
        print(f"""datos limpios guardados en: ---> './data/data_clean.csv' <---
            - cantidad de registros: {df.shape}
            - columnas de texto: {df.select_dtypes(include='object').shape[1]}
            - columnas booleanas: {df.select_dtypes(include="bool").shape[1]}
            - columnas númericas: {df.select_dtypes(include='int').shape[1]}
            - columnas de fecha: {df.select_dtypes(include='datetime').shape[1]}""")

    else:
        df = obtener_datos(DATA_API, RUTA_RELATIVA)
        df = limpiar_datos(df.copy())
        df.to_csv("./data/data_clean.csv", index=False)
        print("datos limpios guardados en './data/data_clean.csv'")
