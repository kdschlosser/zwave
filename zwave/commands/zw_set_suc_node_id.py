from . import DATA_FRAME, FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import set_suc_node_id


class ZwSetSucNodeId(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 6)
    ]

    options = set_suc_node_id.command.option
    capabilities = set_suc_node_id.command.capability
    suc_states = set_suc_node_id.command.suc_state

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @node_id.setter
    def node_id(self, value):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value << 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def suc_state(self) -> suc_states:
        if self._node_id_len == 1:
            return self.suc_states(self._data[1])
        else:
            return self.suc_states(self._data[2])

    @suc_state.setter
    def suc_state(self, value: suc_states):
        if self._node_id_len == 1:
            self._data[1] = value.value  # NOQA
        else:
            self._data[2] = value.value  # NOQA

    @property
    def option(self) -> options:
        if self._node_id_len == 1:
            return self.options(self._data[2])
        else:
            return self.options(self._data[3])

    @option.setter
    def option(self, value: options):
        if self._node_id_len == 1:
            self._data[2] = value.value  # NOQA
        else:
            self._data[3] = value.value  # NOQA

    @property
    def capability(self) -> capabilities:
        if self._node_id_len == 1:
            return self.capabilities(self._data[3])
        else:
            return self.capabilities(self._data[4])

    @capability.setter
    def capability(self, value: capabilities):
        if self._node_id_len == 1:
            self._data[3] = value.value  # NOQA
        else:
            self._data[4] = value.value  # NOQA

    @property
    def session_id(self):
        if self._node_id_len == 1:
            return self._data[4]
        else:
            return self._data[5]

    @session_id.setter
    def session_id(self, value):
        if self._node_id_len == 1:
            self._data[1] = value  # NOQA
        else:
            self._data[2] = value  # NOQA


class ZwSetSucNodeIdResponse(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    @property
    def status(self):
        return self._status


class ZwSetSucNodeIdCallback(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = set_suc_node_id.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
