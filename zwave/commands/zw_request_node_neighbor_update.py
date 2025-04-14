from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import request_node_neighbor_update


class ZwRequestNodeNeighborUpdate(DATA_FRAME):
    id = 0x48
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 6)
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

    @session_id.setter
    def session_id(self, value):
        if self._node_id_len == 1:
            self._data[1] = value  # NOQA
        else:
            self._data[2] = value  # NOQA


class ZwRequestNodeNeighborUpdateCallback(DATA_FRAME):
    id = 0x48
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = request_node_neighbor_update.callback.neighbor_discovery

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)


