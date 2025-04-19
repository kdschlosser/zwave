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
    uint8_t,
    uint16_t
)

from ..enums import get_priority_route


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_GET_PRIORITY_ROUTE_CMD(DATA_FRAME):
    """
    Get Priority Route Command

    This command is used to request the priority route that is defined in the Z-Wave API module. If a route
    has been set to the module using Set Priority Route Command, the module MUST provide the priority
    route using Get Priority Route Command Response frame. If no priority route has been set in the
    module, the Get Priority Route Command Response frame MUST contain either the Last WorkingRoute
    (LWR) or the Next to Last Working Route (NLWR).
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
        ('repeaters', uint8_t * 4),
        ('route_speed', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('repeaters', uint16_t * 4),
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
    def repeaters(self) -> list[int]:
        return [
            self._fields.repeaters[i]
            for i in range(4)
            if self._fields.repeaters[i] != 0x00
        ]

    @repeaters.setter
    def repeaters(self, value: list[int]):
        for i, item in enumerate(value):
            self._fields.repeaters[i] = item

    @property
    def route_speed(self) -> route_speeds:
        return self.route_speeds(self._fields.route_speed)

    @route_speed.setter
    def route_speed(self, value: route_speeds):
        self._fields.route_speed = value.value
