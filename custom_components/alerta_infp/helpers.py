import requests
from .const import DEFAULT_TIMEOUT

INFP_URL = "https://www.infp.ro"

def fetch_earthquake_data():
    """Fetch earthquake data from INFP."""
    try:
        response = requests.get(INFP_URL, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        # Example parsing logic
        data = parse_earthquake_data(response.text)
        return data
    except Exception as e:
        return None

def parse_earthquake_data(html):
    """Parse the HTML response for earthquake data."""
    # Implement scraping logic here
    return {"magnitude": 4.5, "location": "București", "time": "2024-12-10 12:00"}
