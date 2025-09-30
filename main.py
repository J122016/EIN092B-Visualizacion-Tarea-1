import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataset_pipeline import *
from dataset_analysis import *
import correlation_heatmap as correlation_heatmap


def main():
    FILENAME = "TITULADO_2007-2024_web_19_05_2025_E.csv"
    EXPORT_PATH = "exports/"
    export_counter = 0
    DISPLAY_GRAPHS = False

    # Carga dataset, limpieza e inspeccion basica
    print("Cargando dataset...")
    df = load_dataset(FILENAME)
    df.info()
    numeric_columns = get_numeric_columns(df)
    categorical_columns = get_categorical_columns(df)
    categorical_columns_dict = {}
    for col in categorical_columns:
        categorical_columns_dict[col] = get_unique_values_in_column(df, col)
        print(f"Columna: '{col}' - Valores únicos: ")
        tmp_unicos = categorical_columns_dict[col]
        print(tmp_unicos) if len(tmp_unicos) <= 100 else print(tmp_unicos[:50], "...", tmp_unicos[-50:])

    with pd.option_context("display.max_columns", 42):
        print(df.describe(include="all"))
    print(df.head(5))
    print("Dataset cargado.")

    # Creando carpetas de exportación si no existen
    create_export_folders(EXPORT_PATH)

    # Gráficos
    # 1. Grafico de prueba - entidad con titulados (filas) en cada año
    graph_entidades_titulados_anno(
        df, export=f"{EXPORT_PATH}_{export_counter}_test_analysis.svg", display=(False or DISPLAY_GRAPHS)
    )
    export_counter += 1

    # 1. Grafico de prueba - titulados por año
    graph_total_titulados_anno(
        df, export=f"{EXPORT_PATH}_{export_counter}_test_analysis.svg", display=(False or DISPLAY_GRAPHS)
    )
    export_counter += 1

    # Matrices de correlacion + heatmaps
    correlation_heatmap.main(df=df, DISPLAY_GRAPHS=DISPLAY_GRAPHS, export_counter=export_counter)
    export_counter += 1
    # --- --- ---

    # Boxplot
    # ...


    # Lineplots
    # ...

    
    # Histogramas
    # ---


    # Scatterplots
    # ...

    plt.show()

    return


if __name__ == "__main__":
    main()
