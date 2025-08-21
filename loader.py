# loader.py
import pandas as pd

# Definimos los grupos de columnas y sus tipos
COLS_NOMBRES = ['indicativo', 'nombre', 'provincia']
COLS_INTS = ['altitud']
COLS_FLOATS = [
    'tmed','prec','tmin','tmax','velmedia','sol',
    'presMax','presMin','hrMedia','dir','racha',
    'hrMax','hrMin'
]
COLS_NUMS = COLS_INTS + COLS_FLOATS

COL_FECHA = 'fecha'

COLS_HORAS = ['horaPresMax','horaPresMin','horatmin',
              'horatmax','horaracha','horaHrMax','horaHrMin']

COLS_HORAS_LIMPIAS = [c + '_limpia' for c in COLS_HORAS]
COLS_HORAS_TIPOS = [c + '_tipo' for c in COLS_HORAS]
COLS_FECHAHORAS = ['fecha' + c + '_limpia' for c in COLS_HORAS]

COLS_CATEGORIAS = COLS_HORAS_TIPOS + ['dir_tipo']

PATH_VAL_CLIM_LIM = 'Valores_Climatologicos_1970_2024_Limpios.csv'

def cargar_dataset_limpio() -> pd.DataFrame:
    """Carga el dataset de valores climatológicos con los dtypes adecuados."""
    
    dtype_map = (
        {nombre: 'string' for nombre in COLS_NOMBRES} |
        {entero: 'Int64' for entero in COLS_INTS} |
        {decimal: 'Float64' for decimal in COLS_FLOATS} |
        {hora: 'string' for hora in COLS_HORAS} |
        {categoria: 'category' for categoria in COLS_CATEGORIAS} |
        {otro: 'string' for otro in COLS_HORAS_LIMPIAS + COLS_FECHAHORAS}
    )
    
    # Cargamos el CSV con los parámetros por defecto que nos permite
    df = pd.read_csv(
        PATH_VAL_CLIM_LIM,
        sep=';', decimal=',',
        dtype=dtype_map,
        parse_dates=[COL_FECHA],
        dayfirst=True
    )
    
    # Ajustes post-carga
    for col in COLS_HORAS_LIMPIAS:
        if col in df:
            df[col] = pd.to_datetime(df[col], format='%H:%M', errors='coerce').dt.time
    
    # for col in COLS_CATEGORIAS:
    #     if col in df:
    #         df[col] = df[col].astype('category')
    
    for col in COLS_FECHAHORAS:
        if col in df:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df
