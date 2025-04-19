"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import send_data_multi_bridge


class FUNC_ZW_SEND_DATA_MULTI_BRIDGE_CMD(DATA_FRAME):
    """
    Send data using multicast (Bridge API)

    Transmit the data buffer to a list of Z-Wave Nodes (multicast frame). If the transmit optionflag
    TRANSMIT_OPTION_ACK is set the data buffer is also sent as a singlecast frame to each of the
    Z-Wave Nodes in the node list

    NOTE: This function is only available in the Bridge Controller library.
    """
    id = 0xAB
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id', uint8_t),
        ('_num_nodes', uint8_t),
        ('_data', uint8_t * 256)
    ]

    tx_options = send_data_multi_bridge.command.tx_option

    @property
    def packet_length(self):
        data_len = self._num_nodes + 1
        data_len += self._data[data_len] + 1
        return data_len + 4

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA

    @property
    def node_ids(self) -> list[int]:
        ret = []
        for i in range(self._num_nodes):
            ret.append(self._data[i])

        return ret

    @node_ids.setter
    def node_ids(self, value: list[int]):
        data = self.data
        tx_option = self.tx_option
        session_id = self.session_id

        self._num_nodes = len(value)  # NOQA
        for i, item in enumerate(value):
            self._data[i] = item

        self.data = data
        self.tx_option = tx_option
        self.session_id = session_id

    @property
    def data(self) -> bytearray:
        offset = self._num_nodes + 1
        data_len = self._data[offset]
        offset += 1

        return bytearray(self._data[offset:offset + data_len])

    @data.setter
    def data(self, value: bytearray):
        tx_option = self.tx_option
        session_id = self.session_id

        offset = self._num_nodes + 1
        self._data[offset] = len(value)
        offset += 1
        for i, item in enumerate(value):
            self._data[offset + i] = item

        self.tx_option = tx_option
        self.session_id = session_id

    @property
    def tx_option(self) -> tx_options:
        offset = self._num_nodes + 1
        offset += self._data[offset] + 1
        return self.tx_options(self._data[offset])

    @tx_option.setter
    def tx_option(self, value: tx_options):
        session_id = self.session_id

        offset = self._num_nodes + 1
        offset += self._data[offset] + 1
        self._data[offset] = value.value

        self.session_id = session_id

    @property
    def session_id(self) -> int:
        offset = self._num_nodes + 1
        offset += self._data[offset] + 2
        return self._data[offset]

    @session_id.setter
    def session_id(self, value: int):
        offset = self._num_nodes + 1
        offset += self._data[offset] + 2
        self._data[offset] = value


class FUNC_ZW_SEND_DATA_MULTI_BRIDGE_RSP(DATA_FRAME):
    id = 0xAB
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status


class FUNC_ZW_SEND_DATA_MULTI_BRIDGE_CB(DATA_FRAME):
    id = 0xAB
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t)
    ]

    tx_statuses = send_data_multi_bridge.callback.tx_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)
