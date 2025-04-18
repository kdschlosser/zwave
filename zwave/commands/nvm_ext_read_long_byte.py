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


class FUNC_NVM_EXT_READ_LONG_BYTE_CMD(DATA_FRAME):
    """
    Read a byte from external NVM at address offset.
    """
    id = 0x2C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 3

    _fields_ = [
        ('_offset1', uint16_t),
        ('_offset2', uint8_t)
    ]

    @property
    def offset(self) -> int:
        return (self._offset1 << 8) | self._offset2

    @offset.setter
    def offset(self, value: int):
        self._offset1 = (value >> 8) & 0xFFFF  # NOQA
        self._offset2 = value & 0xFF  # NOQA


class FUNC_NVM_EXT_READ_LONG_BYTE_RSP(DATA_FRAME):
    id = 0x2C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_data', uint8_t)]

    @property
    def data(self) -> int:
        return self._data
