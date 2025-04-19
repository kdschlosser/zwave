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

from ..enums import set_priority_route


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('repeaters', uint8_t * 8),
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


class FUNC_ZW_SET_PRIORITY_ROUTE_CMD(DATA_FRAME):
    """
    Set Priority Route Command

    This command is used to set the Priority Route for a destination node. The Priority Route is the route
    that shall be used as the first routing attempt by the Z-Wave protocol when transmitting to a node. The
    Priority Route is expected to be stored in NVM of the Z-Wave module.
    """
    id = 0x93
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
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


class FUNC_ZW_SET_PRIORITY_ROUTE_RSP(DATA_FRAME):
    id = 0x93
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def command_status(self):
        return self._command_status
