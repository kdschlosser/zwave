from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwIsFailedNodeId(HOST_COMMAND):
    id = 0x62
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_node_id', uint8_t * 2)]

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]

    @node_id.setter
    def node_id(self, value):
        if self._node_id_len == 1:
            self._node_id[0] = value
        else:
            self._node_id[0] = (value << 8) & 0xFF
            self._node_id[1] = value & 0xFF


class ZwIsFailedNodeIdResponse(HOST_RESPONSE):
    id = 0x62

    _fields_ = [('_is_faield', uint8_t)]

    @property
    def is_failed(self) -> bool:
        return bool(self._is_failed)
