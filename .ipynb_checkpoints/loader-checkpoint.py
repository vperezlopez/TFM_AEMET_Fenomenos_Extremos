# loader.py
import pandas as pd
import constantes as const

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
                     usecols =  [const.COL_FECHA] +
                                 const.COLS_ESTACION +
                                [const.COL_ALTITUD] +
                                 const.COLS_COORDS +
                                 const.COLS_VARIABLES,
                     dtype = {nombre: 'string' for nombre in const.COLS_ESTACION} |
                             {const.COL_ALTITUD: 'Int64'} |
                             {coordenada: 'Float64' for coordenada in const.COLS_COORDS} |
                             {variable: variable_dtype for variable in const.COLS_VARIABLES},
                     parse_dates = [const.COL_FECHA])

    return df
