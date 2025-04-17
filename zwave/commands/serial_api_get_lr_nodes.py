"""
Serial API Host Appl. Prg. Guide
INS12350
2022-12-01
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_SERIAL_API_GET_LR_NODES_CMD(DATA_FRAME):
    """
    Used after GetSerialApiInitData to get the nodes with IDs > 0xFF
    """
    id = 0xDA
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_offset', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self.offset = value


class FUNC_SERIAL_API_GET_LR_NODES_RSP(DATA_FRAME):
    id = 0xDA
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

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
                request = FUNC_SERIAL_API_GET_LR_NODES_CMD(self._serial)
                request.offset = offset + 1
                response = request.send_wait()

                offset = response.offset
                more_nodes = response.more_nodes
                res.extend(response.node_list)

        return res
