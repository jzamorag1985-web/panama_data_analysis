import os
import pandas as pd
import numpy as np
from fpdf import FPDF


class ReportGenerator:

    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(base_path, "data", "cleaned", "data2016_clean.csv")
        self.output_path = os.path.join(base_path, "report.pdf")

    def load_data(self):
        return pd.read_csv(self.data_path)

    def basic_info(self, df):
        info = []
        info.append(f"Filas: {df.shape[0]}")
        info.append(f"Columnas: {df.shape[1]}")
        return "\n".join(info)

    def null_values(self, df):
        return df.isnull().sum().to_string()

    def describe_data(self, df):
        return df.describe().to_string()

    def correlations(self, df):
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.shape[1] > 1:
            return numeric_df.corr().to_string()
        return "No hay suficientes columnas numéricas para correlación"

    def top_values(self, df):
        results = []
        for col in df.select_dtypes(include=['object']).columns:
            results.append(f"Columna: {col}")
            results.append(df[col].value_counts().head(5).to_string())
            results.append("")
        return "\n".join(results)

    def generate_report(self):
        df = self.load_data()

        info = self.basic_info(df)
        nulls = self.null_values(df)
        desc = self.describe_data(df)
        corr = self.correlations(df)
        top = self.top_values(df)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        pdf.cell(200, 10, txt="REPORTE DE ANALISIS DE DATOS", ln=True)

        pdf.ln(5)
        pdf.cell(200, 10, txt="INFORMACION GENERAL", ln=True)
        for line in info.split("\n"):
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.ln(5)
        pdf.cell(200, 10, txt="VALORES NULOS", ln=True)
        for line in nulls.split("\n"):
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.add_page()
        pdf.cell(200, 10, txt="ESTADISTICAS DESCRIPTIVAS", ln=True)
        for line in desc.split("\n"):
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.add_page()
        pdf.cell(200, 10, txt="CORRELACIONES", ln=True)
        for line in corr.split("\n"):
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.add_page()
        pdf.cell(200, 10, txt="VALORES MAS FRECUENTES", ln=True)
        for line in top.split("\n"):
            pdf.cell(200, 8, txt=line, ln=True)

        pdf.output(self.output_path)


if __name__ == "__main__":
    generator = ReportGenerator()
    generator.generate_report()