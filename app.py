import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict_api", methods=["POST"])
def predict_api():

    data = request.json

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    result = "Yes" if prediction == 1 else "No"

    return jsonify({"Churn Prediction": result})


if __name__ == "__main__":
    app.run(debug=True)