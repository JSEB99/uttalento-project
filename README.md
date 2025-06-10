# PERFIL  DEMOGRAFICO Y CONTEXTO SOCIAL SOBRE  LOS INTENTOS DE SUICIDIO EN LA CIUDAD DE TUNJA BOYACA

**Proyecto [UTTALENTO](https://uttalento.co/)**

---

## 👥 Integrantes

- Juan Sebastian Mora Tibamoso
- Ana Dorcinda Cuervo
- Sonia Patricia Galvis

## Objetivo

Recopilar, analizar, y difundir informaion confiable  sensible,  características demográficaS, sociales y psicológicas  comunes de la gente con intentos de suicidio en el municipio de Tunja Boyaca a diciembre 31 de 2024 co el fin de promover la prevencion y disminuir los mismos.

---

## Fuentes

- [Datos Abiertos](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Informaci-n-Intentos-de-Suicidio-Municipio-de-Tunj/nk8x-s9hw/about_data)

## Tecnologías usadas

- Python
- Power BI

---

## Diccionario de Datos

| Campo                         | Descripción                                                     | Tipo de dato       | Valores posibles / Comentarios                    |
| ----------------------------- | --------------------------------------------------------------- | ------------------ | ------------------------------------------------- |
| fecha_de_notificacion         | Fecha en que se notificó el evento o caso                       | Fecha (YYYY-MM-DD) |                                                   |
| edad_de_la_victima            | Edad de la persona afectada                                     | Entero             |                                                   |
| sexo                          | Género de la víctima                                            | Categórico         | "Femenino", "Masculino"                           |
| area_de_residencia            | Área geográfica donde reside la víctima                         | Texto              | Ejemplo: "Cabecera municipal"                     |
| barrio_de_residencia          | Barrio específico de residencia                                 | Texto              |                                                   |
| seguridad_social              | Régimen de seguridad social o sistema de salud al que pertenece | Texto              | Ejemplo: "Contributivo", "No asegurado"           |
| estrato_socioeconomico        | Nivel socioeconómico asignado                                   | Entero             | Generalmente valores de 1 a 6                     |
| gestante                      | Indica si la víctima está embarazada                            | Booleano           | True / False                                      |
| poblacion_a_cargo_icbf        | Indica si tiene población a cargo registrada en el ICBF         | Booleano           | True / False                                      |
| fecha_del_hecho               | Fecha en que ocurrió el evento                                  | Fecha (YYYY-MM-DD) |                                                   |
| numero_de_intentos            | Número de intentos (ej. de suicidio) relacionados con el caso   | Entero             |                                                   |
| estado_civil                  | Estado civil de la víctima                                      | Texto              | Ejemplo: "Soltero(a)", "Casado(a)", "Union libre" |
| escolaridad                   | Nivel educativo alcanzado                                       | Texto              | Ejemplo: "Básica secundaria", "Profesional"       |
| conflictos_pareja             | Indica si existen conflictos en la pareja                       | Booleano           | True / False                                      |
| enfermedad_cronica_dolorosa   | Indica si padece alguna enfermedad crónica con dolor            | Booleano           | True / False                                      |
| problemas_economicos          | Indica si presenta problemas económicos                         | Booleano           | True / False                                      |
| muerte_de_un_familiar         | Indica si ha ocurrido la muerte de un familiar                  | Booleano           | True / False                                      |
| problemas_juridicos           | Indica si tiene problemas legales o jurídicos                   | Booleano           | True / False                                      |
| suicidio_de_un_familiar       | Indica si algún familiar ha cometido suicidio                   | Booleano           | True / False                                      |
| maltrato_fisico_sicologico    | Indica si ha sufrido maltrato físico o psicológico              | Booleano           | True / False                                      |
| problemas_laborales           | Indica si presenta problemas en el ámbito laboral               | Booleano           | True / False                                      |
| problemas_familiares          | Indica si tiene problemas familiares                            | Booleano           | True / False                                      |
| consumo_de_spa                | Indica consumo de sustancias psicoactivas                       | Booleano           | True / False                                      |
| familiares_cond_suicida       | Indica si hay familiares con conducta suicida                   | Booleano           | True / False                                      |
| ideacion_suicida_persistente  | Indica presencia de ideación suicida persistente                | Booleano           | True / False                                      |
| plan_organizado_de_suicidio   | Indica si existe un plan organizado para suicidio               | Booleano           | True / False                                      |
| antecedente_trastorno         | Indica antecedentes de trastornos mentales                      | Booleano           | True / False                                      |
| trastorno_depresivo           | Indica presencia de trastorno depresivo                         | Booleano           | True / False                                      |
| trastorno_de_personalidad     | Indica presencia de trastorno de personalidad                   | Booleano           | True / False                                      |
| trastorno_bipolar             | Indica presencia de trastorno bipolar                           | Booleano           | True / False                                      |
| esquizofrenia                 | Indica diagnóstico de esquizofrenia                             | Booleano           | True / False                                      |
| antecedente_violencia_o_abuso | Indica antecedentes de violencia o abuso                        | Booleano           | True / False                                      |
| abuso_de_alcohol              | Indica consumo abusivo de alcohol                               | Booleano           | True / False                                      |
| ahorcamiento                  | Indica si se ha intentado ahorcamiento                          | Booleano           | True / False                                      |
| arma_cortopunzante            | Indica si se ha intentado usar arma cortopunzante               | Booleano           | True / False                                      |
| arma_de_fuego                 | Indica si se ha intentado usar arma de fuego                    | Booleano           | True / False                                      |
| inmolacion                    | Indica si se ha intentado inmolación                            | Booleano           | True / False                                      |
| lanzamiento_al_vacio          | Indica si se ha intentado lanzamiento al vacío                  | Booleano           | True / False                                      |
| lanzamiento_a_vehiculo        | Indica si se ha intentado lanzamiento a vehículo                | Booleano           | True / False                                      |
| lanzamiento_al_agua           | Indica si se ha intentado lanzamiento al agua                   | Booleano           | True / False                                      |
| intoxicaciones                | Indica si ha habido intoxicaciones                              | Booleano           | True / False                                      |
| remitido_a_psiquiatria        | Indica si fue remitido a psiquiatría                            | Booleano           | True / False                                      |
| remitido_a_psicologia         | Indica si fue remitido a psicología                             | Booleano           | True / False                                      |
| remitido_a_trabajo_social     | Indica si fue remitido a trabajo social                         | Booleano           | True / False                                      |

---

## Instrucciones

### Python

1. Clonar el repositorio
2. Generar un archivo `.env`, donde pondras la ruta que quieres para la salida de los datos, *por defecto (data/prjt_data.csv)* y la *URL* de la API de los datos

> [!TIP]
> El archivo de lectura csv debe llamarse **prjt_data.csv** para que funcione, en caso contrario, deberá modificarse la variable de entorno a su acomodo.

3. Crear un ambiente virtual, en este caso se uso [uv](https://docs.astral.sh/uv/), sin embargo, no es necesario, lo importante es **instalar las dependencias que se especifican en el archivo `pyproject.toml`**
4. Ejecutar `python etl.py`, *Esto descarga los datos con un nombre en especifico en data, luego los limpia y guarda los datos limpios en esa misma ubicación*

> [!NOTE]
> **uv** tiene la particularidad que es mas rapido instalando dependencias

### Power BI

Normalmente funciona sin tener que modificar nada, en caso de que no funcione hacer lo siguiente:

- Verificar el origen de los datos y ajustarlo al **origen respectivo**, es decir, donde quedaron los datos limpios en tu sistema.

## Análisis

Se utilizaron **análisis descriptivos** en las siguientes categorías:

- Resumen General: Una mirada sobre algunos puntos importantes de los datos
- Perfil Demográfico: Entender el contexto de las personas que realizaron los intentos de suicidio
- Factores de Riesgo Psicosocial: Comprender que tipos de causas y consecuencias sufrían estas personas
- Métodos: Revisar los métodos más comunes
- Geografía: Visualizar los sectores mas afectados
- Atención y Seguimiento: Revisar si las personas fueron remitidas a centros de atención, si tienen pensamientos recurrentes o si ya venian planeandolo con tiempo

### Conclusiones

**Evolución de los intentos**

- En los 4 años evaluados se ve un pequeño incremento en los datos, la media general es de **17 casos por mes** y desde **febrero 2023** los casos ya estan sobre la media, ademas de que **marzo 2023** cuenta con el **pico mas alto**, con un total de **40 casos** presentados en ese mes.
- La edad según la mediana donde se ve mas propenso este tema es **21 años**
- Los eventos se notifican alrededor de **2.85 días** despues, es decir, **3 días** aproximando. *Lo cual no se tiene una atención inmediata frente a estos casos*.

**¿Qué perfil es más común entre los intentos?**

- Las mujeres fueron las mas afectadas, con un total de **529 intentos**, es decir, un **64%** del total
- Las edades más afectadas van de **15-20 años**, sin embargo el espectro se concentra en un rango de **10 a 30 años**, donde en el rango de tiempo evaluado y con rangos de edades cada 5 años se vieron todos ellos con mas de **90 intentos**.
- El estrato más afectado fue el **estrato 3**, con un **42.2%** de los datos, seguido por el **estrato 2** con un **29%**, luego el estrato 1, estrato 4 y estrato 5.
- Las enfermedades crónicas dolorosas **no fueron** un indicativo relevante, ya que de 818 casos, **solo 30** sufrieron de estos males
- Claramente las personas afectadas por estos sucesos **son solteras**, con **648 personas** de 818. Seguido lejanamente por **union libre** con apenas 101.
- La escolaridad fue definida por personas que completaron el colegio, donde el top 3 fue:
  - Básica secundaria: 392
  - Técnica: 133
  - Básica primaria: 132

**¿Ideación suicida persistente o plan organizado?**

- **120 personas** lo planearon, un **14.6%** por lo que no fue algo tan determinante
- Entre los distintos puntos evaluados podemos encontrar como principales determinantes los siguientes:
  - **Antecedente Psiquiatrico**: con 439 personas
  - **Trastorno Depresivo**: con 391 personas
  - **Conflictos de Pareja**: con 285 personas

**¿Métodos más comunes?**

A nivel general los 3 métodos más comunes son:
- Intoxicaciones: 506 personas
- Armas cortopunzantes: 145 personas
- Ahorcamientos: 91 personas

Añadiendo que *Lanzamiento a Vehículos y Lanzamientos al Vacío* estan sobre 70 personas. Las demas si apenas se llegan a ver casos.

Si lo clasificamos por género, ambos mantienen el top y las proporciones, a excepción de **Ahorcamientos**, donde *las mujeres tienen 49 casos y los hombres 42 casos*.

**¿Se relaciona con ideación suicida o diagnóstico previo?**

- En general no, ya que la muestra de personas que lo planificaron es del **14%**, sin embargo, mencionar que las personas afectadas que fueron remitidas a psicología, psiquiatría y/o trabajo social superan el **74%** de los casos.
- El número de reintentos no es muy grande, sin embargo, las proporciones de **2,3 o 4 intentos** se mantienen en un **20%** del total.
- Los pensamientos recurrentes sobre los intentos estan en un **39.6%**, lo cual puede llegar a ser un factor a considerar, teniendo en cuenta la alza en los casos en los recientes años.