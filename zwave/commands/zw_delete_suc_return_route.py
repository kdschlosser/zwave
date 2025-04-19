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
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)

from ..enums import delete_suc_return_route


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('session_id', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_DELETE_SUC_RETURN_ROUTE_CMD(DATA_FRAME):
    """
    Delete SUC Return Route Command

    This command is used to request the deletion of the SUC/SIS return routes.
    """
    id = 0x55
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len + 1

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class FUNC_ZW_DELETE_SUC_RETURN_ROUTE_RSP(DATA_FRAME):
    id = 0x55
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_return_route_response', uint8_t),
    ]

    return_route_responses = delete_suc_return_route.response.return_route_response

    @property
    def return_route_response(self) -> return_route_responses:
        return self.return_route_responses(self._return_route_response)


class FUNC_ZW_DELETE_SUC_RETURN_ROUTE_CB(DATA_FRAME):
    id = 0x55
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    tx_statuses = delete_suc_return_route.callback.tx_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> tx_statuses:
        return self.tx_statuses(self._status)
