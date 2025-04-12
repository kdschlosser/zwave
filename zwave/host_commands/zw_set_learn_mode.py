from . import HOST_COMMAND, HOST_RESPONSE, HOST_CALLBACK, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums.host import set_learn_mode


class ZwSetLearnMode(HOST_COMMAND):
    id = 0x50
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE | FRAME_TYPE_CALLBACK

    _fields_ = [
        ('_learn_mode', uint8_t),
        ('_session_id', uint8_t)
    ]

    learn_modes = set_learn_mode.command.learn_mode

    @property
    def learn_mode(self) -> learn_modes:
        return self.learn_modes(self._learn_mode)

    @learn_mode.setter
    def learn_mode(self, value: learn_modes):
        self._learn_mode = value.value  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class ZwSetLearnModeResponse(HOST_RESPONSE):
    id = 0x60
    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class ZwSetLearnModeCallback(HOST_CALLBACK):
    id = 0x60
    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t),
        ('_node_id', uint8_t * 2)
    ]

    statuses = set_learn_mode.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._learn_mode_status)

    @property
    def node_id(self) -> int:
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]





