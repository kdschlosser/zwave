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


class FUNC_ZW_SET_ROUTING_MAX_CMD(DATA_FRAME):
    """
    Set Maximum Routing Attempts Command

    This command is used to set the maximum number of source routing attempts based on the routing table
    lookups, and this shall be used before the Z-Wave protocol layer starts the dynamic route resolution.
    """
    id = 0xD4
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_max_retries', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def max_retries(self) -> int:
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value: int):
        self._max_retries = value  # NOQA


class FUNC_ZW_SET_ROUTING_MAX_RSP(DATA_FRAME):
    id = 0xD4
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status
