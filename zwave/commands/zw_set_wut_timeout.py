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


class FUNC_ZW_SET_WUT_TIMEOUT_CMD(DATA_FRAME):
    """
    Set Wake up timer interval
    """
    id = 0xB4
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_timeout', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def timeout(self) -> int:
        """
        in seconds, max is 255
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value: int):
        self._timeout = value  # NOQA
