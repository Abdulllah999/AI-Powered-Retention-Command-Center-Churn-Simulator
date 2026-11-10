import json
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.dummy import DummyClassifier
from core import DATA, MODEL
data = pd.read_csv(DATA)
train = data[data.split == "train"]
test = data[data.split == "test"]
assert set(train.text.str.lower()).isdisjoint(set(test.text.str.lower()))
pred = MODEL.predict(test.text)
baseline = DummyClassifier(strategy="most_frequent").fit(train.text, train.label).predict(test.text)
print(json.dumps({"method":"Fixed authored holdout: 24 train / 9 test; vocabulary fitted only on train. Shared phrasing makes this a smoke evaluation, not Twitter validation.","accuracy":accuracy_score(test.label,pred),"macro_f1":f1_score(test.label,pred,average="macro"),"baseline_accuracy":accuracy_score(test.label,baseline),"label_order":["negative","neutral","positive"],"confusion_matrix":confusion_matrix(test.label,pred,labels=["negative","neutral","positive"]).tolist()},indent=2))
