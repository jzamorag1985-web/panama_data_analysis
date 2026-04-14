import os
import pandas as pd
import numpy as np
from scipy import stats


class StatAnalyzer:
    """
    Clase para realizar análisis estadístico sobre un dataset limpio.
    Calcula correlaciones, distribuciones, percentiles y detección de outliers.
    """

    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("El parámetro 'data' debe ser un pandas DataFrame.")

        if data.empty:
            raise ValueError("El dataset está vacío.")

        self.data = data.copy()
        self.numeric_data = self.data.select_dtypes(include=[np.number]).copy()

        if self.numeric_data.empty:
            raise ValueError("No hay columnas numéricas en el dataset.")

    def get_numeric_columns(self) -> list:
        return self.numeric_data.columns.tolist()

    def calculate_correlations(self) -> pd.DataFrame:
        if self.numeric_data.shape[1] < 2:
            raise ValueError("Se necesitan al menos 2 columnas numéricas para calcular correlaciones.")
        return self.numeric_data.corr().round(4)

    def calculate_percentiles(self, column: str) -> dict:
        values = self._validate_column(column)

        return {
            "P10": float(np.percentile(values, 10)),
            "P25": float(np.percentile(values, 25)),
            "P50": float(np.percentile(values, 50)),
            "P75": float(np.percentile(values, 75)),
            "P90": float(np.percentile(values, 90)),
        }

    def analyze_distribution(self, column: str) -> dict:
        values = self._validate_column(column)

        return {
            "mean": float(np.mean(values)),
            "median": float(np.median(values)),
            "std_dev": float(np.std(values, ddof=1)) if len(values) > 1 else 0.0,
            "variance": float(np.var(values, ddof=1)) if len(values) > 1 else 0.0,
            "skewness": float(stats.skew(values)) if len(values) > 2 else 0.0,
            "kurtosis": float(stats.kurtosis(values)) if len(values) > 3 else 0.0,
            "min": float(np.min(values)),
            "max": float(np.max(values)),
        }

    def detect_outliers_iqr(self, column: str) -> pd.DataFrame:
        values = self._validate_column(column)

        q1 = np.percentile(values, 25)
        q3 = np.percentile(values, 75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        return self.data[
            (self.data[column] < lower) | (self.data[column] > upper)
        ].copy()

    def detect_outliers_zscore(self, column: str, threshold: float = 3.0) -> pd.DataFrame:
        values = self._validate_column(column)

        if np.std(values) == 0:
            return self.data.iloc[0:0].copy()

        z_scores = np.abs(stats.zscore(values))
        valid_index = self.numeric_data[column].dropna().index
        outlier_index = valid_index[z_scores > threshold]

        return self.data.loc[outlier_index].copy()

    def full_statistical_summary(self, column: str) -> dict:
        return {
            "correlations": self.calculate_correlations().to_dict(),
            "distribution": self.analyze_distribution(column),
            "percentiles": self.calculate_percentiles(column),
            "outliers_iqr_count": int(len(self.detect_outliers_iqr(column))),
            "outliers_zscore_count": int(len(self.detect_outliers_zscore(column))),
        }

    def export_results(self, column: str, output_dir: str = "output"):
        """
        Exporta resultados para que el módulo 3 pueda usarlos.
        """
        os.makedirs(output_dir, exist_ok=True)

        correlations = self.calculate_correlations()
        percentiles = self.calculate_percentiles(column)
        distribution = self.analyze_distribution(column)
        outliers_iqr = self.detect_outliers_iqr(column)
        outliers_zscore = self.detect_outliers_zscore(column)

        correlations.to_csv(f"{output_dir}/correlations.csv", index=True)

        pd.DataFrame([percentiles]).to_csv(
            f"{output_dir}/percentiles_{column}.csv",
            index=False
        )

        pd.DataFrame([distribution]).to_csv(
            f"{output_dir}/distribution_{column}.csv",
            index=False
        )

        outliers_iqr.to_csv(
            f"{output_dir}/outliers_iqr_{column}.csv",
            index=False
        )

        outliers_zscore.to_csv(
            f"{output_dir}/outliers_zscore_{column}.csv",
            index=False
        )

        print("\nResultados exportados correctamente en la carpeta output.")

    def _validate_column(self, column: str):
        if column not in self.numeric_data.columns:
            raise ValueError(f"La columna '{column}' no es numérica o no existe.")

        values = self.numeric_data[column].dropna().to_numpy()

        if len(values) == 0:
            raise ValueError(f"La columna '{column}' está vacía.")

        return values


if __name__ == "__main__":
    # Módulo 2 lee el archivo limpio generado por el módulo 1
    df = pd.read_csv("data/cleaned/data2016_clean.csv")

    analyzer = StatAnalyzer(df)

    print("\nColumnas numéricas:")
    print(analyzer.get_numeric_columns())

    print("\nCorrelaciones:")
    print(analyzer.calculate_correlations())

    print("\nPercentiles de total_sales:")
    print(analyzer.calculate_percentiles("total_sales"))

    print("\nDistribución de total_sales:")
    print(analyzer.analyze_distribution("total_sales"))

    print("\nOutliers IQR en total_sales:")
    print(analyzer.detect_outliers_iqr("total_sales").head())

    print("\nOutliers Z-Score en total_sales:")
    print(analyzer.detect_outliers_zscore("total_sales").head())

    analyzer.export_results("total_sales")