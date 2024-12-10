import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, DEFAULT_TIMEOUT


class INFPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Alerta INFP."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="INFP Alerts", data=user_input)

        # Define the configuration schema
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("scan_interval", default=DEFAULT_SCAN_INTERVAL): vol.All(int, vol.Range(min=10)),
                vol.Optional("timeout", default=DEFAULT_TIMEOUT): vol.All(int, vol.Range(min=5, max=60)),
            }),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return INFPEntityOptionsFlow()


class INFPEntityOptionsFlow(config_entries.OptionsFlow):
    """Handle options for INFP integration options."""

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Get the current options from the config entry
        options = self.config_entry.options
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("scan_interval", default=options.get("scan_interval", DEFAULT_SCAN_INTERVAL)): vol.All(int, vol.Range(min=10)),
                vol.Optional("timeout", default=options.get("timeout", DEFAULT_TIMEOUT)): vol.All(int, vol.Range(min=5, max=60)),
            }),
        )
