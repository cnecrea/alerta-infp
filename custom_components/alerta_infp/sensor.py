from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL
from .helpers import fetch_earthquake_data
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the INFP alert sensors based on a config entry."""
    try:
        data = await hass.async_add_executor_job(fetch_earthquake_data)
        if data:
            sensors = [
                INFPAlertSensor(hass, f"Alert {alert['id']}", alert, config_entry.entry_id)
                for alert in data
            ]
            async_add_entities(sensors)
        else:
            _LOGGER.warning("No earthquake data available.")
    except Exception as e:
        _LOGGER.error(f"Failed to set up sensors: {e}")

class INFPAlertSensor(SensorEntity):
    """A sensor that monitors a specific earthquake alert from INFP."""

    def __init__(self, hass, name, alert, entry_id):
        self._hass = hass
        self._name = name
        self._state = alert.get("magnitude", "N/A")
        self._attributes = {
            "location": alert.get("location"),
            "time": alert.get("time"),
            "depth": alert.get("depth", "Unknown"),
            "latitude": alert.get("latitude", "Unknown"),
            "longitude": alert.get("longitude", "Unknown"),
        }
        self._entry_id = entry_id
        self._alert_id = alert.get("id")

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

    @property
    def device_info(self):
        """Return device information for linking entities."""
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": "INFP Alerts",
            "manufacturer": "INFP",
            "model": "Earthquake Alert System",
            "entry_type": "service",
        }

    async def async_update(self):
        """Update the sensor state."""
        _LOGGER.debug(f"Updating sensor {self._name}")
        try:
            data = await self._hass.async_add_executor_job(fetch_earthquake_data)
            for alert in data:
                if alert.get("id") == self._alert_id:
                    self._state = alert.get("magnitude", "N/A")
                    self._attributes.update({
                        "location": alert.get("location"),
                        "time": alert.get("time"),
                        "depth": alert.get("depth", "Unknown"),
                        "latitude": alert.get("latitude", "Unknown"),
                        "longitude": alert.get("longitude", "Unknown"),
                    })
                    _LOGGER.info(f"Updated sensor {self._name} with new data.")
                    break
        except Exception as e:
            _LOGGER.error(f"Failed to update sensor {self._name}: {e}")
