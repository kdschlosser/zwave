from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)
from ..enums import send_nop
from .. import tx_report


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


class _SendNOPFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class SendNOP(DATA_FRAME):
    id = 0xE9
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_anon_union', _SendNOPFields)]

    _anonymous_ = ('_anon_union',)

    tx_options = send_nop.command.tx_option

    @property
    def packet_length(self):
        return self._node_id_len + 2

    @property
    def destination_node_id(self) -> int:
        return self._fields.node_id

    @destination_node_id.setter
    def destination_node_id(self, value: int):
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


class SendNOPResponse(DATA_FRAME):
    id = 0xE9
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self):
        return self._response_status


class SendNOPCallback(DATA_FRAME):
    id = 0xE9
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t),
        ('_tx_report', tx_report.TXReport)
    ]

    tx_statuses = send_nop.callback.tx_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self._tx_statuses(self._tx_status)

    @property
    def tx_report(self) -> tx_report.TXReport:
        return self._tx_report
