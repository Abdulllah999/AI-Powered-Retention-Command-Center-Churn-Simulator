import numpy as np
from retention import generate_customer_data, fit_model, FEATURES
from streamlit.testing.v1 import AppTest
def test_generator_deterministic():
    a=generate_customer_data(); b=generate_customer_data()
    assert a.equals(b) and len(a)==300 and a.Churn_Risk.between(0,100).all()
def test_formula_baseline_is_exact():
    model,_,_,metrics=fit_model(generate_customer_data())
    assert metrics["formula_baseline_mae"] == 0
    assert metrics["mae"] < metrics["mean_baseline_mae"]
    assert np.isfinite(model.predict(generate_customer_data()[FEATURES])).all()
def test_streamlit_empty_filter():
    at = AppTest.from_file("myfile.py").run(timeout=30)
    assert not at.exception
    at.multiselect[0].set_value([]).run(timeout=30)
    assert not at.exception
