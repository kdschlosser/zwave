"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
)


class FUNC_ZW_WATCHDOG_KICK_CMD(DATA_FRAME):
    """
     Kick Watchdog (500 series and older)
    """
    id = 0xB8
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
