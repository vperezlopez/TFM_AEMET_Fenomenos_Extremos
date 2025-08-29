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

# Diccionarios con tipos de variables:

COLS_NOMBRES = {
    'indicativo': 'string',
    'nombre': 'string',
    'provincia': 'string'
}

COLS_INTS = {
    'altitud': 'Int64'
}

COLS_FLOATS = {
    'tmed': 'Float64',
    'prec': 'Float64',
    'tmin': 'Float64',
    'tmax': 'Float64',
    'velmedia': 'Float64',
    'sol': 'Float64',
    'presMax': 'Float64',
    'presMin': 'Float64',
    'hrMedia': 'Float64',
    'dir': 'Float64',
    'racha': 'Float64',
    'hrMax': 'Float64',
    'hrMin': 'Float64'
}

# COLS_NUMS = COLS_INTS + COLS_FLOATS

COL_FECHA = 'fecha'
COLS_HORAS = [
    'horaPresMax',
    'horaPresMin',
    'horatmin',
    'horatmax',
    'horaracha',
    'horaHrMax',
    'horaHrMin'
]

COLS_COORDS = {
    'lat': 'Float64',
    'lon': 'Float64'
}


###############################################

dtypes_map = {
    'indicativo': 'string',
    'nombre': 'string',
    'provincia': 'string',
    'altitud': 'Int64',
    'tmed': 'Float64',
    'prec': 'Float64',
    'tmin': 'Float64',
    'tmax': 'Float64',
    'velmedia': 'Float64',
    'sol': 'Float64',
    'presMax': 'Float64',
    'presMin': 'Float64',
    'hrMedia': 'Float64',
    'dir': 'Float64',
    'racha': 'Float64',
    'hrMax': 'Float64',
    'hrMin': 'Float64',
    'lat': 'Float64',
    'lon': 'Float64'

}
COL_FECHA = 'fecha'
COLS_HORAS = [
    'horaPresMax',
    'horaPresMin',
    'horatmin',
    'horatmax',
    'horaracha',
    'horaHrMax',
    'horaHrMin'
]

COLS_COORDS = {
    
}






PATH_VAL_CLIM_LIM = 'Valores_Climatologicos_1970_2024_Limpios.csv'

def cargar_dataset_limpio(url: str = PATH_VAL_CLIM_LIM) -> pd.DataFrame:
    """Carga el dataset de valores climatológicos con los dtypes adecuados."""

    cols_df = pd.read_csv(url, sep = ';', nrows = 0).columns

    cols_faltantes = list(set(cols_df) - set(dtypes_map.keys()))

    # print(dtypes_map | {col: 'string' for col in cols_faltantes})
    
    # dtype_map = (
    #     {nombre: 'string' for nombre in COLS_NOMBRES} |
    #     {entero: 'Int64' for entero in COLS_INTS} |
    #     {decimal: 'Float64' for decimal in COLS_FLOATS} |
    #     {hora: 'string' for hora in COLS_HORAS} |
    #     {categoria: 'category' for categoria in COLS_CATEGORIAS} |
    #     {otro: 'string' for otro in COLS_HORAS_LIMPIAS + COLS_FECHAHORAS}
    # )
    
    # Cargamos el CSV con los parámetros por defecto que nos permite
    df = pd.read_csv(
        PATH_VAL_CLIM_LIM,
        sep = ';', #decimal = ',',
        dtype = dtypes_map | {col: 'string' for col in cols_faltantes},
        parse_dates = [COL_FECHA],
        dayfirst=True
    )
    
    # Ajustes post-carga
    # for col in COLS_HORAS_LIMPIAS:
    #     if col in df:
    #         df[col] = pd.to_datetime(df[col], format='%H:%M', errors='coerce').dt.time
    
    # for col in COLS_CATEGORIAS:
    #     if col in df:
    #         df[col] = df[col].astype('category')
    
    # for col in COLS_FECHAHORAS:
    #     if col in df:
    #         df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df
