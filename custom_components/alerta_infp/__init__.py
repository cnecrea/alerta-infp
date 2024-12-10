from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import logging

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration via YAML (deprecated)."""
    _LOGGER.debug("Setting up Alerta INFP integration via YAML.")
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the integration via Config Flow."""
    _LOGGER.debug("Setting up Alerta INFP entry.")
    hass.data.setdefault(DOMAIN, {})
    try:
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
        _LOGGER.info("Successfully set up Alerta INFP integration.")
        return True
    except Exception as e:
        _LOGGER.error(f"Error setting up Alerta INFP: {e}")
        return False

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the integration."""
    _LOGGER.debug("Unloading Alerta INFP entry.")
    try:
        unload_success = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
        if unload_success:
            hass.data[DOMAIN].pop(entry.entry_id, None)
            _LOGGER.info("Successfully unloaded Alerta INFP integration.")
            return True
        _LOGGER.warning("Failed to unload Alerta INFP integration.")
        return False
    except Exception as e:
        _LOGGER.error(f"Error unloading Alerta INFP: {e}")
        return False
