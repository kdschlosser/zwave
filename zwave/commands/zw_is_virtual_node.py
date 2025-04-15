from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t


class ZwIsVirtualNode(DATA_FRAME):
    id = 0xA6
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_node_id', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA


class ZwIsVirtualNodeResponse(DATA_FRAME):
    id = 0xA6
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_characteristic', uint8_t)]

    @property
    def is_virtual_node(self) -> bool:
        return bool(self._characteristic)
