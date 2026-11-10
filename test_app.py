import pytest
from core import compare, extract_skills
from app import app
def test_boundaries():
    assert extract_skills("NoSQL pythonic REACT") == {"react"}
def test_exact_evidence():
    r = compare("Python and SQL", "SQL Docker")
    assert r["evidence_terms"] == ["sql"]
    assert r["terms_to_review"] == ["docker"]
def test_demographics_do_not_change_result():
    assert compare("Ali Python age 22", "Python") == compare("Sara Python age 52", "Python")
def test_invalid():
    with pytest.raises(ValueError): compare("", "Python")
def test_web_escapes_input():
    response = app.test_client().post("/", data={"resume":"<script>alert(1)</script> Python", "job":"Python"})
    assert response.status_code == 200 and b"<script>" not in response.data
