import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import random

app = Flask(__name__)

# load trained model
model = pickle.load(open("model.pkl","rb"))

# load dataset
df = pd.read_csv("data/Telco_Customer_Churn_lyst1769326950438.csv")

# Fix TotalCharges column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# convert churn to numeric
df["Churn"] = df["Churn"].map({"No":0,"Yes":1})

# model features
features = df.drop(columns=["customerID","Churn"])
target = df["Churn"]


# ===============================
# MODEL PERFORMANCE CALCULATION
# ===============================

y_pred = model.predict(features)

accuracy = accuracy_score(target, y_pred)
precision = precision_score(target, y_pred)
recall = recall_score(target, y_pred)
f1 = f1_score(target, y_pred)
cm = confusion_matrix(target, y_pred)

model_metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1),
    "confusion_matrix": cm.tolist()
}
# ===============================
# ROUTES
# ===============================
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/model_metrics")
def model_metrics_page():
    return render_template("model_metrics.html")

@app.route("/pipeline")
def pipeline_page():
    return render_template("pipeline.html")

@app.route("/model_metrics_api")
def model_metrics_api():
    return jsonify(model_metrics)

@app.route("/predict_api", methods=["POST"])
def predict_api():

    data = request.json

    input_df = pd.DataFrame([data])

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    prediction = "Yes" if pred == 1 else "No"

    # find actual churn from dataset
    actual = None
   
    try:
        match = df[
            (df["customerID"] == (data["customerID"]))
        ]        

        if len(match) > 0:
            actual = "Yes" if match.iloc[0]["Churn"] == 1 else "No"

    except:
        actual = None

    return jsonify({
        "prediction": prediction,
        "probability": float(prob),
        "actual": actual
    })

@app.route("/sample/<type>")
def sample(type):

    if type == "random":
        row = df.sample(1)

    elif type == "high":
        row = df[df["Churn"] == 1].sample(1)

    elif type == "low":
        row = df[df["Churn"] == 0].sample(1)

    elif type == "sample1":
        row = df.sample(1)

    elif type == "sample2":
        row = df.sample(1)

    actual = "Yes" if row.iloc[0]["Churn"] == 1 else "No"

    features_row = row.drop(columns=["Churn"])

    return jsonify({
        "data": features_row.to_dict(orient="records")[0],
        "actual": actual
    })

if __name__ == "__main__":
    app.run(debug=True)