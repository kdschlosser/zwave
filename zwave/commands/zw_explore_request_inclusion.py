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

from ..enums import explore_request_inclusion


class FUNC_ZW_EXPLORE_REQUEST_INCLUSION_CMD(DATA_FRAME):
    """
    Explore Request Inclusion Command

    This command is used to initiate a Network-Wide Inclusion process. When the Z-Wave module receives this
    command, the module MUST issue an explore frame for requesting inclusion (add) to a Z-Wave
    network.
    """
    id = 0x5E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_EXPLORE_REQUEST_INCLUSION_RSP(DATA_FRAME):
    id = 0x5E
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_inclusion_request_status', uint8_t)
    ]

    inclusion_request_statuses = explore_request_inclusion.response.inclusion_request_status

    @property
    def inclusion_request_status(self) -> inclusion_request_statuses:
        return self.inclusion_request_statuses(self._inclusion_request_status)
