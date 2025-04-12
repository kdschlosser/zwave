from . import HOST_COMMAND, HOST_RESPONSE, HOST_CALLBACK, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums.host import suc_return_route


class ZwAssignSucReturnRoute(HOST_COMMAND):
    id = 0x51
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE | FRAME_TYPE_CALLBACK

    _fields_ = [
        ('_data', uint8_t * 3)
    ]

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
    def session_id(self):
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return self._data[2]


class ZwAssignSucReturnRouteResponse(HOST_RESPONSE):
    id = 0x51

    _fields_ = [
        ('_status', uint8_t)
    ]

    @property
    def status(self):
        return self._status


class ZwAssignSucReturnRouteCallback(HOST_CALLBACK):
    id = 0x51

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t)
    ]

    statuses = suc_return_route.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)


