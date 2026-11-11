import json
from core import compare
cases = [("Python SQL", "SQL Docker", ["sql"], ["docker"]), ("pythonic NoSQL", "Python SQL", [], ["python", "sql"]), ("FLASK React", "Flask React", ["flask", "react"], [])]
passed = sum(compare(a,b)["evidence_terms"] == c and compare(a,b)["terms_to_review"] == d for a,b,c,d in cases)
result = {"method":"Three authored exact-match cases; functional validation, not hiring validity", "passed":passed,"total":len(cases)}
print(json.dumps(result, indent=2))
assert passed == len(cases)
