from flask import Blueprint, request, jsonify

investments_bp = Blueprint("investments", __name__)

# Mock investment listings (Major Indian Cities)
investment_list = [
    {
        "id": 1,
        "name": "Luxury Apartments",
        "city": "Pune",
        "price": 7500000,
        "roi": 8.5,
        "type": "Residential"
    },
    {
        "id": 2,
        "name": "Commercial Business Park",
        "city": "Bangalore",
        "price": 12000000,
        "roi": 10.0,
        "type": "Commercial"
    },
    {
        "id": 3,
        "name": "Mixed-Use Smart Complex",
        "city": "Mumbai",
        "price": 9500000,
        "roi": 9.2,
        "type": "Mixed-Use"
    },
    {
        "id": 4,
        "name": "IT SEZ Campus",
        "city": "Hyderabad",
        "price": 18000000,
        "roi": 11.0,
        "type": "Commercial"
    }
]

# GET: Fetch all investment opportunities
@investments_bp.route("/api/investments", methods=["GET"])
def get_investments():
    return jsonify(investment_list)

# POST: Record investor interest
@investments_bp.route("/api/invest", methods=["POST"])
def submit_investment():
    data = request.json
    print("📩 New Investment Interest:", data)
    return jsonify({"message": "Investment interest recorded successfully!"}), 200
