import requests
from .const import DEFAULT_TIMEOUT
import logging

_LOGGER = logging.getLogger(__name__)

INFP_URL = "https://www.infp.ro"

def fetch_earthquake_data():
    """Fetch earthquake data from INFP."""
    try:
        _LOGGER.debug("Fetching earthquake data from INFP.")
        response = requests.get(INFP_URL, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        html_content = response.text
        _LOGGER.debug(f"Raw HTML fetched: {html_content[:500]}")  # Log the first 500 characters for context
        data = parse_earthquake_data(html_content)
        _LOGGER.debug(f"Parsed data: {data}")
        return data
    except Exception as e:
        _LOGGER.error(f"Error fetching data from INFP: {e}")
        return []

def parse_earthquake_data(html):
    """Parse the HTML response for earthquake data."""
    # Implement real parsing logic here.
    # For now, return dummy data for testing purposes.
    _LOGGER.debug("Parsing earthquake data.")
    return [
        {"id": "1", "magnitude": 4.5, "location": "București", "time": "2024-12-10 12:00"},
        {"id": "2", "magnitude": 5.0, "location": "Iași", "time": "2024-12-10 12:05"},
    ]
