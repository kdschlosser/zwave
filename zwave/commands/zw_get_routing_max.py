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


class FUNC_ZW_GET_ROUTING_MAX_CMD(DATA_FRAME):
    """
    Get the maximum number of source routing attempts based on the routing table
    lookups, and this shall be used before the Z-Wave protocol layer starts the dynamic route resolution.
    """
    id = 0xD5
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_ROUTING_MAX_RSP(DATA_FRAME):
    id = 0xD5
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_max_routing_retries', uint8_t)]

    @property
    def max_routing_retries(self) -> int:
        return self._max_routing_retries
