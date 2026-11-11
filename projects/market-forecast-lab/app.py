import json
from flask import Flask, render_template, request
from core import load_data, forecast
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()
    result = json.dumps(forecast(data),indent=2) if request.method == "POST" else None
    return render_template("index.html", title="Market Forecast Lab", subtitle="Can a forecasting model beat yesterday’s close?", notice="Synthetic prices and news-sentiment features. Educational forecasting experiment; no market feed or investment recommendation.", action="Forecast next synthetic close", result=result, error=None, last_date=str(data.date.iloc[-1].date()), last_close=round(float(data.close.iloc[-1]),2))
if __name__ == "__main__": app.run(host="127.0.0.1", port=5004)
