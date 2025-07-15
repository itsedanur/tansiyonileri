from tsyn.data_loader import load_excel
import pytest, pandas as pd

def test_invalid_columns(tmp_path):
    bad = tmp_path/"bad.xlsx"
    pd.DataFrame({"Foo":[1]}).to_excel(bad, index=False)
    with pytest.raises(ValueError):
        load_excel(bad)
