"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_SEND_DATA_ABORT_CMD(DATA_FRAME):
    """
    Send Data Abort Command

    This command is used to instruct the Z-Wave Module to abort an ongoing transmission started with any
    of the following commands:

        • Bridge Controller Node Send Data Command
        • Bridge Controller Node Send Data Multicast Command
        • End Node Send Data Command
        • End Node Send Data Multicast Command
        • Controller Node Send Data Command
        • Controller Node Send Data Multicast Command
        • Send NOP Command
    """
    id = 0x16
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
