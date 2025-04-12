from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums.host import set_priority_route


class ZwSetPriorityRoute(HOST_COMMAND):
    id = 0x93
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [
        ('_data', uint8_t * 6)
    ]

    route_speeds = set_priority_route.command.route_speed

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @node_id.setter
    def node_id(self, value):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value << 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def repeater(self) -> int:
        if self._node_id_len == 1:
            return (
                (self._data[1] << 24) |
                (self._data[2] << 16) |
                (self._data[3] << 8) |
                self._data[4]
            )
        else:
            return (
                (self._data[2] << 24) |
                (self._data[3] << 16) |
                (self._data[4] << 8) |
                self._data[5]
            )

    @repeater.setter
    def repeater(self, value: int):
        if self._node_id_len == 1:
            self._data[1] = (value >> 24) & 0xFF
            self._data[2] = (value >> 16) & 0xFF
            self._data[3] = (value >> 8) & 0xFF
            self._data[4] = value & 0xFF
        else:
            self._data[2] = (value >> 24) & 0xFF
            self._data[3] = (value >> 16) & 0xFF
            self._data[4] = (value >> 8) & 0xFF
            self._data[5] = value & 0xFF

    @property
    def route_speed(self) -> route_speeds:
        if self._node_id_len == 1:
            return self.route_speeds(self._data[5])
        else:
            return self.route_speeds(self._data[6])

    @route_speed.setter
    def route_speed(self, value: route_speeds):
        if self._node_id_len == 1:
            self._data[6] = value.value
        else:
            self._data[8] = value.value


class ZwSetPriorityRouteResponse(HOST_RESPONSE):
    id = 0x93

    _fields_ = [
        ('_response', uint8_t)
    ]

    @property
    def response(self):
        return self._response
