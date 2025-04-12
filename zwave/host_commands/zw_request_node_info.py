from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwRequestNodeInfo(HOST_COMMAND):
    id = 0x60
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_node_id', uint8_t * 2)]

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


class ZwRequestNodeInfoResponse(HOST_RESPONSE):
    id = 0x60
    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self):
        return self._command_status

