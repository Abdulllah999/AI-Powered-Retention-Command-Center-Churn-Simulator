from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
FEATURES = ["close", "return_1", "return_5", "volatility_5", "sentiment"]
def make_data():
    rng = np.random.default_rng(19)
    n = 360
    sentiment = rng.normal(0, .5, n).clip(-1,1)
    shocks = rng.normal(0, .012, n)
    returns = np.zeros(n)
    for i in range(1,n): returns[i] = .0003 + .08*returns[i-1] + .002*sentiment[i-1] + shocks[i]
    dates = pd.bdate_range("2024-01-01", periods=n)
    return pd.DataFrame({"date":dates,"close":100*np.exp(np.cumsum(returns)),"sentiment":sentiment})
def load_data(path=None):
    if path is None: path = Path(__file__).parent / "data" / "synthetic_market.csv"
    df = pd.read_csv(path, parse_dates=["date"])
    if len(df)<100 or not {"date","close","sentiment"} <= set(df): raise ValueError("Need at least 100 rows with date, close and sentiment.")
    if df.date.isna().any() or not df.date.is_monotonic_increasing or df.date.duplicated().any(): raise ValueError("Dates must be valid, unique and strictly increasing.")
    for col in ["close","sentiment"]: df[col] = pd.to_numeric(df[col], errors="raise")
    if not np.isfinite(df[["close","sentiment"]].to_numpy()).all() or (df.close<=0).any() or not df.sentiment.between(-1,1).all(): raise ValueError("Invalid price or sentiment values.")
    return df

def features(df):
    frame = df.copy()
    frame["return_1"] = frame.close.pct_change()
    frame["return_5"] = frame.close.pct_change(5)
    frame["volatility_5"] = frame.return_1.rolling(5).std()
    frame["target_next_close"] = frame.close.shift(-1)
    frame["target_date"] = frame.date.shift(-1)
    return frame

def evaluate(df):
    frame = features(df).dropna().reset_index(drop=True)
    start = int(len(frame)*.8)
    rows = []
    for i in range(start,len(frame)):
        # At close t, only labels with target_date <= t are available.
        history = frame.iloc[:i]
        assert history.target_date.max() <= frame.iloc[i].date
        model = make_pipeline(StandardScaler(), Ridge(alpha=10.0))
        model.fit(history[FEATURES], history.target_next_close)
        pred = float(model.predict(frame.iloc[[i]][FEATURES])[0])
        # Ablation: identical model without news sentiment.
        price_only = make_pipeline(StandardScaler(), Ridge(alpha=10.0))
        price_only.fit(history[FEATURES[:-1]], history.target_next_close)
        price_pred = float(price_only.predict(frame.iloc[[i]][FEATURES[:-1]])[0])
        rows.append({"origin":frame.iloc[i].date.isoformat(),"target_date":frame.iloc[i].target_date.isoformat(),"actual":float(frame.iloc[i].target_next_close),"ridge":pred,"price_only":price_pred,"persistence":float(frame.iloc[i].close)})
    scores = {f"{name}_mae":float(mean_absolute_error([r["actual"] for r in rows],[r[name] for r in rows])) for name in ["ridge","price_only","persistence"]}
    return {"method":"Expanding-window one-step-ahead evaluation on last 20%; fixed alpha 10, no test tuning; sentiment available by origin close.","train_first_fold":start,"test_origins":len(rows), **scores, "data":"Synthetic market, seed 19. No evidence of trading performance."}, rows

def forecast(df):
    frame = features(df)
    train = frame.dropna()
    model = make_pipeline(StandardScaler(), Ridge(alpha=10.0))
    model.fit(train[FEATURES], train.target_next_close)
    latest = frame.iloc[[-1]]
    return {"origin":str(latest.date.iloc[0].date()),"predicted_next_close":round(float(model.predict(latest[FEATURES])[0]),4),"persistence_baseline":round(float(latest.close.iloc[0]),4),"note":"Synthetic point estimate; no calibrated interval or investment guidance."}
