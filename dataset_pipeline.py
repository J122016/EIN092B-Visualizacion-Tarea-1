import pandas as pd


def load_dataset(filename:str) -> pd.DataFrame:
    df = pd.read_csv(filename, encoding='latin1', delimiter=';', on_bad_lines='warn')

    # parseo de año
    df["AÑO"] = df["AÑO"].str[4:].astype(int)
    df["AÑO"] = pd.to_datetime(df["AÑO"], format='%Y')
    df = df.sort_values(by='AÑO', ascending=True)
    
    # TODO: ver que hacer con nulos
    # ...

    # ...

    return df