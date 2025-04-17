"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class ZwAreNodesNeighbors(DATA_FRAME):
    """
    Used to check if two nodes are marked as being within direct range of each other
    """
    id = 0xBC
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id1', uint8_t),
        ('_node_id2', uint8_t)
    ]

    @property
    def packet_length(self):
        return 2

    @property
    def node_id1(self) -> int:
        return self._node_id1

    @node_id1.setter
    def node_id1(self, value: int):
        self._node_id1 = value  # NOQA

    @property
    def node_id2(self) -> int:
        return self._node_id2

    @node_id2.setter
    def node_id2(self, value: int):
        self._node_id2 = value  # NOQA


class ZwAreNodesNeighborsResponse(DATA_FRAME):
    id = 0xBC
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response', uint8_t),
    ]

    @property
    def response(self) -> int:
        return self._response
