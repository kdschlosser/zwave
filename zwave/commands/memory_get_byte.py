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
    uint8_t,
    uint16_t,
)


class FUNC_MEMORY_GET_BYTE_CMD(DATA_FRAME):
    """
    Read one byte from the NVM allocated for the application.

    If a write operation is in progress, the write queue will be checked for the actual data.
    """
    id = 0x21
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_offfset', uint16_t)]

    @property
    def packet_length(self):
        return 2

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, value: int):
        self._offset = value  # NOQA


class FUNC_MEMORY_GET_BYTE_RSP(DATA_FRAME):
    id = 0x21
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_data', uint8_t)]

    @property
    def data(self) -> int:
        return self._data
