"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_WATCHDOG_ENABLE_CMD(DATA_FRAME):
    """
    Enable Watchdog (500 series and older)
    """
    id = 0xB6
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
