from . import HOST_COMMAND, HOST_CALLBACK, FRAME_TYPE_ACK, FRAME_TYPE_CALLBACK, uint8_t


class ZwSetDefault(HOST_COMMAND):
    id = 0x42
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_CALLBACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class ZwSetDefaultCallback(HOST_CALLBACK):
    id = 0x42

    _fields_ = [('_session_id', uint8_t)]

    @property
    def session_id(self) -> int:
        return self._session_id




FRAME_TYPE_NOACK = 0x00
FRAME_TYPE_ACK = 0x01
FRAME_TYPE_RESPONSE = 0x02
FRAME_TYPE_CALLBACK = 0x04
FRAME_TYPE_UNSOLICITED = 0x08

