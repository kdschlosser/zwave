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

from ..enums import explore_request_exclusion


class FUNC_ZW_EXPLORE_REQUEST_EXCLUSION_CMD(DATA_FRAME):
    """
    Explore Request Exclusion Command

    This command is used to initiate a Network-Wide Exclusion process. When the Z-Wave module receives
    this command, the module MUST issue an explore frame for requesting exclusion (remove) from a Z-
    Wave network.
    """
    id = 0x5F
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_EXPLORE_REQUEST_EXCLUSION_RSP(DATA_FRAME):
    id = 0x5F
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_exclusion_request_status', uint8_t)
    ]

    exclusion_request_statuses = explore_request_exclusion.response.exclusion_request_status

    @property
    def exclusion_request_status(self) -> exclusion_request_statuses:
        return self.exclusion_request_statuses(self._exclusion_request_status)
