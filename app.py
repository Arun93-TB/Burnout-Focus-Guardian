from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

MOTIVATION_QUOTES = [
    "Take care of yourself. Productivity follows wellness.",
    "Small breaks lead to big achievements.",
    "Rest is not laziness; it is preparation.",
    "Your health is your greatest wealth.",
    "Balance work and life for long-term success."
]

HEALTH_TIPS = [
    "Drink at least 2 liters of water daily.",
    "Walk for 20 minutes every day.",
    "Sleep 7-8 hours every night.",
    "Avoid too much caffeine.",
    "Practice deep breathing for 5 minutes."
]

def calculate_burnout(sleep, work, mood, meetings, caffeine):
    score = 0
    causes = []
    actions = []

    if sleep < 6:
        score += 25
        causes.append("Insufficient sleep")
        actions.append("Sleep at least 7-8 hours.")

    elif sleep >= 8:
        score -= 5

    if work > 8:
        score += 20
        causes.append("Long working hours")
        actions.append("Take a 10-minute break every hour.")

    if mood <= 2:
        score += 25
        causes.append("Low mood")
        actions.append("Spend time with friends or family.")

    elif mood >= 4:
        score -= 5

    if meetings > 5:
        score += 15
        causes.append("Too many meetings")
        actions.append("Reduce unnecessary meetings.")

    if caffeine > 3:
        score += 15
        causes.append("High caffeine intake")
        actions.append("Reduce coffee and drink more water.")

    score = max(0, min(score, 100))

    return score, causes, actions


@app.route("/")
def home():
    return jsonify({
        "project": "Burnout & Focus Guardian",
        "developer": "Arun Kumar",
        "status": "Backend Running Successfully"
    })


@app.route("/status")
def status():
    return jsonify({
        "server": "Online",
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    sleep = float(data.get("sleep", 0))
    work = float(data.get("work", 0))
    mood = float(data.get("mood", 0))
    meetings = float(data.get("meetings", 0))
    caffeine = float(data.get("caffeine", 0))

    risk_score, causes, actions = calculate_burnout(
        sleep,
        work,
        mood,
        meetings,
        caffeine
    )

    if risk_score <= 25:
        risk_level = "Low"

    elif risk_score <= 50:
        risk_level = "Medium"

    elif risk_score <= 75:
        risk_level = "High"

    else:
        risk_level = "Very High"

    health_score = 100 - risk_score

    if not causes:
        causes.append("No major burnout symptoms detected.")

    if not actions:
        actions.append("Keep maintaining your healthy lifestyle.")

    response = {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "health_score": health_score,
        "causes": causes,
        "actions": actions,
        "motivation": random.choice(MOTIVATION_QUOTES),
        "wellness_tip": random.choice(HEALTH_TIPS),
        "analysis_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    return jsonify(response)


@app.route("/tips")
def tips():
    return jsonify({
        "tips": HEALTH_TIPS
    })


@app.route("/motivation")
def motivation():
    return jsonify({
        "quote": random.choice(MOTIVATION_QUOTES)
    })


@app.route("/about")
def about():
    return jsonify({
        "Project": "Burnout & Focus Guardian",
        "Version": "1.0",
        "Technology": "Python Flask",
        "Purpose": "Predict burnout risk and provide wellness suggestions."
    })


if __name__ == "__main__":
    app.run(debug=True)