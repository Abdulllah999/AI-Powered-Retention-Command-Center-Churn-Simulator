from pathlib import Path
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
DATA = Path(__file__).parent / "data" / "examples.csv"
def train():
    data = pd.read_csv(DATA)
    training = data[data["split"] == "train"]
    model = make_pipeline(TfidfVectorizer(ngram_range=(1,2)), LogisticRegression(max_iter=1000, random_state=42))
    model.fit(training["text"], training["label"])
    return model
MODEL = train()
def predict(text):
    if not text.strip() or len(text) > 2000:
        raise ValueError("Enter between 1 and 2,000 characters.")
    vector = MODEL.named_steps["tfidfvectorizer"].transform([text])
    if vector.nnz == 0:
        return {"label":"abstain", "reason":"No known vocabulary. A larger representative dataset is needed."}
    return {"label":str(MODEL.predict([text])[0]), "note":"Toy fixture model; sarcasm, negation and domain shifts can fail."}
