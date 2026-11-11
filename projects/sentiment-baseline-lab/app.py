import json
from flask import Flask, render_template, request
from core import predict
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8192
@app.route("/", methods=["GET", "POST"])
def index():
    text = request.form.get("text", "Excellent service and good quality")
    result = error = None
    if request.method == "POST":
        try: result = json.dumps(predict(text), indent=2)
        except ValueError as exc: error = str(exc)
    return render_template("index.html", title="Sentiment Baseline Lab", subtitle="A small, inspectable TF-IDF classification pipeline.", notice="Authored examples only. No Twitter data, API access or real-world accuracy claim.", action="Classify text", result=result, error=error, text=text)
if __name__ == "__main__": app.run(host="127.0.0.1", port=5002)
