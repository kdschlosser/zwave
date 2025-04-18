from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t,
    uint32_t
)

from ..enums import get_priority_route


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_GET_PRIORITY_ROUTE_CMD(DATA_FRAME):
    """
    Get the route that is used as the first routing attempty when transmitting to a node
    """
    id = 0x92
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


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('repeater', uint32_t),
        ('route_speed', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('repeater', uint32_t),
        ('route_speed', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_GET_PRIORITY_ROUTE_RSP(DATA_FRAME):
    id = 0x92
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    route_speeds = get_priority_route.response.route_speed

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def repeater(self) -> int:
        return self._fields.repeater

    @repeater.setter
    def repeater(self, value: int):
        self._fields.repeater = value

    @property
    def route_speed(self) -> route_speeds:
        return self.route_speeds(self._fields.route_speed)

    @route_speed.setter
    def route_speed(self, value: route_speeds):
        self._fields.route_speed = value.value
