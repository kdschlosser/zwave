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

from ..enums import send_suc_node_id


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('tx_option', uint8_t),
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('tx_option', uint8_t),
        ('session_id', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_SEND_SUC_ID_CMD(DATA_FRAME):
    """
    Send SUC NodeID Command

    This command is used to trigger the transfer of SUC/SIS NodeID from Primary/Static controller to a
    given controller NodeID.
    """
    id = 0x57
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = send_suc_node_id.command.tx_option

    @property
    def packet_length(self):
        return self._node_id_len + 2

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def tx_option(self) -> tx_options:
        return self.tx_options(self._fields.tx_option)

    @tx_option.setter
    def tx_option(self, value: tx_options):
        self._fields.tx_option = value.value

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class FUNC_ZW_SEND_SUC_ID_RSP(DATA_FRAME):
    id = 0x57
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t),
    ]

    @property
    def command_status(self):
        return self._command_status


class FUNC_ZW_SEND_SUC_ID_CB(DATA_FRAME):
    id = 0x57
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_tx_status', uint8_t),
    ]

    tx_statuses = send_suc_node_id.callback.tx_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)
