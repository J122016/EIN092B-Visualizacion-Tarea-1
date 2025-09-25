import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataset_pipeline import load_dataset
from dataset_analysis import *


def main():
    FILENAME = "TITULADO_2007-2024_web_19_05_2025_E.csv"
    EXPORT_PATH = "exports/"
    EXPORT_COUNTER = 0

    # Carga dataset, limpieza e inspeccion basica
    print("Cargando dataset...")
    df = load_dataset(FILENAME)
    df.info()
    with pd.option_context("display.max_columns", 42):
        print(df.describe(include="all"))
    print(df.head(5))
    print("Dataset cargado.")

    # Gráficos
    # 1. Grafico de prueba - entidad con titulados (filas) en cada año
    graph_entidades_titulados_anno(
        df, export=f"{EXPORT_PATH}_{EXPORT_COUNTER}_test_analysis.svg", display=True
    )
    EXPORT_COUNTER += 1

    # 1. Grafico de prueba - titulados por año
    graph_total_titulados_anno(
        df, export=f"{EXPORT_PATH}_{EXPORT_COUNTER}_test_analysis.svg", display=True
    )
    EXPORT_COUNTER += 1

    return


if __name__ == "__main__":
    main()
