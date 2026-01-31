"""Tests for the Compit water heater platform."""

# TODO: Implement when water heater device class is defined
# The following tests should be implemented once the water heater device class
# value is known from the Compit API (similar to CLIMATE_DEVICE_CLASS = 10):
#
# 1. Test water heater entities creation with snapshot
# 2. Test water heater temperature setting
# 3. Test water heater operation mode changes
# 4. Test water heater away mode
# 5. Test water heater state reporting
#
# Example test structure (to be uncommented and completed):
#
# from unittest.mock import MagicMock
# import pytest
# from syrupy.assertion import SnapshotAssertion
# from homeassistant.const import Platform
# from homeassistant.core import HomeAssistant
# from homeassistant.helpers import entity_registry as er
# from . import setup_integration, snapshot_compit_entities
# from tests.common import MockConfigEntry
#
# async def test_water_heater_entities_snapshot(
#     hass: HomeAssistant,
#     entity_registry: er.EntityRegistry,
#     mock_config_entry: MockConfigEntry,
#     mock_connector: MagicMock,
#     snapshot: SnapshotAssertion,
# ) -> None:
#     """Snapshot test for water heater entities creation."""
#     await setup_integration(hass, mock_config_entry)
#     snapshot_compit_entities(hass, entity_registry, snapshot, Platform.WATER_HEATER)
