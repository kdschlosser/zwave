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

from ..enums import send_data
from .. import tx_report


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('data_len', uint8_t),
        ('data', uint8_t * 257),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('data_len', uint8_t),
        ('data', uint8_t * 257),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_SEND_DATA_CMD(DATA_FRAME):
    """
    Controller Node Send Data Command

    This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
    """
    id = 0x13
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = send_data.command.tx_option

    @property
    def packet_length(self):
        return self._fields.data_len + self._node_id_len + 2

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def data(self) -> bytearray:
        return bytearray(self._data[:self._fields.data_len])

    @data.setter
    def data(self, value: bytearray):
        session_id = self.session_id
        option = self.option

        for i, item in enumerate(value):
            self._fields.data[i] = value

        self._fields.data_len = len(value)
        self.option = option
        self.session_id = session_id

    @property
    def option(self) -> tx_options:
        return self.tx_options(self._fields.data[self._fields.data_len])

    @option.setter
    def option(self, value: tx_options):
        self._fields.data[self._fields.data_len] = value.value

    @property
    def session_id(self) -> int:
        return self._fields.data[self._fields.data_len + 1]

    @session_id.setter
    def session_id(self, value: int):
        self._fields.data[self._fields.data_len + 1] = value


class FUNC_ZW_SEND_DATA_RSP(DATA_FRAME):
    id = 0x13
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def status(self) -> int:
        return self._status


class FUNC_ZW_SEND_DATA_CB(DATA_FRAME):
    id = 0x13
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t),
        ('_reports', tx_report.TXReport * 10)
    ]

    tx_statuses = send_data.callback.tx_status

    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)

    @property
    def tx_reports(self) -> list[tx_report.TXReport]:
        import ctypes
        res = []
        count = int((self._length - 6) / ctypes.sizeof(tx_report.TXReport))

        for i in range(count):
            res.append(self._reports[i])

        return res
