import json
from pathlib import Path
import pandas as pd
from core import load_data, evaluate
summary, rows = evaluate(load_data())
print(json.dumps(summary, indent=2))
Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/evaluation.json").write_text(json.dumps(summary,indent=2)+"\n")
pd.DataFrame(rows).to_csv("artifacts/predictions.csv",index=False)
