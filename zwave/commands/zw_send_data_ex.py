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

from ..enums import send_data_ex
from .. import tx_report


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('data_length', uint8_t),
        ('data', uint8_t * 261),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('data_length', uint8_t),
        ('data', uint8_t * 261),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_SEND_DATA_EX_CMD(DATA_FRAME):
    """
    End Node Send Data Command

    This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
    This command MUST only be supported by End node library types
    """

    id = 0x0E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_anon_union', _Fields)]

    _anonymous_ = ('_anon_union',)

    tx_options = send_data_ex.command.tx_option
    tx_security_options = send_data_ex.command.tx_security_option
    security_keys = send_data_ex.command.security_key
    tx_options2 = None

    @property
    def packet_length(self):
        return self._node_id_len + self._fields.data_length + 6

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def data(self) -> bytearray:
        return bytearray(self._fields.data[:self._fields.data_length])

    @data.setter
    def data(self, value: bytearray):
        self._fields.data_length = len(value)

        for i, item in enumerate(value):
            self._fields.data[i] = item

    @property
    def tx_option(self) -> tx_options:
        return self.tx_options(self._fields.data[self._fields.data_length + 1])

    @tx_option.setter
    def tx_option(self, value: tx_options):
        self._fields.data[self._fields.data_length + 1] = value.value

    @property
    def tx_security_option(self) -> tx_security_options:
        return self.tx_security_options(self._fields.data[self._fields.data_length + 2])

    @tx_security_option.setter
    def tx_security_option(self, value: tx_security_options):
        self._fields.data[self._fields.data_length + 2] = value.value

    @property
    def security_key(self) -> security_keys:
        return self.security_keys(self._fields.data[self._fields.data_length + 3])

    @security_key.setter
    def security_key(self, value: security_keys):
        self._fields.data[self._fields.data_length + 3] = value.value

    @property
    def tx_option2(self) -> tx_options2:
        raise NotImplementedError

    @tx_option2.setter
    def tx_option2(self, value: tx_options2):
        raise NotImplementedError

    @property
    def session_id(self) -> int:
        return self._fields.data[self._fields.data_length + 5]

    @session_id.setter
    def session_id(self, value: int):
        self._fields.data[self._fields.data_length + 5] = value


class FUNC_ZW_SEND_DATA_EX_RSP(DATA_FRAME):
    id = 0x0E
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class FUNC_ZW_SEND_DATA_EX_CB(DATA_FRAME):
    id = 0x0E
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t),
        ('_tx_report', tx_report.TXReport)
    ]

    tx_statuses = send_data_ex.callback.tx_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self._tx_statuses(self._tx_status)

    @property
    def tx_report(self) -> tx_report.TXReport:
        return self._tx_report
