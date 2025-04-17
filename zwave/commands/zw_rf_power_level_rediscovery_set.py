from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwRfPowerLevelRediscoverySet(DATA_FRAME):
    """
    ???
    """
    # TODO: enum values
    id = 0x1E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def power_level(self) -> int:
        return self._power_level

    @power_level.setter
    def power_level(self, value: int):
        self._power_level = value  # NOQA
