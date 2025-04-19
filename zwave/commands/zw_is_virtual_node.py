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


class FUNC_ZW_IS_VIRTUAL_NODE_CMD(DATA_FRAME):
    """
    Is Virtual Node Command

    This command is used to check if a given NodeID is a virtual end node.
    """
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


class FUNC_ZW_IS_VIRTUAL_NODE_RSP(DATA_FRAME):
    id = 0xA6
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_characteristic', uint8_t)]

    @property
    def is_virtual_node(self) -> bool:
        return bool(self._characteristic)
