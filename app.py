from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = 'model/student_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError("Model not found! Run train_model.py first.")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    if request.method == "POST":
        # Get user input
        hours = float(request.form['hours'])
        attendance = float(request.form['attendance'])
        assignments = float(request.form['assignments'])
        previous_marks = float(request.form['previous_marks'])

        # validation rules
        if hours > 12:
            hours = 12

        if attendance > 100:
            attendance = 100

        if assignments > 10:
            assignments = 10

        if previous_marks > 100:
            previous_marks = 100

        # Predict
        features = np.array([[hours, attendance, assignments, previous_marks]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]  # probability of passing

    return render_template("index.html", prediction=prediction, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)