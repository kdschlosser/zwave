from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwRfPowerLevelSet(DATA_FRAME):
    # TODO: Values for power level enum

    id = 0x17
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        self._power_level = value  # NOQA


class ZwRfPowerLevelSetResponse(DATA_FRAME):
    id = 0x17
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    @property
    def power_level(self):
        return self._power_level
