import requests
from .const import DEFAULT_TIMEOUT

INFP_URL = "https://www.infp.ro"

def fetch_earthquake_data():
    """Fetch earthquake data from INFP."""
    try:
        response = requests.get(INFP_URL, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        # Parse multiple alerts
        return parse_earthquake_data(response.text)
    except Exception as e:
        return []

def parse_earthquake_data(html):
    """Parse the HTML response for earthquake data."""
    # Implement logic to parse and return multiple alerts
    return [
        {"id": "1", "magnitude": 4.5, "location": "București", "time": "2024-12-10 12:00"},
        {"id": "2", "magnitude": 5.0, "location": "Iași", "time": "2024-12-10 12:05"},
    ]
