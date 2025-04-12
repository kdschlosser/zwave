from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwExploreRequestExclusion(HOST_COMMAND):
    id = 0x5F
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwExploreRequestExclusionResponse(HOST_RESPONSE):
    id = 0x5F

    _fields_ = [
        ('_exclusion_request_status', uint8_t)
    ]

    @property
    def exclusion_request_status(self) -> bool:
        return bool(self._exclusion_request_status)
