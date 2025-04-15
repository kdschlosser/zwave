from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwSetRoutingMax(DATA_FRAME):
    id = 0xD4
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_max_retries', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def max_retries(self) -> int:
        return self._max_retries

    @max_retries.setter
    def max_retries(self, value: int):
        self._max_retries = value  # NOQA


class ZwSetRoutingMaxResponse(DATA_FRAME):
    id = 0xD4
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status
