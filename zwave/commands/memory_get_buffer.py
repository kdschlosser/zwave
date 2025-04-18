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
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t,
    uint16_t
)


class FUNC_MEMORY_GET_BUFFER_CMD(DATA_FRAME):
    """
    Read a number of bytes from the NVM allocated for the application.

    If a write operation is in progress, the write queue will be checked for the actual data.
    """
    id = 0x23
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_offfset', uint16_t),
        ('_num_bytes', uint8_t)
    ]

    @property
    def packet_length(self):
        return 3

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, value: int):
        self._offset = value  # NOQA

    @property
    def number_of_bytes(self) -> int:
        return self._num_bytes

    @number_of_bytes.setter
    def number_of_bytes(self, value: int):
        self._num_bytes = value  # NOQA


class FUNC_MEMORY_GET_BUFFER_RSP(DATA_FRAME):
    id = 0x23
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_buffer', uint8_t * 256)]

    @property
    def data(self) -> bytearray:
        return bytearray(self._buffer[:256])
