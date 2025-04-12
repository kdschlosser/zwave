from . import HOST_COMMAND, HOST_RESPONSE, HOST_CALLBACK, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums.host import send_suc_node_id


class ZwSendSucNodeId(HOST_COMMAND):
    id = 0x57
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE | FRAME_TYPE_CALLBACK

    _fields_ = [
        ('_data', uint8_t * 6)
    ]

    options = send_suc_node_id.command.option

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
    def option(self) -> options:
        if self._node_id_len == 1:
            return self.options(self._data[1])
        else:
            return self.options(self._data[2])

    @option.setter
    def option(self, value: options):
        if self._node_id_len == 1:
            self._data[1] = value.value  # NOQA
        else:
            self._data[2] = value.value  # NOQA

    @property
    def session_id(self):
        if self._node_id_len == 1:
            return self._data[2]
        else:
            return self._data[3]

    @session_id.setter
    def session_id(self, value):
        if self._node_id_len == 1:
            self._data[2] = value  # NOQA
        else:
            self._data[3] = value  # NOQA


class ZwSendSucNodeIdResponse(HOST_RESPONSE):
    id = 0x57

    _fields_ = [
        ('_status', uint8_t),
    ]

    @property
    def status(self):
        return self._status


class ZwSendSucNodeIdCallback(HOST_CALLBACK):
    id = 0x57

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = send_suc_node_id.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
