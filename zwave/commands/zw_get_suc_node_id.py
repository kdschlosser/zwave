from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS
)


class FUNC_ZW_GET_SUC_NODE_ID_CMD(DATA_FRAME):
    """
    Try to retrieve a Static Update Controller node id (zero if no SUC present)
    """
    id = 0x56
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_GET_SUC_NODE_ID_RSP(DATA_FRAME):
    id = 0x56
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def node_id(self) -> int:
        return self._fields.node_id
