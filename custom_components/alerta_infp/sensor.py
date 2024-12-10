from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL
from .helpers import fetch_earthquake_data
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the INFP alert sensor based on a config entry."""
    scan_interval = config_entry.options.get("scan_interval", DEFAULT_SCAN_INTERVAL)
    name = config_entry.title

    async_add_entities([INFPAlertSensor(hass, name, scan_interval, config_entry.entry_id)])


class INFPAlertSensor(SensorEntity):
    """A sensor that monitors earthquake alerts from INFP."""

    def __init__(self, hass, name, scan_interval, entry_id):
        self._hass = hass
        self._name = name
        self._state = None
        self._attributes = {}
        self._scan_interval = scan_interval
        self._entry_id = entry_id
        self._last_alert_id = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the current state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return additional attributes of the sensor."""
        return self._attributes

    async def async_update(self):
        """Fetch the latest data and update the sensor state."""
        _LOGGER.debug("Updating INFP Alert Sensor")
        try:
            data = await self._hass.async_add_executor_job(fetch_earthquake_data)
            if data:
                alert_id = data.get("id")
                # Avoid processing the same alert multiple times
                if alert_id and alert_id != self._last_alert_id:
                    self._last_alert_id = alert_id
                    self._state = data.get("magnitude", "N/A")
                    self._attributes = {
                        "location": data.get("location"),
                        "time": data.get("time"),
                        "depth": data.get("depth"),
                        "latitude": data.get("latitude"),
                        "longitude": data.get("longitude"),
                    }
                    _LOGGER.info(f"New earthquake detected: {data}")
                else:
                    _LOGGER.debug("No new alerts.")
            else:
                _LOGGER.warning("No data received from INFP.")
                self._state = "No Data"
                self._attributes = {}
        except Exception as e:
            _LOGGER.error(f"Error fetching data from INFP: {e}")
            self._state = "Error"
