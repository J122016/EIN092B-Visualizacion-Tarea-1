import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import itertools
from dataset_pipeline import load_dataset, create_export_folders

def correlation_heatmap_base(df: pd.DataFrame, export: str, display: bool = True) -> None:
    plt.figure(figsize=(12, 10))
    numeric_df = df.select_dtypes(include=['number'])  # Selecciona solo columnas numéricas
    corr = numeric_df.corr()  # Calcula la matriz de correlación
    plot = sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    title = export.split("-")[-1].replace("_", " ").replace(".svg", "") if "-" in export else export
    plt.title(f"Matriz de Correlación: {title}")
    plt.tight_layout()
    if display:
        plt.figure()
    plot.figure.savefig(export, dpi=300)
    plt.close()
    return

def graph_correlation_filter(df: pd.DataFrame, filter_columns: list, year_col: str, drop_columns: list, export: str, display: bool = True) -> None:
    """
    Genera matrices de correlación filtradas por cada valor único en las columnas de filter_columns.
    Ejemplo: filter_columns = ["NIVEL GLOBAL", "ÁREA DEL CONOCIMIENTO"]
    Genera una matriz de correlación para cada combinación única de estos valores por año.
    """
    dict_values = {}
    if year_col:
        # NOTE: WARNING!!! - si se filtra por año puede incrementar mucho las combinaciones
        dict_values[year_col] = df[year_col].dropna().unique()
    dict_values.update({col: df[col].dropna().unique() for col in filter_columns})
    filter_columns = list(dict_values.keys())

    all_combinations = list(itertools.product(*dict_values.values()))
    print(f"Generando {len(all_combinations)} matrices de correlaciónes")
    display = display and len(all_combinations) <= 10 # Para no saturar pantalla

    export_subindex = 0

    for combination in all_combinations:
        print(f"{export_subindex+1}/{len(all_combinations)}: {combination}")
        temp_df = df.copy()
        tmp_dict = dict(zip(filter_columns, combination))
        for col in filter_columns:
            temp_df = temp_df[temp_df[col] == tmp_dict[col]]

        temp_df = temp_df.drop(columns=drop_columns) if drop_columns else temp_df

        filename_context = "+".join([f"{value}" for value in combination])
        correlation_heatmap_base(temp_df, export=f"{export}-{export_subindex}_{filename_context}.svg", display=display)
        export_subindex += 1

    return


def main(df: pd.DataFrame, DISPLAY_GRAPHS: bool = False, export_counter:int = 0) -> None:
    EXPORT_PATH_CORRELATION = "exports/correlation/"
    create_export_folders(EXPORT_PATH_CORRELATION)
    
    ## 1. Matriz de correlación general
    correlation_heatmap_base(
        df, export=f"{EXPORT_PATH_CORRELATION}_{export_counter}_correlation_heatmap_general.svg", display=(False or DISPLAY_GRAPHS)
    )

    ## 2. Matriz de correlación por filtrada por NIVEL GLOBAL, MODALIDAD y ÁREA DEL CONOCIMIENTO
    graph_correlation_filter(
        df, filter_columns=["NIVEL GLOBAL", "ÁREA DEL CONOCIMIENTO"],
        year_col=None, drop_columns=["CÓDIGO INSTITUCIÓN", "TOTAL TITULACIONES ACUM"],
        export=f"{EXPORT_PATH_CORRELATION}_{export_counter}_correlation_heatmap_filtered",
        display=(False or DISPLAY_GRAPHS)
    )
    export_counter += 1

    ## 3. Matriz de correlación filtrada por AÑO y AREA DEL CONOCIMIENTO
    graph_correlation_filter(
        df, filter_columns=["AÑO_CATEGORIA","ÁREA DEL CONOCIMIENTO"],
        year_col=None, drop_columns=["CÓDIGO INSTITUCIÓN", "TOTAL TITULACIONES ACUM"],
        export=f"{EXPORT_PATH_CORRELATION}_{export_counter}_correlation_heatmap_filtered",
        display=(False or DISPLAY_GRAPHS)
    )

    ## otras matrices de correlación
    # ...

    return


if __name__ == "__main__":
    FILENAME = "TITULADO_2007-2024_web_19_05_2025_E.csv"
    DISPLAY_GRAPHS = False
    df = load_dataset(FILENAME)
    main(df, DISPLAY_GRAPHS)