from flask import Flask, render_template, request
import pickle

# Load the trained model and vectorizer
model = pickle.load(open("finalized_model.pkl", "rb"))
vector = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if request.method == "POST":

        news = request.form["news"].strip()

        # Check for empty input
        if news == "":
            return render_template(
                "prediction.html",
                prediction_text="⚠ Please enter a news headline."
            )

        # Predict
        predict = model.predict(vector.transform([news]))

        result = predict[0]   # Get the actual prediction string

        # Display user-friendly message
        if result.upper() == "FAKE":
            message = "❌ This news is predicted to be FAKE."
        else:
            message = "✅ This news is predicted to be REAL."

        return render_template(
            "prediction.html",
            prediction_text=message
        )

    return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)