# constantes.py

PATH_DF_BRUTO = 'Valores_Climatologicos_1970_2024_con_Coordenadas.csv'
PATH_DF_PROCESADO = 'Valores_Climatologicos_1970_2024_Limpios.csv'
PATH_DF_TIDY = 'Valores_Climatologicos_1970_2024_Tidy_Lite.csv'

COL_FECHA = 'fecha'

COL_INDICATIVO = 'indicativo'
COL_PROVINCIA = 'provincia'

COLS_LOCALIZACION = [
    'nombre',
    'provincia',
]
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

COL_TMAX = 'tmax'
COL_TMIN = 'tmin'
COL_DIR = 'dir'
COL_PREC = 'prec'

COLS_VARIABLES = [
    'tmax',
    'tmed',
    'tmin',
    'sol',
    'velmedia',
    'racha',
    # 'dir',
    # 'presMax',
    # 'presMin',
    'hrMax',
    'hrMedia',
    'hrMin',
    'prec'
]

COL_VAR = 'variable'
COL_VAL = 'valor'
