import json
from flask import Flask, render_template, request
from core import compare
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 65536
@app.route("/", methods=["GET", "POST"])
def index():
    resume = request.form.get("resume", "Fictional sample: built Python and Flask tools using SQL.")
    job = request.form.get("job", "Python, SQL, Flask and Docker experience.")
    result = error = None
    if request.method == "POST":
        try: result = json.dumps(compare(resume, job), indent=2)
        except ValueError as exc: error = str(exc)
    return render_template("index.html", title="Interview Evidence Lab", subtitle="Trace skill mentions. Prepare better human interviews.", notice="No ranking, personality inference, emotion detection or automated hiring decisions.", action="Compare evidence", result=result, error=error, resume=resume, job=job)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
