"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import rf_power_level_set


class FUNC_ZW_RF_POWER_LEVEL_SET_CMD(DATA_FRAME):
    """
    Set RF Power Level Command

    This command is used to set the power level used for RF transmission
    """

    id = 0x17
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    power_levels = rf_power_level_set.command.power_level

    @property
    def packet_length(self):
        return 1

    @property
    def power_level(self) -> power_levels:
        return self.power_levels(self._power_level)

    @power_level.setter
    def power_level(self, value: power_levels):
        self._power_level = value.value  # NOQA


class FUNC_ZW_R_F_POWER_LEVEL_SET_RSP(DATA_FRAME):
    id = 0x17
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    power_levels = rf_power_level_set.response.power_level

    @property
    def power_level(self) -> power_levels:
        return self.power_levels(self._power_level)
