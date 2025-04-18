from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import request_new_route_destinations


class FUNC_ZW_REQUEST_NEW_ROUTE_DESTINATIONS_CMD(DATA_FRAME):
    """
    ???
    """
    id = 0x5C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _packet_length = 0

    _fields_ = [
        ('_data', uint8_t * 256),
    ]

    @property
    def packet_length(self):
        return self._packet_length + 1

    @property
    def node_ids(self) -> list[int]:
        if self._packet_length == 0:
            return []

        return [self._data[i] for i in range(self._packet_length - 1)]

    @node_ids.setter
    def node_ids(self, value: list[int]):
        session_id = self.session_id

        self._packet_length = len(value)

        for i, item in enumerate(value):
            self._data[i] = item

        self._data[len(value)] = session_id

    @property
    def session_id(self) -> int:
        return self._data[self._packet_length]

    @session_id.setter
    def session_id(self, value: int):
        self._data[self._packet_length] = value


class FUNC_ZW_REQUEST_NEW_ROUTE_DESTINATIONS_RSP(DATA_FRAME):
    id = 0x5C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response', uint8_t)
    ]

    @property
    def request_new_route_response(self) -> bool:
        return bool(self._response)


class FUNC_ZW_REQUEST_NEW_ROUTE_DESTINATIONS_CB(DATA_FRAME):
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
