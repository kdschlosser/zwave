from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class SerialApiGetLRNodes(HOST_COMMAND):
    id = 0xDA
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_offset', uint8_t)]

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self.offset = value


class SerialApiGetLRNodesResponse(HOST_RESPONSE):
    id = 0xDA

    _fields_ = [
        ('_more_nodes', uint8_t),
        ('_offset', uint8_t),
        ('_node_list_len', uint8_t),
        ('_node_list', uint8_t * 128)
    ]

    @property
    def more_nodes(self):
        return bool(self._more_nodes)

    @property
    def offset(self):
        return self._offset

    @property
    def node_list_len(self):
        return self._node_list_len

    @property
    def node_list(self):
        more_nodes = self.more_nodes
        offset = self.offset
        node_list_len = self.node_list_len
        res = []

        start_node_id = 255 + (128 * 8 * offset)

        for i in range(node_list_len):
            for bit in range(8):
                if self._node_list[i] & (1 << bit):
                    res.append(start_node_id + (8 * i) + bit)

        if offset == 0:
            while more_nodes:
                request = SerialApiGetLRNodes(self._serial)
                request.offset = offset + 1
                response = request.send_wait()

                offset = response.offset
                more_nodes = response.more_nodes
                res.extend(response.node_list)

        return res
