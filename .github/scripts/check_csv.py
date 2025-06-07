import sys
import pandas as pd
import os

COLUMNAS_REQUERIDAS = {
    'id_ano', 'fecha_de_notificacion_del', 'edad_de_la_victima',
    'unidad_de_medida_de_la_victima,sexo', 'area_de_residencia', 'barrio_de_residencia',
    'seguridad_social', 'estrato_socioeconomico', 'gestante', 'poblacion_a_cargo_icbf',
    'fecha_del_hecho', 'intentos_previos', 'numero_de_intentos', 'estado_civil',
    'escolaridad', 'conflicto_con_pareja_o_ex', 'enfermedad_cronica_dolorosa',
    'problemas_economicos', 'muerte_de_un_familiar', 'escolar_educativa',
    'problemas_juridicos', 'suicidio_de_un_familiar', 'maltrato_fisico_sicologico',
    'problemas_laborales', 'problemas_familiares', 'consumo_de_spa',
    'antecedentes_familiares_de', 'ideacion_suicida_persistente',
    'plan_organizado_de_suicidio', 'antecedente_trastorno', 'trastorno_depresivo',
    'trastorno_de_personalidad', 'trastorno_bipolar', 'esquizofrenia',
    'antecedente_violencia_o_abuso', 'abuso_de_alcohol', 'ahorcamiento',
    'arma_cortopunzante', 'arma_de_fuego', 'inmolacion', 'lanzamiento_al_vacio',
    'lanzamiento_a_vehiculo', 'lanzamiento_al_agua', 'intoxicaciones',
    'remitido_a_psiquiatria', 'remitido_a_psicologia', 'remitido_a_trabajo_social'}

CSV_PATH = 'data/prjt_data.csv'

if not os.path.exists(CSV_PATH):
    print(f"❌ El archivo {CSV_PATH} no existe.")
    sys.exit(1)

try:
    df = pd.read_csv(CSV_PATH, nrows=1)
    columnas = set(df.columns)
    if not COLUMNAS_REQUERIDAS.issubset(columnas):
        faltantes = COLUMNAS_REQUERIDAS - columnas
        print(
            f"❌ El archivo no contiene todas las columnas requeridas. Faltan: {', '.join(faltantes)}")
        sys.exit(1)
    else:
        print("✅ El archivo contiene todas las columnas requeridas.")
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")
    sys.exit(1)
