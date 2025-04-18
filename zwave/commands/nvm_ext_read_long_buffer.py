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
    uint16_t,
    uint8_t
)


class FUNC_NVM_EXT_READ_LONG_BUFFER_CMD(DATA_FRAME):
    """
    Read a number of bytes from external NVM starting from address offset.
    """
    id = 0x2A
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_offset1', uint16_t),
        ('_offset2', uint8_t),
        ('_num_bytes', uint16_t)
    ]

    @property
    def packet_length(self):
        return 5

    @property
    def offset(self) -> int:
        return (self._offset1 << 8) | self._offset2

    @offset.setter
    def offset(self, value: int):
        self._offset1 = (value >> 8) & 0xFFFF  # NOQA
        self._offset2 = value & 0xFF  # NOQA

    @property
    def number_of_bytes(self) -> int:
        return self._num_bytes

    @number_of_bytes.setter
    def number_of_bytes(self, value: int):
        self._num_bytes = value  # NOQA


class FUNC_NVM_EXT_READ_LONG_BUFFER_RSP(DATA_FRAME):
    id = 0x2A
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_data', uint8_t * 256)]

    @property
    def data(self) -> bytearray:
        return bytearray(self._data[:256])
