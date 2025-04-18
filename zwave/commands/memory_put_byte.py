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
    uint16_t
)

from ..enums import memory_put_byte


class FUNC_MEMORY_PUT_BYTE_CMD(DATA_FRAME):
    """
    Write one byte to the application area of the NVM.

    On controllers and enhanced 232 slaves this function is based on external NVM and a long write time (2-
    5 msec.) must be taken into consideration when implementing the application.

    The data to be written to FLASH are not written immediately to the FLASH. Instead it is saved in a RAM
    buffer and then written when the RF is not active and it is more than 200ms ago the buffer was
    accessed.
    """
    id = 0x22
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_offfset', uint16_t),
        ('_data', uint8_t)
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
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value  # NOQA


class FUNC_MEMORY_PUT_BYTE_RSP(DATA_FRAME):
    id = 0x22
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response', uint8_t)]

    responses = memory_put_byte.response.response

    @property
    def response(self) -> responses:
        return self.responses(self._response)

