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

from ..enums import set_suc_node_id


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('suc_state', uint8_t),
        ('tx_option', uint8_t),
        ('capabilities', uint8_t),
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('suc_state', uint8_t),
        ('tx_option', uint8_t),
        ('capabilities', uint8_t),
        ('session_id', uint8_t),
    ]


class _ZwSetSucNodeIdFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class ZwSetSucNodeId(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _ZwSetSucNodeIdFields),
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = set_suc_node_id.command.tx_option
    capabilities = set_suc_node_id.command.capability
    suc_states = set_suc_node_id.command.suc_state

    @property
    def packet_length(self):
        return self._node_id_len + 4

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def suc_state(self) -> suc_states:
        return self.suc_states(self._fields.suc_state)

    @suc_state.setter
    def suc_state(self, value: suc_states):
        self._fields.suc_state = value.value

    @property
    def tx_option(self) -> tx_options:
        return self.tx_options(self._fields.tx_option)

    @tx_option.setter
    def tx_option(self, value: tx_options):
        self._fields.tx_option = value.value

    @property
    def capability(self) -> capabilities:
        return self.capabilities(self._fields.capabilities)

    @capability.setter
    def capability(self, value: capabilities):
        self._fields.capabilities = value.value

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class ZwSetSucNodeIdResponse(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t),
    ]

    @property
    def command_status(self):
        return self._command_status


class ZwSetSucNodeIdCallback(DATA_FRAME):
    id = 0x54
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_suc_status', uint8_t),
    ]

    suc_statuses = set_suc_node_id.callback.suc_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def suc_status(self) -> suc_statuses:
        return self.suc_statuses(self._suc_status)
