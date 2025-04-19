"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_GET_VIRTUAL_NODES_CMD(DATA_FRAME):
    """
    Get Virtual Nodes Command

    This command is used to request available Virtual End Nodes in a Z-Wave Network.
    """
    id = 0xA5
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_VIRTUAL_NODES_RSP(DATA_FRAME):

    id = 0xA5
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_node_mask', uint8_t * 256)]

    @property
    def virtual_nodes(self) -> list[int]:
        res = []

        for i in range(256):
            node_mask = self._node_mask[i]
            if node_mask == 0x00:
                continue

            for j in range(8):
                res.append((j * 8) + i + 1)

        return res
