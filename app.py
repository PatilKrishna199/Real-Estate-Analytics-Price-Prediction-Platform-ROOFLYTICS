from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pandas as pd
import os

# Blueprints
from routes.predictions import predictions_bp
from routes.investments import investments_bp

# Flask setup
app = Flask(__name__)
CORS(app)

# -------------------- DATASET LOADING --------------------

DATA_PATH = os.path.join(os.path.dirname(__file__), "real_data.csv")

try:
    real_estate_data = pd.read_csv(DATA_PATH)
    print("✅ Dataset loaded successfully from local file.")
    print("Columns:", real_estate_data.columns.tolist())
except Exception as e:
    print("❌ Failed to load dataset:", e)
    real_estate_data = pd.DataFrame()

# -------------------- FRONTEND ROUTE --------------------

@app.route("/")
def index():
    cities = sorted(real_estate_data["City"].dropna().unique())
    property_types = sorted(real_estate_data["PropertyType"].dropna().unique())

    # Show some properties on landing page
    properties = real_estate_data.head(12).to_dict(orient="records")

    return render_template(
        "index.html",
        cities=cities,
        property_types=property_types,
        properties=properties
    )

# -------------------- REGISTER BLUEPRINTS --------------------

app.register_blueprint(predictions_bp)
app.register_blueprint(investments_bp)

# -------------------- HEALTH CHECK --------------------

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK", "message": "Real Estate AI API running"}), 200

# -------------------- RUN SERVER --------------------

if __name__ == "__main__":
    print("🌐 Visit your site at: http://localhost:5000")
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )



# How to run project
# cd "C:\Users\krp36\Real Estate Project\new web for cep\checking unit 1"
# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# python app.py
