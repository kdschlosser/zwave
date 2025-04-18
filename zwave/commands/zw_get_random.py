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
    uint8_t
)


class FUNC_ZW_GET_RANDOM_CMD(DATA_FRAME):
    """
    Returns random data of variable length
    """
    id = 0x1C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_number_of_bytes', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def number_of_random_bytes(self) -> int:
        return self._number_of_bytes

    @number_of_random_bytes.setter
    def number_of_random_bytes(self, value: int):
        self._number_of_bytes = value  # NOQA


class FUNC_ZW_GET_RANDOM_RSP(DATA_FRAME):
    id = 0x1C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t),
        ('_number_of_bytes', uint8_t),
        ('_data', uint8_t * 256)
    ]

    @property
    def command_status(self) -> int:
        return self._command_status

    @property
    def random_bytes(self) -> bytearray:
        return bytearray(self._data[:self._number_of_bytes])
