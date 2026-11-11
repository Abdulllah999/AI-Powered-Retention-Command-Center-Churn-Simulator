import json
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.dummy import DummyClassifier
from core import fit, LABELS
model, xt, xv, yt, yv = fit()
pred = model.predict(xv)
baseline = DummyClassifier(strategy="most_frequent").fit(xt,yt).predict(xv)
print(json.dumps({"method":"600 artificial cases; fixed stratified 450/150 split. Duplicate binary patterns can cross splits; score measures synthetic generator recovery only, not clinical validity.","accuracy":accuracy_score(yv,pred),"macro_f1":f1_score(yv,pred,average="macro"),"baseline_accuracy":accuracy_score(yv,baseline),"labels":LABELS,"confusion_matrix":confusion_matrix(yv,pred,labels=LABELS).tolist()},indent=2))
