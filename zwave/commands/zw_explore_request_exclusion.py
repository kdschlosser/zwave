from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwExploreRequestExclusion(DATA_FRAME):
    id = 0x5F
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class ZwExploreRequestExclusionResponse(DATA_FRAME):
    id = 0x5F
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_exclusion_request_status', uint8_t)
    ]

    @property
    def exclusion_request_status(self) -> bool:
        return bool(self._exclusion_request_status)
