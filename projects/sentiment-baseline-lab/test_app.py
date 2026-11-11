import pytest
from core import predict
from app import app
def test_unknown_abstains(): assert predict("zzzzqqq")['label'] == 'abstain'
def test_empty():
    with pytest.raises(ValueError): predict("  ")
def test_known(): assert predict("wonderful excellent")['label'] == 'positive'
def test_web():
    assert app.test_client().post("/",data={"text":"good service"}).status_code == 200
