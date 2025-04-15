from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwExploreRequestInclusion(DATA_FRAME):
    id = 0x5E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class ZwExploreRequestInclusionResponse(DATA_FRAME):
    id = 0x5E
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_inclusion_request_status', uint8_t)
    ]

    @property
    def inclusion_request_status(self) -> bool:
        return bool(self._inclusion_request_status)
