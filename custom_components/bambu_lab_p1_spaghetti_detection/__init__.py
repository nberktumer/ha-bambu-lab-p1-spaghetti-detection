import logging

import aiohttp
import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall, ServiceResponse, SupportsResponse

DOMAIN = "bambu_lab_p1_spaghetti_detection"
BRAND = "Bambu Lab P1 - Spaghetti Detection"

LOGGER = logging.getLogger(__package__)

PLATFORMS = [Platform.NUMBER, Platform.DATETIME]

SPAGHETTI_DETECTION_SCHEMA = vol.Schema({
    vol.Required("obico_host"): str,
    vol.Required("obico_auth_token"): str,
    vol.Required("image_url"): str,
})


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the Bambu Lab P1 - Spaghetti Detection integration."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def spaghetti_detection_handler(call: ServiceCall) -> ServiceResponse:
        """Handle the custom service."""
        obico_host = call.data.get("obico_host", "")
        obico_auth_token = call.data.get("obico_auth_token", "")
        image_url = call.data.get("image_url", "")

        if obico_host.endswith("/"):
            obico_host = obico_host[:-1]

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{obico_host}/p/?img={image_url}",
                                   headers={"Authorization": f"Bearer {obico_auth_token}"}) as response:
                result = await response.json()

        return {"result": result}

    hass.services.async_register(
        DOMAIN,
        "predict",
        spaghetti_detection_handler,
        schema=SPAGHETTI_DETECTION_SCHEMA,
        supports_response=SupportsResponse.ONLY
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Bambu Lab P1 - Spaghetti Detection integration."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
