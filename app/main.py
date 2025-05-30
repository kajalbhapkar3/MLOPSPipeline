
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
from src.deploying.predict import load_model, make_prediction

app = Flask(__name__)
model = load_model()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        engine_hp = float(request.form["engine_hp"])
        prediction = make_prediction(model, {"engine_hp": engine_hp})
        return render_template("result.html", engine_hp=engine_hp, prediction=round(prediction, 2))
    except Exception as e:
        return f"❌ Error: {e}"

@app.route("/health", methods=["GET"])
def health():
    return "✅ API is live!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)