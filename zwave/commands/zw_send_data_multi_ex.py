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

from ..enums import send_data_multi_ex


class FUNC_ZW_SEND_DATA_MULTI_EX_CMD(DATA_FRAME):
    """
    End Node Send Data Multicast Command

    This command is used to transmit a data buffer to a list of Z-Wave nodes (i.e., S2 Multicast frame).
    """

    id = 0x0F
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data_length', uint8_t),
        ('_data', uint8_t * 261),
    ]

    tx_options = send_data_multi_ex.command.tx_option
    security_keys = send_data_multi_ex.command.security_key

    @property
    def packet_length(self):
        return self._data_length + 5

    @property
    def data(self) -> bytearray:
        return bytearray(self._data[:self._data_length])

    @data.setter
    def data(self, value: bytearray):
        self._data_length = len(value)  # NOQA

        for i, item in enumerate(value):
            self._data[i] = item

    @property
    def tx_option(self) -> tx_options:
        return self.tx_options(self._data[self._data_length + 1])

    @tx_option.setter
    def tx_option(self, value: tx_options):
        self._data[self._data_length + 1] = value.value

    @property
    def security_key(self) -> security_keys:
        return self.security_keys(self._data[self._data_length + 2])

    @security_key.setter
    def security_key(self, value: security_keys):
        self._data[self._data_length + 2] = value.value

    @property
    def multicast_group_id(self) -> int:
        return self._data[self._data_length + 3]

    @multicast_group_id.setter
    def multicast_group_id(self, value: int):
        self._data[self._data_length + 3] = value

    @property
    def session_id(self) -> int:
        return self._data[self._data_length + 4]

    @session_id.setter
    def session_id(self, value: int):
        self._data[self._data_length + 4] = value


class FUNC_ZW_SEND_DATA_MULTI_EX_RSP(DATA_FRAME):
    id = 0x0F
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class FUNC_ZW_SEND_DATA_MULTI_EX_CB(DATA_FRAME):
    id = 0x0F
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_tx_status', uint8_t)
    ]

    tx_statuses = send_data_multi_ex.callback.tx_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self._tx_statuses(self._tx_status)
