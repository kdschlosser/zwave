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
    uint16_t
)

from ..enums import send_data_bridge
from .. import tx_report


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('dst_node_id', uint8_t),
        ('data_len', uint8_t),
        ('data', uint8_t * 256)
    ]


class _NodeID16(NODE_ID_16_FRAME):

    _fields_ = [
        ('dst_node_id', uint16_t),
        ('data_len', uint8_t),
        ('data', uint8_t * 256)
    ]


class _Fields(NODE_ID_FIELDS):

    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16)
    ]


class FUNC_ZW_SEND_DATA_BRIDGE_CMD(DATA_FRAME):
    """
    Bridge Controller Node Send Data Command

    This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
    """
    id = 0xA9
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields)
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = send_data_bridge.command.tx_option

    @property
    def packet_length(self):
        return self._node_id_len * 2 + self._fields.data_len + 7

    @property
    def src_node_id(self) -> int:
        return self._fields.node_id

    @src_node_id.setter
    def src_node_id(self, value: int):
        self._fields.node_id = value

    @property
    def dst_node_id(self) -> int:
        return self._fields.dst_node_id

    @dst_node_id.setter
    def dst_node_id(self, value: int):
        self._fields.dst_node_id = value

    @property
    def data(self) -> bytearray:
        return bytearray(self._fields.data[:self._fields.data_len])

    @data.setter
    def data(self, value: bytearray):
        tx_option = self.tx_option
        route = self.route
        session_id = self.session_id

        self._fields.data_len = len(value)

        for i, item in enumerate(value):
            self._fields.data[i] = value

        self.tx_option = tx_option
        self.route = route
        self.session_id = session_id

    @property
    def tx_option(self) -> tx_options:
        offset = self._fields.data_len + 1
        return self.tx_options(self._data[offset])

    @tx_option.setter
    def tx_option(self, value: tx_options):
        offset = self._fields.data_len + 1
        self._data[offset] = value.value

    @property
    def route(self) -> list[int]:
        offset = self._fields.data_len + 2
        return [self._fields.data[i] for i in range(offset, offset + 4, 1)]

    @route.setter
    def route(self, value: list[int]):
        offset = self._fields.data_len + 2

        data = value[:]
        while len(data) < 4:
            data.append(0x00)

        for i, item in enumerate(data):
            self._fields.data[i + offset] = item

    @property
    def session_id(self) -> int:
        offset = self._fields.data_len + 6
        return self._data[offset]

    @session_id.setter
    def session_id(self, value: int):
        offset = self._fields.data_len + 6
        self._data[offset] = value


class FUNC_ZW_SEND_DATA_BRIDGE_RSP(DATA_FRAME):
    id = 0xA9
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response_status', uint8_t)
    ]

    @property
    def response_status(self) -> int:
        return self._response_status


class FUNC_ZW_SEND_DATA_BRIDGE_CB(DATA_FRAME):
    id = 0xA9
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t),
        ('_reports', tx_report.TXReport * 10)
    ]

    tx_statuses = send_data_bridge.callback.tx_status

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
