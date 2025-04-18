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

from ..enums import send_data_multi


class FUNC_ZW_SEND_DATA_MULTI_CMD(DATA_FRAME):
    """
    Controller Node Send Data Multicast Command

    This command is used to transmit a data buffer to a list of Z-Wave nodes (i.e., Multicast frame).
    """
    id = 0x14
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    fields_ = [
        ('_node_id_count', uint8_t),
        ('_data', uint8_t * 256)
    ]

    tx_options = send_data_multi.command.tx_option

    @property
    def packet_length(self):
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        offset += self._data[offset] + 3

        return offset + 1

    @property
    def node_ids(self) -> list[int]:
        res = []
        if self._node_id_len == 1:
            for i in range(self._node_id_count):
                res.append(self._data[i])
        else:
            for i in range(self._node_id_count):
                res.append(self._data[i * 2] << 8 | self._data[i * 2 + 1])

        return res

    @node_ids.setter
    def node_ids(self, value: list[int]):
        data = self.data
        tx_option = self.tx_option
        session_id = self.session_id

        if self._node_id_len == 1:
            for i, item in enumerate(value):
                self._data[i] = item
        else:
            for i, item in enumerate(value):
                self._data[i * 2] = (item >> 8) & 0xFF
                self._data[i * 2 + 1] = item & 0xFF

        self._node_id_count = len(value)  # NOQA

        self.data = data
        self.tx_option = tx_option
        self.session_id = session_id

    @property
    def data(self) -> bytearray:
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        data_len = self._data[offset]
        offset += 1

        res = bytearray(data_len)

        for i in range(data_len):
            res[i] = self._data[i + offset]

        return res

    @data.setter
    def data(self, value: bytearray):
        tx_option = self.tx_option
        session_id = self.session_id

        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        self._data[offset] = len(value)
        offset += 1
        for i, item in enumerate(value):
            self._data[i + offset] = item

        self.tx_option = tx_option
        self.session_id = session_id

    @property
    def tx_option(self) -> tx_options:
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        offset += self._data[offset] + 2

        return self.tx_options(self._data[offset])

    @tx_option.setter
    def tx_option(self, value: tx_options):
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        offset += self._data[offset] + 2
        self._data[offset] = value.value

    @property
    def session_id(self) -> int:
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        offset += self._data[offset] + 3

        return self._data[offset]

    @session_id.setter
    def session_id(self, value: int):
        offset = self._node_id_count
        if self._node_id_len == 2:
            offset *= 2

        offset += 1
        offset += self._data[offset] + 3
        self._data[offset] = value


class FUNC_ZW_SEND_DATA_MULTI_RSP(DATA_FRAME):
    id = 0x14
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class FUNC_ZW_SEND_DATA_MULTI_CB(DATA_FRAME):
    id = 0x14
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t)
    ]

    tx_statuses = send_data_multi.callback.tx_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)
