from . import DATA_FRAME, FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import request_new_route_destinations


class ZwRequestNewRouteDestinations(DATA_FRAME):
    id = 0x5C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 200)
    ]

    def nodes(self, value: list[Node]):
        for i, node in enumerate(value):
            self._data[i] = node.id

        self._nodes_len = len(value)

    nodes = property(fset=nodes)

    def session_id(self, value):
        self._data[self._nodes_len] = value

    session_id = property(fset=session_id)


class ZwRequestNewRouteDestinationsResponse(DATA_FRAME):
    id = 0x5C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response', uint8_t)
    ]

    @property
    def request_new_route_response(self) -> bool:
        return bool(self._response)


class ZwRequestNewRouteDestinationsCallback(DATA_FRAME):
    id = 0x5C
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t)
    ]

    statuses = request_new_route_destinations.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
