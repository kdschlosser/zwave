from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import get_protocol_status


class ZwGetProtocolStatus(DATA_FRAME):
    id = 0xBF
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class ZwGetProtocolStatusResponse(DATA_FRAME):
    id = 0xBF
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    statuses = get_protocol_status.response.status

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
