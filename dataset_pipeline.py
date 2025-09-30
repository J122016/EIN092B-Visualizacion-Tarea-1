import pandas as pd
import os

def load_dataset(filename:str) -> pd.DataFrame:
    df = pd.read_csv(filename, encoding='latin1', delimiter=';', on_bad_lines='warn')

    # parseo de año
    df["AÑO_CATEGORIA"] = df["AÑO"].str[4:].astype(str)
    df["AÑO"] = df["AÑO"].str[4:].astype(int)
    df["AÑO"] = pd.to_datetime(df["AÑO"], format='%Y')
    df = df.sort_values(by='AÑO', ascending=True)

    # Transformación promedio de edad a número (vacios tranformados a 0) - TODO: verificar
    df["PROMEDIO EDAD PROGRAMA "] = pd.to_numeric(df["PROMEDIO EDAD PROGRAMA "], errors='coerce').fillna(0).astype(int)
    df["PROMEDIO EDAD MUJER "] = pd.to_numeric(df["PROMEDIO EDAD MUJER "], errors='coerce').fillna(0).astype(int)
    df["PROMEDIO EDAD HOMBRE "] = pd.to_numeric(df["PROMEDIO EDAD HOMBRE "], errors='coerce').fillna(0).astype(int)
    df["PROMEDIO EDAD NB "] = pd.to_numeric(df["PROMEDIO EDAD NB "], errors='coerce').fillna(0).astype(int)

    # Rellenando vacios con 0 en columnas de instancias de RANGO DE EDAD	
    df["RANGO DE EDAD 15 A 19 AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 15 A 19 AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD 20 A 24 AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 20 A 24 AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD 25 A 29 AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 25 A 29 AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD 30 A 34 AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 30 A 34 AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD 35 A 39 AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 35 A 39 AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD 40 Y MÁS AÑOS"] = pd.to_numeric(df["RANGO DE EDAD 40 Y MÁS AÑOS"], errors='coerce').fillna(0).astype(int)
    df["RANGO DE EDAD SIN INFORMACIÓN"] = pd.to_numeric(df["RANGO DE EDAD SIN INFORMACIÓN"], errors='coerce').fillna(0).astype(int)

    # Mapeando modalidad a Números - TODO:ver si existe mejor forma para visualización
    modalidad_map = { 'No Presencial': 1 , 'Semipresencial': 2, 'Presencial': 3} # orden de 'negativo a positivo'
    df["MODALIDAD_NUM"] = df["MODALIDAD"].map(modalidad_map)
    
    # TODO: ver que hacer con nulos
    # ...

    # ...

    return df


def get_unique_values_in_column(df: pd.DataFrame, column: str) -> list:
    return df[column].unique().tolist()

def get_numeric_columns(df: pd.DataFrame) -> list:
    return df.select_dtypes(include=['number']).columns.tolist()

def get_categorical_columns(df: pd.DataFrame) -> list:
    return df.select_dtypes(include=['object', 'category']).columns.tolist()

### Funciones de filtrado ###
def get_df_filtered_by_column_values(df: pd.DataFrame, column: str, values: list) -> pd.DataFrame:
    return df[df[column].isin(values)]

### Funciones externas adicionales para ambiente ###
def create_export_folders(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
    return