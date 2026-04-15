import pandas as pd
from data_loader import DataLoader

if __name__ == "__main__":
    test = DataLoader(
        "data/raw/Ventas Comparativas 2016 - 2017.xlsx",
        "DATA2016"
    )

    test.load_data()
    test.detect_nulls()
    test.clean_data()
    test.normalize_columns()
    test.export_clean_data("data/cleaned/data2016_clean.csv")
    
    