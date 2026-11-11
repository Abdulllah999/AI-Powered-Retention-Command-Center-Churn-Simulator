import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
FEATURES = ["fever", "cough", "sneezing", "itchy_eyes", "fatigue"]
LABELS = ["Synthetic cold-like pattern", "Synthetic flu-like pattern", "Synthetic allergy-like pattern"]
def make_data(seed=73, n=600):
    rng = np.random.default_rng(seed)
    labels = rng.integers(0, 3, n)
    probabilities = np.array([[.25,.65,.70,.15,.35],[.85,.80,.20,.10,.85],[.05,.20,.85,.85,.15]])
    x = (rng.random((n, 5)) < probabilities[labels]).astype(int)
    return pd.DataFrame(x, columns=FEATURES), np.array(LABELS)[labels]
def fit():
    x, y = make_data()
    xt, xv, yt, yv = train_test_split(x, y, test_size=.25, stratify=y, random_state=42)
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42).fit(xt, yt)
    return model, xt, xv, yt, yv
MODEL, _, _, _, _ = fit()
def predict(values):
    if len(values) != 5 or any(type(v) is not int or v not in (0,1) for v in values):
        raise ValueError("Provide five binary feature values.")
    if not any(values):
        return {"pattern":"abstain", "note":"No selected features; no inference is made."}
    label = str(MODEL.predict(pd.DataFrame([values], columns=FEATURES))[0])
    return {"pattern":label, "note":"This matches artificial training patterns, not a diagnosis. Real conditions overlap and may be serious."}
def faq(topic):
    answers = {
        "about":"This model learns invented symptom-pattern distributions. It cannot diagnose, recommend treatment, or estimate clinical risk.",
        "privacy":"No patient data is used. Inputs are not stored by the application. Use fictional cases only.",
        "help":"For real symptoms, contact a qualified clinician. Seek urgent local medical help for severe or worsening symptoms, including breathing difficulty. This is not a complete triage guide."
    }
    if topic not in answers: raise ValueError("Choose a supported FAQ topic.")
    return answers[topic]
