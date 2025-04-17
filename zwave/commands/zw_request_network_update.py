from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import request_network_update


class FUNC_ZW_REQUEST_NETWORK_UPDATE_CMD(DATA_FRAME):
    """
    Request an Automatic Controller Update from the SUC
    """
    id = 0x53
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t * 6)
    ]

    @property
    def packet_length(self):
        return 1

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value  # NOQA


class FUNC_ZW_REQUEST_NETWORK_UPDATE_RSP(DATA_FRAME):
    id = 0x53
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    @property
    def status(self):
        return self._status


class FUNC_ZW_REQUEST_NETWORK_UPDATE_CB(DATA_FRAME):
    id = 0x53
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = request_network_update.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
