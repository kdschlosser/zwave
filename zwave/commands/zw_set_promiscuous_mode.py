"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_SET_PROMISCUOUS_MODE_CMD(DATA_FRAME):
    """
    Enable / disable promiscuous mode

    A Controller in promiscuous mode will transfer payload from a promiscuously received application frame
    destined and originated from nodes residing in same network (HomeID). The promiscuously received
    application frame (only end destination frame) will be transferred to the application through
    ApplicationCommandHandler / ApplicationCommandHandler_Bridge with the
    RECEIVE_STATUS_FOREIGN_FRAME bit set in rxStatus.
    """
    id = 0xD0
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_state', uint8_t)]

    @property
    def packet_length(self):
        return 0

    @property
    def enabled(self) -> bool:
        return bool(self._state)

    @enabled.setter
    def enabled(self, value: bool):
        self._state = int(bool(value))  # NOQA
