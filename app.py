from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

with open("fraud_model.pkl", "rb") as file:
    model = pickle.load(file)

locations = {
    "Hyderabad": 0,
    "Mumbai": 1,
    "Delhi": 2,
    "Chennai": 3,
    "Bangalore": 4
}


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    amount = float(data["amount"])
    location = locations[data["location"]]
    time = int(data["time"].split(":")[0])
    transactions = int(data["transactions"])

    transaction = [[
        amount,
        location,
        time,
        transactions
    ]]

    reasons = []

    if amount >= 40000:
        reasons.append("High transaction amount")

    if time < 5:
        reasons.append("Transaction made during unusual hours")

    if transactions >= 7:
        reasons.append("High transaction frequency")

    if location != 0:
        reasons.append("Transaction location differs from expected location")

    if len(reasons) == 0:
        reasons.append("No major risk indicators detected")

    prediction = model.predict(transaction)[0]

    probability = model.predict_proba(transaction)[0][1]

    risk_percentage = round(probability * 100)

    if prediction == 1:
        result = "Potential Fraud ⚠️"
    else:
        result = "Normal Transaction ✅"

    return jsonify({
        "prediction": int(prediction),
        "result": result,
        "risk_percentage": risk_percentage,
        "reasons": reasons
    })

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def frontend(filename):
    if filename in ["script.js", "style.css"]:
        return send_from_directory(".", filename)
    return "Not Found", 404
    
if __name__ == "__main__":
    app.run(debug=True)
