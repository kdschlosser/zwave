from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class MemoryGetId(DATA_FRAME):
    id = 0x20
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class MemoryGetIdResponse(DATA_FRAME):
    id = 0x20
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_home_id1', uint8_t),
        ('_home_id2', uint8_t),
        ('_home_id3', uint8_t),
        ('_home_id4', uint8_t),
        ('_node_id', uint8_t * 2),
    ]

    @property
    def home_id(self):
        return (
            (self._home_id1 << 24) |
            (self._home_id2 << 16) |
            (self._home_id3 << 8) |
            self._home_id4
        )

    @property
    def node_id(self) -> int:
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]
