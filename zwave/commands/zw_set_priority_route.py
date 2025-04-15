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
from ..enums import set_priority_route


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


class _ZwSetPriorityRouteFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class ZwSetPriorityRoute(DATA_FRAME):
    id = 0x93
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _ZwSetPriorityRouteFields),
    ]

    _anonymous_ = ('_anon_union',)

    route_speeds = set_priority_route.command.route_speed

    @property
    def packet_length(self):
        return self._node_id_len + 5

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


class ZwSetPriorityRouteResponse(DATA_FRAME):
    id = 0x93
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def command_status(self):
        return self._command_status
