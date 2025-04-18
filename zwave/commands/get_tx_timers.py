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


class FUNC_GET_TX_TIMERS_CMD(DATA_FRAME):
    """
    Get Tx Timer Command

    This command is used to request the Z-Wave Module internal Tx timer. When the module receives this
    command, it MUST return the Tx timer for each channels
    """
    id = 0x38
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_GET_TX_TIMERS_RSP(DATA_FRAME):
    id = 0x38
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_tx_timer_ch0', uint8_t),
        ('_tx_timer_ch1', uint8_t),
        ('_tx_timer_ch2', uint8_t),
    ]

    @property
    def tx_timer_ch0(self):
        return self._tx_timer_ch0

    @property
    def tx_timer_ch1(self):
        return self._tx_timer_ch1

    @property
    def tx_timer_ch2(self):
        return self._tx_timer_ch2
