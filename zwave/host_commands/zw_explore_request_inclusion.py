from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwExploreRequestInclusion(HOST_COMMAND):
    id = 0x5E
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwExploreRequestInclusionResponse(HOST_RESPONSE):
    id = 0x5E

    _fields_ = [
        ('_inclusion_request_status', uint8_t)
    ]

    @property
    def inclusion_request_status(self) -> bool:
        return bool(self._inclusion_request_status)
