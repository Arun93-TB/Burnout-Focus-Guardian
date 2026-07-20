from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    # Get values from frontend
    sleep = float(data.get("sleep", 0))
    work = float(data.get("work", 0))
    mood = float(data.get("mood", 0))
    meetings = float(data.get("meetings", 0))
    caffeine = float(data.get("caffeine", 0))

    risk_score = 0
    causes = []
    actions = []

    # Sleep Analysis
    if sleep < 6:
        risk_score += 25
        causes.append("Not enough sleep")
        actions.append("Sleep at least 7-8 hours every night.")

    # Work Hours Analysis
    if work > 8:
        risk_score += 20
        causes.append("Working long hours")
        actions.append("Take short breaks every hour.")

    # Mood Analysis
    if mood <= 2:
        risk_score += 25
        causes.append("Low mood")
        actions.append("Talk with friends or family and relax.")

    # Meetings Analysis
    if meetings > 5:
        risk_score += 15
        causes.append("Too many meetings")
        actions.append("Reduce unnecessary meetings.")

    # Caffeine Analysis
    if caffeine > 3:
        risk_score += 15
        causes.append("High caffeine intake")
        actions.append("Drink more water and reduce caffeine.")

    # Risk Level
    if risk_score <= 25:
        risk_level = "Low"
    elif risk_score <= 50:
        risk_level = "Medium"
    elif risk_score <= 75:
        risk_level = "High"
    else:
        risk_level = "Very High"

    if not causes:
        causes.append("No major burnout signs detected.")
        actions.append("Keep maintaining your healthy lifestyle!")

    return jsonify({
        "risk_score": risk_score,
        "risk_level": risk_level,
        "causes": causes,
        "actions": actions
    })


if __name__ == "__main__":
    app.run(debug=True)