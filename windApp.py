from flask import Flask, render_template, request, session, redirect, url_for
import joblib
import requests
import os
from dotenv import load_dotenv
import webbrowser

load_dotenv()

app = Flask(__name__)
app.secret_key = "windenergysecret"

# Load ML model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "power_prediction.pkl")
model = joblib.load(model_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.route('/')
def home():
    return render_template("intro.html")


@app.route('/predict')
def predict():
    return render_template(
        "predict.html",
        temp=session.get('temp'),
        humid=session.get('humid'),
        pressure=session.get('pressure'),
        speed=session.get('speed'),
        prediction_text=session.get('prediction'),
        input_theo=session.get('input_theo'),
        input_wind=session.get('input_wind'),
        city=session.get('city'),
        error=session.get('error')
    )


# 🌦 WEATHER ROUTE
@app.route('/windapi', methods=['POST'])
def windapi():
    city = request.form.get('city')
    session['city'] = city

    if not API_KEY:
        session['error'] = "API key not configured"
        return redirect(url_for('predict'))

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        resp = requests.get(url, timeout=5).json()

        if resp.get("cod") != 200:
            session['error'] = resp.get("message", "City not found")
            return redirect(url_for('predict'))

        # Store NUMERIC values for ML
        session['temp'] = resp['main']['temp']
        session['humid'] = resp['main']['humidity']
        session['pressure'] = resp['main']['pressure']
        session['speed'] = resp['wind']['speed']
        session.pop('error', None)

    except Exception:
        session['error'] = "Weather service unavailable"

    return redirect(url_for('predict'))


# ⚡ PREDICTION ROUTE
@app.route('/y_predict', methods=['POST'])
def y_predict():
    try:
        theo = float(request.form['theo'])      # Theoretical Power
        wind = float(request.form['wind'])      # Wind Speed

        prediction = model.predict([[wind, theo]])
        result = round(prediction[0], 2)

        session['prediction'] = f"Predicted Wind Energy: {result} kWh"
        session['input_theo'] = theo
        session['input_wind'] = wind
        session.pop('error', None)

    except ValueError:
        session['error'] = "Please enter valid numeric values."

    return redirect(url_for('predict'))

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open_new("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
