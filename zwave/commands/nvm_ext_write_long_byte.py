"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint16_t,
    uint8_t
)


class FUNC_NVM_EXT_WRITE_LONG_BYTE_CMD(DATA_FRAME):
    """
    Write a byte to external NVM at address offset.
    """
    id = 0x2D
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 4

    _fields_ = [
        ('_offset1', uint16_t),
        ('_offset2', uint8_t),
        ('_data', uint8_t)
    ]

    @property
    def offset(self) -> int:
        return (self._offset1 << 8) | self._offset2

    @offset.setter
    def offset(self, value: int):
        self._offset1 = (value >> 8) & 0xFFFF  # NOQA
        self._offset2 = value & 0xFF  # NOQA

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value  # NOQA


class FUNC_NVM_EXT_WRITE_LONG_BYTE_RSP(DATA_FRAME):
    id = 0x2D
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response', uint8_t)]

    @property
    def response(self) -> int:
        return self._response
