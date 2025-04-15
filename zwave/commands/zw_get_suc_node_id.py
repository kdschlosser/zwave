from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS
)


class ZwGetSucNodeId(DATA_FRAME):
    id = 0x56
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class _ZwGetSucNodeIdResponseFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class ZwGetSucNodeIdResponse(DATA_FRAME):
    id = 0x56
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _ZwGetSucNodeIdResponseFields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def node_id(self) -> int:
        return self._fields.node_id
