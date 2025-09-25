import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def graph_entidades_titulados_anno(
    df: pd.DataFrame, export: str, display: bool = True
) -> None:
    plt.figure(figsize=(10, 6))
    plot = sns.countplot(data=df, x="AÑO", palette="viridis")
    plt.title("Número de entidades (filas) con titulados por año")
    plt.xlabel("Año")
    plot.set_xticklabels(df["AÑO"].dt.year.unique())
    plt.ylabel("Número de entidades (filas) con titulados")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if display:
        plt.figure()
    plot.figure.savefig(export, dpi=300)
    plt.close()
    return


def graph_total_titulados_anno(
    df: pd.DataFrame, export: str, display: bool = True
) -> pd.DataFrame:
    plt.figure(figsize=(10, 6))
    df["TOTAL TITULACIONES ACUM"] = df.groupby("AÑO")["TOTAL TITULACIONES"].cumsum()
    plot = sns.lineplot(
        data=df, x="AÑO", y="TOTAL TITULACIONES ACUM", marker="o", color="b"
    )
    plt.title("Total de titulados por año")
    plt.xlabel("Año")
    plt.ylabel("Total de titulados")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if display:
        plt.figure()
    plot.figure.savefig(export, dpi=300)
    plt.close()
    return df
