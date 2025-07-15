import pandas as pd
from pathlib import Path

def load_excel(path: str | Path):
    df = pd.read_excel(path)
    required = {"Tarih", "Sabah Tansiyon", "Akşam Tansiyon"}
    if not required.issubset(df.columns):
        raise ValueError(f"Excel beklenen kolonları içermiyor: {required}")
    return df
