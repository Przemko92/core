"""Support for water heater devices."""

from enum import StrEnum

DOMAIN = "water_heater"

STATE_ECO = "eco"
STATE_ELECTRIC = "electric"
STATE_PERFORMANCE = "performance"
STATE_HIGH_DEMAND = "high_demand"
STATE_HEAT_PUMP = "heat_pump"
STATE_GAS = "gas"


class WaterHeaterDeviceClass(StrEnum):
    """Device class for water heaters."""

    WATER_HEATER = "water_heater"
    """Generic water heater device."""
