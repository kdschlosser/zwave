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
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_IS_FAILED_NODE_ID_CMD(DATA_FRAME):
    """
    Is Node Failed Command

    This command is used to request if a given NodeID is considered as failed by the Z-Wave API Module.
    """
    id = 0x62
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value


class FUNC_ZW_IS_FAILED_NODE_ID_RSP(DATA_FRAME):
    id = 0x62
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_is_failed', uint8_t)]

    @property
    def is_failed(self) -> bool:
        return bool(self._is_failed)
