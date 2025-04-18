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
    uint8_t,
    uint16_t
)

from ..enums import memory_put_buffer


class FUNC_MEMORY_PUT_BUFFER_CMD(DATA_FRAME):
    """
    Copy a number of bytes from a RAM buffer to the application area of the NVM.
    """
    id = 0x24
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    _buffer_data = None

    _fields_ = [
        ('_offfset', uint16_t),
        ('_num_bytes', uint16_t),
        # data goes here
        ('_session_id', uint8_t)
    ]

    @property
    def packet_length(self):
        return self._num_bytes + 5

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, value: int):
        self._offset = value  # NOQA

    @property
    def data(self) -> bytearray:
        if self._buffer_data is None:
            return bytearray(0)

        return self._buffer_data[:self._num_bytes]

    @data.setter
    def data(self, value: bytearray):
        self._buffer_data = value
        self._num_bytes = len(value)  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class FUNC_MEMORY_PUT_BUFFER_RSP(DATA_FRAME):
    id = 0x24
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response', uint8_t)]

    responses = memory_put_buffer.response.response

    @property
    def response(self) -> responses:
        return self.responses(self._response)


class FUNC_MEMORY_PUT_BUFFER_CB(DATA_FRAME):
    id = 0x24
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def session_id(self) -> int:
        return self._session_id
