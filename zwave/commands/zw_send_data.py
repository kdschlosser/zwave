from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t
from ..enums import send_data
from .. import tx_report


class ZwSendData(DATA_FRAME):
    id = 0x13
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 256)
    ]

    options = send_data.command.option

    @property
    def node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @node_id.setter
    def node_id(self, value: int):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value >> 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def data(self) -> bytearray:
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        data_len = self._data[offset]
        offset += 1
        res = bytearray(data_len)
        for i in range(data_len):
            res[i] = self._data[offset + i]

        return res

    @data.setter
    def data(self, value: bytearray):
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        self._data[offset] = len(value)

        offset += 1
        for i, item in enumerate(value):
            self._data[offset + i] = item

    @property
    def option(self) -> options:
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        data_len = self._data[offset]
        offset += 2 + data_len
        return self.options(self._data[offset])

    @option.setter
    def option(self, value: options):
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        data_len = self._data[offset]
        offset += 2 + data_len
        self._data[offset] = value.value

    @property
    def session_id(self) -> int:
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        data_len = self._data[offset]
        offset += 3 + data_len
        return self._data[offset]

    @session_id.setter
    def session_id(self, value: int):
        if self._node_id_len == 1:
            offset = 1
        else:
            offset = 2

        data_len = self._data[offset]
        offset += 3 + data_len
        self._data[offset] = value


class ZwSendDataResponse(DATA_FRAME):
    id = 0x13
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def status(self) -> int:
        return self._status


class ZwSendDataCallback(DATA_FRAME):
    id = 0x13
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t),
        ('_reports', tx_report.TXReport * 10)
    ]

    tx_statuses = send_data.callback.status

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
