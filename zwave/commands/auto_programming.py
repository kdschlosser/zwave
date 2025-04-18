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


class FUNC_AUTO_PROGRAMMING_CMD(DATA_FRAME):
    """
    This function enables the Auto Program Mode and resets the 500 Series Z-Wave SOC after 7.8ms..
    Leave Serial API and enter bootloader (700+ series only).
    """
    id = 0x27
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
