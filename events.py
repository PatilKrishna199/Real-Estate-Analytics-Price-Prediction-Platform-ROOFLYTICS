from flask import Blueprint, jsonify

events = Blueprint('events', __name__)

upcoming_events = [
    {"title": "Real Estate Market Trends 2025", "date": "April 25, 2025", "time": "6 PM IST"},
    {"title": "Smart Investing with AI", "date": "May 10, 2025", "time": "5 PM IST"},
    {"title": "Risk-Free Property Investment Hacks", "date": "May 20, 2025", "time": "7 PM IST"}
]

@events.route('/api/events', methods=['GET'])
def get_events():
    """Fetch upcoming webinars & investment events."""
    return jsonify(upcoming_events)
