"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import rediscovery_needed


class FUNC_ZW_REDISCOVERY_NEEDED_CMD(DATA_FRAME):
    """
    This function can request a SUC/SIS controller to update the requesting nodes neighbors. The function
    will try to request a neighbor rediscovery from a SUC/SIS controller in the network. In order to reach a
    SUC/SIS controller it uses other nodes (bNodeID) in the network. The application must implement the
    algorithm for scanning the bNodeID’s to find a node which can help
    """
    id = 0x59
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id', uint8_t),
        ('_session_id', uint8_t)
    ]

    @property
    def packet_length(self):
        return 2

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class FUNC_ZW_REDISCOVERY_NEEDED_RSP(DATA_FRAME):
    id = 0x59
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t),
    ]

    @property
    def command_status(self) -> int:
        return self._command_status


class FUNC_ZW_REDISCOVERY_NEEDED_CB(DATA_FRAME):
    id = 0x59
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_route_status', uint8_t)
    ]

    route_statuses = rediscovery_needed.callback.route_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def route_status(self) -> route_statuses:
        return self.route_statuses(self._route_status)
