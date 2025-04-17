from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t,
    uint16_t
)

from ..enums import assign_return_route


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('dst_node_id', uint8_t),
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('dst_node_id', uint16_t),
        ('session_id', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_ASSIGN_RETURN_ROUTE_CMD(DATA_FRAME):
    """
    Assign a return route from the source node to the destination node
    """
    id = 0x46
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len * 2 + 1

    @property
    def src_node_id(self) -> int:
        return self._fields.node_id

    @src_node_id.setter
    def src_node_id(self, value: int):
        self._fields.node_id = value

    @property
    def dst_node_id(self) -> int:
        return self._fields.dst_node_id

    @dst_node_id.setter
    def dst_node_id(self, value: int):
        self._fields.dst_node_id = value

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class FUNC_ZW_ASSIGN_RETURN_ROUTE_RSP(DATA_FRAME):
    id = 0x46
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t)
    ]

    @property
    def status(self):
        return self._status


class FUNC_ZW_ASSIGN_RETURN_ROUTE_CB(DATA_FRAME):
    id = 0x46
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t)
    ]

    statuses = assign_return_route.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
