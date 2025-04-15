from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwSetDefault(DATA_FRAME):
    id = 0x42
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class ZwSetDefaultCallback(DATA_FRAME):
    id = 0x42
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def session_id(self) -> int:
        return self._session_id
