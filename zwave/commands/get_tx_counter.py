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


class FUNC_GET_TX_COUNTER_CMD(DATA_FRAME):
    """
    Get the number of transmits that the protocol has done since last reset of the counter.

    If the number returned is 255 then the number of transmits ≥ 255. The counter
    should be reset by the application, when it is to be restarted.
    """
    id = 0x81
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_GET_TX_COUNTER_RSP(DATA_FRAME):
    id = 0x81
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_counter', uint8_t)]

    @property
    def counter(self) -> int:
        return self._counter
