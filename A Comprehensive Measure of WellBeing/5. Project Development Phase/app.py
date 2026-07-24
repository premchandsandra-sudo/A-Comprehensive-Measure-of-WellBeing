from flask import Flask, render_template, request
import joblib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(base_dir)
template_dir = os.path.join(project_dir, "3. Project Design Phase")
static_dir = os.path.join(template_dir, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Load model from the same directory or fallback locations
model_path = os.path.join(base_dir, "model.pkl")
if not os.path.exists(model_path):
    model_path = os.path.join(project_dir, "6.Project Testing", "model.pkl")

# If model doesn't exist, we will warn but try to load
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

def get_hdi_category(hdi):
    if hdi < 0.550:
        return "Low Human Development"
    elif hdi < 0.700:
        return "Medium Human Development"
    elif hdi < 0.800:
        return "High Human Development"
    else:
        return "Very High Human Development"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return "Model not trained yet. Please run train_model.py first.", 500
        
    try:
        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        income = float(request.form["income"])

        result = model.predict([
            [life, expected, mean, income]
        ])

        prediction = round(float(result[0]), 3)

        # Keep display range between 0 and 1
        prediction = max(0, min(prediction, 1))

        category = get_hdi_category(prediction)
        percentage = round(prediction * 100, 1)

        return render_template(
            "result.html",
            prediction=prediction,
            percentage=percentage,
            category=category,
            life=life,
            expected=expected,
            mean=mean,
            income=income
        )
    except Exception as e:
        return f"Error during prediction: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5000)
