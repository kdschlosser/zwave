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

from ..enums import send_node_information


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


class _ZwSendNodeInformationFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class ZwSendNodeInformation(DATA_FRAME):
    id = 0x12
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _ZwSendNodeInformationFields),
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = send_node_information.command.tx_option

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


class ZwSendNodeInformationResponse(DATA_FRAME):
    id = 0x12
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class ZwSendNodeInformationCallback(DATA_FRAME):
    id = 0x12
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t)
    ]

    tx_statuses = send_node_information.callback.tx_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)
