from flask import Blueprint, request, jsonify
import pandas as pd
import os
import inflect
from models.predictor import predict_price
from models.loan_calc import calculate_loan

# Create Blueprint
predictions_bp = Blueprint("predictions", __name__)

# Load dataset (city-based)
DATASET_PATH = os.path.join(os.path.dirname(__file__), "../data/real_data.csv")

try:
    real_estate_data = pd.read_csv(DATASET_PATH)
    print("✅ Dataset Loaded Successfully!")
    print("Columns:", real_estate_data.columns.tolist())
except Exception as e:
    print(f"❌ Error Loading Dataset: {e}")
    real_estate_data = pd.DataFrame()

# Number to words engine
p = inflect.engine()

@predictions_bp.route("/api/predict", methods=["POST"])
def predict_property():
    """
    API: Predict Future Property Price & Loan Insights
    """
    try:
        data = request.json

        city = data.get("location")
        years = int(data.get("years", 5))

        if not city or not years:
            return jsonify({"error": "Missing required input"}), 400

        # Filter dataset by City
        match = real_estate_data[real_estate_data["City"] == city]

        if match.empty:
            return jsonify({"error": "City not found in dataset"}), 404

        # Use list price as current price
        current_price = float(match["ListPrice"].mean())

        # Predict future price (via appreciation model)
        predicted_price = predict_price(current_price, years)

        # Convert to words
        current_price_words = p.number_to_words(int(current_price)).capitalize()
        predicted_price_words = p.number_to_words(int(predicted_price)).capitalize()

        # Loan calculation on predicted price
        loan_info = calculate_loan(predicted_price, years)

        response = {
            "city": city,
            "current_price": f"₹{current_price:,.2f}",
            "current_price_words": current_price_words,
            "predicted_price": f"₹{predicted_price:,.2f}",
            "predicted_price_words": predicted_price_words,
            "investment_duration_years": years,
            "loan_info": loan_info
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
