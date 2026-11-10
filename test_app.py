import numpy as np
import pytest
from core import make_data, features, evaluate, forecast, load_data, FEATURES
from app import app
def test_no_future_features():
    data = make_data()
    changed = data.copy()
    changed.loc[200:, "close"] *= 2
    changed.loc[200:, "sentiment"] = .99
    np.testing.assert_allclose(features(data).loc[199,FEATURES].to_numpy(dtype=float),features(changed).loc[199,FEATURES].to_numpy(dtype=float))
def test_next_day_label():
    data = make_data()
    assert features(data).loc[20,"target_next_close"] == data.loc[21,"close"]
def test_last_origin_uses_no_future_price():
    result = forecast(make_data())
    assert np.isfinite(result["predicted_next_close"])
def test_rejects_unsorted(tmp_path):
    p=tmp_path/'bad.csv'; make_data().iloc[::-1].to_csv(p,index=False)
    with pytest.raises(ValueError): load_data(p)
def test_walk_forward():
    summary, rows = evaluate(make_data().iloc[:120])
    assert len(rows)>0 and summary["persistence_mae"] >= 0
    assert all(r["target_date"] > r["origin"] for r in rows)
def test_web(): assert app.test_client().post("/").status_code == 200
