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


class FUNC_ZW_CLEAR_NETWORK_STATS_CMD(DATA_FRAME):
    """
    Clear Network Statistics Command

    This command is used to clear the current Network Statistics collected by the Z-Wave API Module.
    """
    id = 0x39
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_CLEAR_NETWORK_STATS_RSP(DATA_FRAME):
    id = 0x39
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self):
        return self._command_status
