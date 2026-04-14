import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:

    def __init__(self, df):
        self.df = df  # Guardamos el DataFrame
        self.output_dir = "output/charts"
        os.makedirs(self.output_dir, exist_ok=True)  # Crea carpeta si no existe

    def sales_by_store(self):
        sales = (
            self.df.groupby("store_name")["total_sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        sales.plot(kind="bar", figsize=(12, 6))
        plt.title("Top 10 Stores by Total Sales")
        plt.xlabel("Store")
        plt.ylabel("Total Sales ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Guardar gráfico
        plt.savefig(f"{self.output_dir}/sales_by_store.png")
        plt.close()

    def quantity_by_category(self):
        plt.figure(figsize=(12, 10))

        quantity = (
            self.df.groupby("category")["qty_sold"]
            .sum()
            .sort_values(ascending=True)
        )

        quantity.plot(kind="barh")

        plt.title("Quantity Sold by Category (All Categories)")
        plt.xlabel("Quantity Sold")
        plt.ylabel("Category")
        plt.tight_layout()

        # Guardar gráfico
        plt.savefig(f"{self.output_dir}/quantity_by_category.png")
        plt.close()

    def sales_distribution(self):
        df_filtered = self.df[self.df["total_sales"] <= 700]
        bins = range(0, 701, 25)

        plt.figure(figsize=(8, 5))
        df_filtered["total_sales"].hist(bins=bins)

        plt.title("Sales Distribution (0–700)")
        plt.xlabel("Total Sales ($)")
        plt.ylabel("Frequency")
        plt.xlim(0, 700)
        plt.tight_layout()

        # Guardar gráfico
        plt.savefig(f"{self.output_dir}/sales_distribution.png")
        plt.close()

    def correlation_heatmap(self):
        correlation = self.df[["qty_sold", "sold_price", "total_sales"]].corr()

        plt.figure(figsize=(6, 5))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

        plt.title("Correlation Between Variables")
        plt.tight_layout()

        # Guardar gráfico
        plt.savefig(f"{self.output_dir}/correlation_heatmap.png")
        plt.close()


if __name__ == "__main__":
    # Cargar datos
    df = pd.read_csv("data/cleaned/data2016_clean.csv")

    # Limpieza básica
    df["store_name"] = df["store_name"].str.strip()
    df = df[df["store_name"] != "Overall"]
    df = df[df["department"] != "No data"]
    df = df.dropna()

    print("Datos cargados correctamente")
    print(df.head())

    # Crear objeto visualizador
    viz = Visualizer(df)

    # Ejecutar gráficos
    viz.sales_by_store()
    viz.quantity_by_category()
    viz.sales_distribution()
    viz.correlation_heatmap()