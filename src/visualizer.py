import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:
    
    
    def __init__(self, df):
        self.df = df  # Guardamos el DataFrame en la clase

    def sales_by_store(self):
        # Agrupa por tienda y suma las ventas totales
        sales = (
            self.df.groupby("store_name")["total_sales"]
            .sum()
            .sort_values(ascending=False)  # Ordena de mayor a menor
            .head(10)  # Solo top 10 tiendas
        )

        # Gráfico de barras vertical
        sales.plot(kind="bar", figsize=(12, 6))
        plt.title("Top 10 Stores by Total Sales")
        plt.xlabel("Store")
        plt.ylabel("Total Sales ($)")
        plt.xticks(rotation=45)  # Rota nombres para mejor lectura
        plt.tight_layout()
        plt.show()

    def quantity_by_category(self):
        plt.figure(figsize=(12, 10))

        
        quantity = (
            self.df.groupby("category")["qty_sold"]
            .sum()
            .sort_values(ascending=True)  # Ver los menos vendidos primero
        )

        # Gráfico horizontal
        quantity.plot(kind="barh")

        plt.title("Quantity Sold by Category (All Categories)")
        plt.xlabel("Quantity Sold")
        plt.ylabel("Category")

        plt.tight_layout()
        plt.show()

    def sales_distribution(self):
        # Filtra valores extremos (outliers)
        df_filtered = self.df[self.df["total_sales"] <= 700]

        # Define intervalos del histograma
        bins = range(0, 701, 25)

        plt.figure(figsize=(8, 5))
        df_filtered["total_sales"].hist(bins=bins)

        plt.title("Sales Distribution (0–700)")
        plt.xlabel("Total Sales ($)")
        plt.ylabel("Frequency")
        plt.xlim(0, 700)

        plt.tight_layout()
        plt.show()

    def correlation_heatmap(self):
        # Calcula correlación entre variables numéricas
        correlation = self.df[["qty_sold", "sold_price", "total_sales"]].corr()

        plt.figure(figsize=(6, 5))

        # Heatmap con valores visibles
        sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

        plt.title("Correlation Between Variables")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Cargar datos
    df = pd.read_csv("data/cleaned/data2016_clean.csv")

    # Limpieza básica
    df["store_name"] = df["store_name"].str.strip()  # Quita espacios
    df = df[df["store_name"] != "Overall"]  # Elimina fila resumen
    df = df[df["department"] != "No data"]  # Elimina datos inválidos

    # Elimina filas con valores nulos (puede reducir dataset)
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