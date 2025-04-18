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
    uint8_t
)


class FUNC_NVR_GET_VALUE_CMD(DATA_FRAME):
    """
    Read a value from the NVR Flash memory area.

    The function will check the checksum of the NVR
    page and if the checksum is correct the function will read the value in NVR. If the checksum is incorrect
    the default unitialized value 0xFF will be read from all fields. The valid offset goes from 0x00 to 0xEF
    and to hide the lock bits from the application it is offset with 0x10 compared to the addresses that can
    be seen in the Z-Wave programmer when doing a raw read of the NVR.
    """
    id = 0x28
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_offfset', uint8_t),
        ('_num_bytes', uint8_t)
    ]

    @property
    def packet_length(self):
        return 2

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


class FUNC_NVR_GET_VALUE_RSP(DATA_FRAME):
    id = 0x28
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_buffer', uint8_t * 256)]

    @property
    def data(self) -> bytearray:
        return bytearray(self._buffer[:256])
