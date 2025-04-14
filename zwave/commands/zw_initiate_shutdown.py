from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_ACK, uint8_t


class ZwInitiateShutdown(DATA_FRAME):
    id = 0xD9
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class ZwInitiateShutdownResponse(DATA_FRAME):
    id = 0xD9
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def status(self) -> int:
        return self._status


