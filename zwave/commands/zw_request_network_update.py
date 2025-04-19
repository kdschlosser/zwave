"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

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
    Request Network Update Command

    This command is used to instruct the Z-Wave API Module to request an Automatic Controller Update
    to the SUC.
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
        ('_command_status', uint8_t),
    ]

    @property
    def command_status(self):
        return self._command_status


class FUNC_ZW_REQUEST_NETWORK_UPDATE_CB(DATA_FRAME):
    id = 0x53
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_network_update_status', uint8_t),
    ]

    network_update_statuses = request_network_update.callback.network_update_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def network_update_status(self) -> network_update_statuses:
        return self.network_update_statuses(self._network_update_status)
