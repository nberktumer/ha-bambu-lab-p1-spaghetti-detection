from homeassistant.components.number import NumberEntity, NumberEntityDescription

NUMBER_TYPES: tuple[NumberEntityDescription, ...] = (
    NumberEntityDescription(
        key="current_frame_number",
        name="Current Frame Number",
        native_min_value=0,
        native_max_value=10000000000000000
    ),
    NumberEntityDescription(
        key="lifetime_frame_number",
        name="Lifetime Frame Number",
        native_min_value=0,
        native_max_value=10000000000000000
    ),
    NumberEntityDescription(
        key="ewm_mean",
        name="EWM Mean",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="adjusted_ewm_mean",
        name="Adjusted EWM Mean",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="p",
        name="P",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="normalized_p",
        name="Normalized P",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="p_sum",
        name="P Sum",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="rolling_mean_diff",
        name="Rolling Mean Diff",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="rolling_mean_long",
        name="Rolling Mean Long",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="rolling_mean_short",
        name="Rolling Mean Short",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="thresh_warning",
        name="Thresh Warning",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
    NumberEntityDescription(
        key="thresh_failure",
        name="Thresh Failure",
        native_min_value=-1000000000000000,
        native_max_value=10000000000000000,
        native_step=0.000000001
    ),
)


async def async_setup_entry(hass, entry, async_add_entities):
    entities = [
        BambuLabP1SpaghettiDetectionNumberEntity(entity_description) for entity_description in NUMBER_TYPES
    ]

    async_add_entities(entities)


class BambuLabP1SpaghettiDetectionNumberEntity(NumberEntity):
    def __init__(self, entity_description):
        entity_description.name = "Spaghetti Detection - %s" % entity_description.name
        self.entity_description = entity_description

        self.entity_id = "number.bambu_lab_p1_spaghetti_detection_%s" % entity_description.key
        self._attr_unique_id = "number.bambu_lab_p1_spaghetti_detection_%s" % entity_description.key
        if self._attr_native_value is None:
            self._attr_native_value = 0

    async def async_set_native_value(self, value: float) -> None:
        """Set the value of the number entity."""
        self._attr_native_value = value
        self.async_write_ha_state()
