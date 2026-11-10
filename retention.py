import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.dummy import DummyRegressor
FEATURES = ["Monthly_Spend", "Tenure_Months", "Support_Tickets", "Engagement_Score"]
def generate_customer_data():
    # Preserve original NumPy seed and draw order for reviewable behavior.
    rng = np.random.RandomState(42)
    n = 300
    df = pd.DataFrame({
        "CustomerID":[f"CU-{i:04d}" for i in range(1001,1001+n)],
        "Segment":rng.choice(['Champions','Loyalists','At Risk','Hibernating'],size=n,p=[.3,.4,.2,.1]),
        "Monthly_Spend":rng.uniform(50,800,n).round(2),
        "Tenure_Months":rng.randint(2,60,n),
        "Support_Tickets":rng.randint(0,10,n),
        "Engagement_Score":rng.uniform(15,100,n).round(1)})
    df["Churn_Risk"] = (100-df.Engagement_Score+df.Support_Tickets*7.5).clip(0,100).round(1)
    return df

def fit_model(data):
    x = data[FEATURES]; y = data.Churn_Risk
    xt,xv,yt,yv = train_test_split(x,y,test_size=.2,random_state=42)
    model = RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1).fit(xt,yt)
    pred = model.predict(xv)
    baseline = DummyRegressor(strategy="mean").fit(xt,yt).predict(xv)
    metrics = {"method":"Fixed random 240/60 split, seed 42. Synthetic formula approximation, not churn probability estimation.","mae":float(mean_absolute_error(yv,pred)),"r2":float(r2_score(yv,pred)),"mean_baseline_mae":float(mean_absolute_error(yv,baseline)),"formula_baseline_mae":float(mean_absolute_error(yv,(100-xv.Engagement_Score+7.5*xv.Support_Tickets).clip(0,100).round(1)))}
    importance = pd.DataFrame({"Feature":FEATURES,"Importance":model.feature_importances_}).sort_values("Importance",ascending=False)
    stats = {"means":x.mean().to_dict(),"mins":x.min().to_dict(),"maxs":x.max().to_dict()}
    return model,importance,stats,metrics
