from flask import Flask, jsonify, render_template, request
from analyzer.parser import parse_log
from analyzer.rules import analyze_events

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/analyze")
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No log file uploaded."}), 400
    uploaded = request.files["file"]
    if not uploaded.filename:
        return jsonify({"error": "Please choose a log file."}), 400
    try:
        raw = uploaded.read().decode("utf-8", errors="replace")
        events = parse_log(raw)
        alerts = analyze_events(events)
        return jsonify({
            "filename": uploaded.filename,
            "events": events,
            "alerts": alerts,
            "summary": {
                "events": len(events),
                "alerts": len(alerts),
                "critical": sum(a["severity"] == "CRITICAL" for a in alerts),
                "high": sum(a["severity"] == "HIGH" for a in alerts),
            },
        })
    except Exception as exc:
        return jsonify({"error": f"Could not analyze log: {exc}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
