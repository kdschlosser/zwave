from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import assign_priority_suc_return_route


class ZwAssignPrioritySucReturnRoute(DATA_FRAME):
    id = 0x58
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 9)
    ]

    route_speeds = assign_priority_suc_return_route.command.route_speed

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
    def dest_node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return (self._data[2] << 8) | self._data[3]

    @dest_node_id.setter
    def dest_node_id(self, value: int):
        if self._node_id_len == 1:
            self._data[1] = value
        else:
            self._data[2] = (value << 8) & 0xFF
            self._data[3] = value & 0xFF

    @property
    def repeater(self) -> int:
        if self._node_id_len == 1:
            return (
                (self._data[2] << 24) |
                (self._data[3] << 16) |
                (self._data[4] << 8) |
                self._data[5]
            )
        else:
            return (
                (self._data[4] << 24) |
                (self._data[5] << 16) |
                (self._data[6] << 8) |
                self._data[7]
            )

    @repeater.setter
    def repeater(self, value: int):
        if self._node_id_len == 1:
            self._data[2] = (value >> 24) & 0xFF
            self._data[3] = (value >> 16) & 0xFF
            self._data[4] = (value >> 8) & 0xFF
            self._data[5] = value & 0xFF
        else:
            self._data[4] = (value >> 24) & 0xFF
            self._data[5] = (value >> 16) & 0xFF
            self._data[6] = (value >> 8) & 0xFF
            self._data[7] = value & 0xFF

    @property
    def route_speed(self) -> route_speeds:
        if self._node_id_len == 1:
            return self.route_speeds(self._data[6])
        else:
            return self.route_speeds(self._data[8])

    @route_speed.setter
    def route_speed(self, value: route_speeds):
        if self._node_id_len == 1:
            self._data[6] = value.value
        else:
            self._data[8] = value.value

    @property
    def session_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[7]
        else:
            return self._data[9]

    @session_id.setter
    def session_id(self, value: int):
        if self._node_id_len == 1:
            self._data[7] = value
        else:
            self._data[9] = value


class ZwAssignPrioritySucReturnRouteResponse(DATA_FRAME):
    id = 0x58
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response', uint8_t)
    ]

    @property
    def response(self):
        return self._response


class ZwAssignPrioritySucReturnRouteCallback(DATA_FRAME):
    id = 0x58
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t)
    ]

    statuses = assign_priority_suc_return_route.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

