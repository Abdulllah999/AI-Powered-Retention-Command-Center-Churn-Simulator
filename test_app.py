import pytest
from core import predict, faq
from app import app
def test_abstains(): assert predict([0]*5)["pattern"] == "abstain"
@pytest.mark.parametrize("x", [[1,0], [1,0,2,0,0], [True,0,0,0,0]])
def test_rejects_bad_features(x):
    with pytest.raises(ValueError): predict(x)
def test_api():
    c = app.test_client()
    assert c.post("/api/pattern",json={"features":[1,1,0,0,1]}).status_code == 200
    assert c.post("/api/pattern",json={"features":[2]*5}).status_code == 400
    assert c.post("/api/pattern",json=[]).status_code == 400
def test_faq_is_not_diagnosis(): assert "cannot diagnose" in faq("about")
