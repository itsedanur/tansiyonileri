

import pandas as pd
import numpy as np

def split_bp(col: pd.Series) -> pd.DataFrame:
    def _split(x):
        try:
            sys, dia = x.split("/")
            return int(sys), int(dia)
        except Exception:
            return np.nan, np.nan
    return (
        col.apply(_split)
           .apply(pd.Series)
           .rename(columns={0: "sistolik", 1: "diyastolik"})
    )
