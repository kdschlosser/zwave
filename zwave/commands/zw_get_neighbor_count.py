"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


class FUNC_ZW_GET_NEIGHBOR_COUNT_CMD(DATA_FRAME):
    """
    ???
    """
    id = 0xBB
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ =[('_node_id', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA


class FUNC_ZW_GET_NEIGHBOR_COUNT_RSP(DATA_FRAME):
    id = 0xBB
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_count', uint8_t)]

    @property
    def count(self) -> int:
        return self._count
