from . import DATA_FRAME, FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import set_slave_learn_mode


class ZwSetSlaveLearnMode(DATA_FRAME):
    id = 0xA4
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 6)
    ]

    modes = set_slave_learn_mode.command.mode

    @property
    def node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @node_id.setter
    def node_id(self, value: int):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value << 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def mode(self) -> modes:
        if self._node_id_len == 1:
            return self.modes(self._data[1])
        else:
            return self.modes(self._data[2])

    @mode.setter
    def mode(self, value: modes):
        if self._node_id_len == 1:
            self._data[1] = value.value  # NOQA
        else:
            self._data[2] = value.value  # NOQA

    @property
    def session_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[2]
        else:
            return self._data[3]

    @session_id.setter
    def session_id(self, value: int):
        if self._node_id_len == 1:
            self._data[2] = value  # NOQA
        else:
            self._data[3] = value  # NOQA


class ZwSetSlaveLearnModeResponse(DATA_FRAME):
    id = 0xA4
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    @property
    def status(self):
        return self._status


class ZwSetSlaveLearnModeCallback(DATA_FRAME):
    id = 0xA4
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
        ('_original_node_id', uint8_t),
        ('_new_node_id', uint8_t),
    ]

    statuses = set_slave_learn_mode.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def original_node_id(self) -> int:
        return self._original_node_id

    @property
    def new_node_id(self) -> int:
        return self._new_node_id
