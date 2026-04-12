import pandas as pd

class DataLoader:
    def __init__(self, file, sheet):
        # aquí guarda el nombre del archivo y la hoja que vamos a usar
        self.file = file
        self.sheet = sheet
        self.df = None  # aquí luego se va a guardar el dataset

    def load_data(self):
        try:
            # carga el archivo de excel usando pandas
            self.df = pd.read_excel(self.file, sheet_name=self.sheet)
            print("Datos cargados correctamente.\n")

            # esto es para que pandas no corte columnas en la terminal
            pd.set_option("display.max_columns", None)
            pd.set_option("display.width", 1000)

            # muestra las primeras filas para ver si todo cargó bien
            print("Primeras filas del dataset:")
            print(self.df.head(20).to_string())

        except Exception as e:
            print("Error al cargar los datos:", e)

    def detect_nulls(self):
        if self.df is not None:
            # aquí revisa cuántos valores vacíos hay por columna
            print("\nValores nulos por columna:")
            print(self.df.isnull().sum())

    def clean_data(self):
        if self.df is not None:
            # elimina filas que estén completamente vacías
            self.df = self.df.dropna(how="all")

            # rellena los vacíos en columnas de texto con "No data"
            self.df["Department"] = self.df["Department"].fillna("No data")
            self.df["Category"] = self.df["Category"].fillna("No data")
            self.df["Item"] = self.df["Item"].fillna("No data")
            self.df["Description"] = self.df["Description"].fillna("No data")

            # convierte las columnas numéricas por si vienen como texto
            self.df["Qty Sold"] = pd.to_numeric(self.df["Qty Sold"], errors="coerce")
            self.df["Sold Price"] = pd.to_numeric(self.df["Sold Price"], errors="coerce")
            self.df["Total Sales"] = pd.to_numeric(self.df["Total Sales"], errors="coerce")

            print("\nDatos limpiados correctamente.")

    def normalize_columns(self):
        if self.df is not None:
            # aquí básicamente le hace un "lavado" a los nombres de columnas
            self.df.columns = self.df.columns.str.strip().str.lower().str.replace(" ", "_")

            print("\nColumnas después de normalizar:")
            print(self.df.columns)

    def export_clean_data(self, output_file):
        try:
            if self.df is not None:
                # exporta el dataset limpio a csv para que los otros módulos lo usen
                self.df.to_csv(output_file, index=False)
                print("\nArchivo limpio exportado correctamente.")
        except Exception as e:
            print("Error al exportar:", e)


def main():
    # aquí crea el objeto con el archivo y la hoja que vamos a trabajar
    loader = DataLoader("data/raw/Ventas Comparativas 2016 - 2017.xlsx", "DATA2016")

    # estos son los pasos del proceso (tipo pipeline)
    loader.load_data()          # cargo datos
    loader.detect_nulls()       # reviso vacíos
    loader.clean_data()         # limpio datos
    loader.normalize_columns() # normalizo nombres
    loader.export_clean_data("data/cleaned/data2016_clean.csv")  # exporto limpio


# ejecuta todo el programa
main()