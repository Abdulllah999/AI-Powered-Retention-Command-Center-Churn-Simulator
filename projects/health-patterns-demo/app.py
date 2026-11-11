import json
from flask import Flask, render_template, request, jsonify
from core import FEATURES, predict, faq
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8192
@app.route("/", methods=["GET", "POST"])
def index():
    result = error = None
    selected = request.form.getlist("symptom") if request.method == "POST" else ["cough", "sneezing"]
    topic = request.form.get("topic", "about")
    if request.method == "POST":
        try:
            if any(s not in FEATURES for s in selected): raise ValueError("Unknown feature.")
            result = json.dumps({**predict([int(s in selected) for s in FEATURES]), "faq":faq(topic)}, indent=2)
        except ValueError as exc: error = str(exc)
    return render_template("index.html", title="Health Pattern Explorer", subtitle="Study classification with fictional symptom patterns.", notice="Educational simulation. Not a disease diagnosis, clinical probability or treatment tool. FAQ responses are fixed text, not an AI clinician.", action="Explore fictional pattern", result=result, error=error, features=FEATURES, selected=selected, topic=topic)
@app.post("/api/pattern")
def api_pattern():
    data = request.get_json(silent=True)
    if not isinstance(data, dict): return jsonify(error="Expected a JSON object."), 400
    try: return jsonify(predict(data.get("features", [])))
    except (ValueError, TypeError) as exc: return jsonify(error=str(exc)), 400
if __name__ == "__main__": app.run(host="127.0.0.1", port=5003)
