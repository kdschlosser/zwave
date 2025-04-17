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

from ..enums import get_protocol_status


class FUNC_ZW_GET_PROTOCOL_STATUS_CMD(DATA_FRAME):
    """
    Request the current status of the protocol running on the Z-Wave module
    """
    id = 0xBF
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_PROTOCOL_STATUS_RSP(DATA_FRAME):
    id = 0xBF
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    statuses = get_protocol_status.response.status

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
