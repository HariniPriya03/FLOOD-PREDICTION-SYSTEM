from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("floods.save")
scaler = joblib.load("transform.save")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET"])
def predict_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    cloud_cover = float(request.form["Cloud_Cover"])
    annual = float(request.form["Annual"])
    jan_feb = float(request.form["Jan_Feb"])
    mar_may = float(request.form["Mar_May"])
    jun_sep = float(request.form["Jun_Sep"])

    data = pd.DataFrame(
        [[cloud_cover, annual, jan_feb, mar_may, jun_sep]],
        columns=[
            "Cloud Cover",
            "ANNUAL",
            "Jan-Feb",
            "Mar-May",
            "Jun-Sep"
        ]
    )

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return render_template("chance.html")
    else:
        return render_template("no_chance.html")


if __name__ == "__main__":
    app.run(debug=True)