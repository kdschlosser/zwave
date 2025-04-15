from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t


class ZwGetVirtualNodes(DATA_FRAME):
    id = 0xA5
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class ZwGetVirtualNodesResponse(DATA_FRAME):
    # TODO: docs don't make any sense

    id = 0xA5
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_node_mask', uint8_t)]

    @property
    def node_mask(self):
        return self._node_mask

