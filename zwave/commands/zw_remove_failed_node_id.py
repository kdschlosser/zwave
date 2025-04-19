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
    uint8_t,
)

from ..enums import remove_failed_node_id
from ..command_classes import COMMAND_CLASS
from .. import zw_types


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


class FUNC_ZW_REMOVE_FAILED_NODE_ID_CMD(DATA_FRAME):
    """
    Remove Failed Node Command

    This command is used to request a non-responding node removal operation from the controller routing
    table. When a node is non-responding, its’ NodeID shall be included in the failed NodeID list. If the
    node responding again it shall be removed from the failed NodeID list. A failed node MUST only
    be removed if the NodeID is in the failed NodeID list and extra precaution shall be considered before
    the failed node is removed. A responding node MUST NOT be removed.
    """
    id = 0x61
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


class FUNC_ZW_REMOVE_FAILED_NODE_ID_RSP(DATA_FRAME):
    id = 0x61
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response_status', uint8_t),
    ]

    response_statuses = remove_failed_node_id.response.response_status

    @property
    def response_status(self) -> response_statuses:
        return self.response_statuses(self._response_status)


class FUNC_ZW_REMOVE_FAILED_NODE_ID_CB(DATA_FRAME):
    id = 0x61
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_operation_status', uint8_t),
    ]

    operation_statuses = remove_failed_node_id.callback.operation_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def operation_status(self) -> operation_statuses:
        return self.operation_statuses(self._operation_status)
