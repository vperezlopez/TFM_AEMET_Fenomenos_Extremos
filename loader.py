# loader.py
import pandas as pd

###############################################

COL_FECHA = 'fecha'

COLS_ESTACION = [
    'indicativo',
    'nombre',
    'provincia',
]

COL_ALTITUD = 'altitud'

COLS_COORDS = [
    'lat',
    'lon'
]

COLS_VARIABLES = [
    'tmed',
    'prec',
    'tmin',
    'tmax',
    'velmedia',
    'sol',
    'presMax',
    'presMin',
    'hrMedia',
    'dir',
    'racha',
    'hrMax',
    'hrMin'
]

# dtypes_map = {
#     'indicativo': 'string',
#     'nombre': 'string',
#     'provincia': 'string',
#     'altitud': 'Int64',
#     'tmed': 'Float64',
#     'prec': 'Float64',
#     'tmin': 'Float64',
#     'tmax': 'Float64',
#     'velmedia': 'Float64',
#     'sol': 'Float64',
#     'presMax': 'Float64',
#     'presMin': 'Float64',
#     'hrMedia': 'Float64',
#     'dir': 'Float64',
#     'racha': 'Float64',
#     'hrMax': 'Float64',
#     'hrMin': 'Float64',
#     'lat': 'Float64',
#     'lon': 'Float64'
# }

# COLS_HORAS = [
#     'horaPresMax',
#     'horaPresMin',
#     'horatmin',
#     'horatmax',
#     'horaracha',
#     'horaHrMax',
#     'horaHrMin'
# ]

###########################################################################################################

def cargar_dataset(url: str, variables_brutas: bool = False) -> pd.DataFrame:
    """Carga el dataset de valores climatológicos con los dtypes adecuados."""

    # El Dataset es tan grande que nos sale un warning si no se indican dtypes, ya que no puede inferirlos
    # Leemos cada grupo de columnas según su tipo (conocido de antemano)
    # Los valores decimales de las variables usaban originalmente la coma como separador decimal
    # Aunque se le indique con el argumento 'decimal', da error
    # Añadimos una opción para cargarlos como object y así procesarlos

    variable_dtype = 'Float64'
    if variables_brutas:
        variable_dtype = 'object'
    
    df = pd.read_csv(url,
                     sep = ';', decimal = ',',
                     usecols = [COL_FECHA] + COLS_ESTACION + [COL_ALTITUD] + COLS_COORDS + COLS_VARIABLES,
                     dtype = {nombre: 'string' for nombre in COLS_ESTACION} |
                             {COL_ALTITUD: 'Int64'} |
                             {coordenada: 'Float64' for coordenada in COLS_COORDS} |
                             {variable: variable_dtype for variable in COLS_VARIABLES},
                     parse_dates = [COL_FECHA])

    return df
