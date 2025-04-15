from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwRequestNodeInfo(DATA_FRAME):
    id = 0x60
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_node_id', uint8_t * 2)]

    @property
    def packet_length(self):
        return 0

    @property
    def destination_node_id(self):
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]

    @destination_node_id.setter
    def destination_node_id(self, value):
        if self._node_id_len == 1:
            self._node_id[0] = value
        else:
            self._node_id[0] = (value >> 8) & 0xFF
            self._node_id[1] = value & 0xFF


class ZwRequestNodeInfoResponse(DATA_FRAME):
    id = 0x60
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self):
        return self._command_status

