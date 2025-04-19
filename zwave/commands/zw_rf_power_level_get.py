"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import rf_power_level_get


class FUNC_ZW_RF_POWER_LEVEL_GET_CMD(DATA_FRAME):
    """
    Get the current power level used in RF transmitting.
    """
    id = 0xBA
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_RF_POWER_LEVEL_GET_RSP(DATA_FRAME):
    id = 0xBA
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    power_levels = rf_power_level_get.response.power_level

    @property
    def power_level(self) -> power_levels:
        return self.power_levels(self._power_level)
