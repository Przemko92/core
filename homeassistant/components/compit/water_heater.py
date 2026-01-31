"""Water heater platform for Compit integration."""

import logging

from homeassistant.components.water_heater import WaterHeaterDeviceClass, WaterHeaterEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import DOMAIN
from .coordinator import CompitConfigEntry

# TODO: Define the actual water heater device class value when available from the Compit API
# Similar to CLIMATE_DEVICE_CLASS = 10 in climate.py
# WATER_HEATER_DEVICE_CLASS = ???

_LOGGER: logging.Logger = logging.getLogger(__name__)
PARALLEL_UPDATES = 0


async def async_setup_entry(
    hass: HomeAssistant,
    entry: CompitConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Compit water heater platform from a config entry."""
    # TODO: Implement when water heater device class is defined in the Compit API
    # coordinator = entry.runtime_data
    # water_heater_entities = []
    # for device_id in coordinator.connector.all_devices:
    #     device = coordinator.connector.all_devices[device_id]
    #     if device.definition.device_class == WATER_HEATER_DEVICE_CLASS:
    #         water_heater_entities.append(
    #             CompitWaterHeater(coordinator, device_id, device.definition.name)
    #         )
    # async_add_entities(water_heater_entities)
    _LOGGER.debug("Water heater platform not yet implemented - awaiting device class definition")
