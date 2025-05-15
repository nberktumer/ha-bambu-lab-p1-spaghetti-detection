from datetime import datetime, timezone

from homeassistant.components.datetime import DateTimeEntity, DateTimeEntityDescription

from .const import (
    DOMAIN,
    DEVICE_NAME,
    DEVICE_MANUFACTURER,
    DEVICE_MODEL,
    DEVICE_ENTRY_TYPE,
)

DATETIME_TYPES: tuple[DateTimeEntityDescription, ...] = (
    DateTimeEntityDescription(
        key="last_notify_time",
        name="Spaghetti Detection - Last Notify Time"
    ),
)


async def async_setup_entry(hass, entry, async_add_entities):
    entities = [
        BambuLabP1SpaghettiDetectionDateTimeEntity(entry.entry_id, entity_description)
        for entity_description in DATETIME_TYPES
    ]
    async_add_entities(entities)


class BambuLabP1SpaghettiDetectionDateTimeEntity(DateTimeEntity):
    def __init__(self, entry_id, entity_description):
        self.entity_description = entity_description
        self._entry_id = entry_id  # ✅ Set the entry_id

        self.entity_id = f"datetime.bambu_lab_p1_spaghetti_detection_{entity_description.key}"
        self._attr_unique_id = f"datetime.bambu_lab_p1_spaghetti_detection_{entity_description.key}"
        self._attr_native_value = datetime.fromtimestamp(0, timezone.utc)

    async def async_set_value(self, value: datetime) -> None:
        """Set the value of the datetime entity."""
        self._attr_native_value = value
        self.async_write_ha_state()

    async def set_value(self, value: datetime) -> None:
        """Set the value of the number entity."""
        self._attr_native_value = value
        self.async_write_ha_state()
   
    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": DEVICE_NAME,
            "manufacturer": DEVICE_MANUFACTURER,
            "model": DEVICE_MODEL,
            "entry_type": DEVICE_ENTRY_TYPE,
        }