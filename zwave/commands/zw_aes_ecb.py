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


class FUNC_ZW_AES_ECB_CMD(DATA_FRAME):
    """
    Encrypt Data With AES Command

    This command is used to request the Z-Wave API module to encrypt a Z-Wave frame payload using
    AES-128 Electronic CookBook mode.
    """
    id = 0x67
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_key', uint8_t * 16),
        ('_data', uint8_t * 16)
    ]

    @property
    def packet_length(self):
        return 32

    @property
    def key(self) -> bytearray:
        return bytearray(self._key)

    @key.setter
    def key(self, value: bytearray):
        if len(value) != 16:
            raise ValueError

        for i, item in value:
            self._key[i] = item

    @property
    def data(self) -> bytearray:
        return bytearray(self._data)

    @data.setter
    def data(self, value: bytearray):
        data = value[:]  # make a copy

        while len(data) != 16:
            data += bytearray([0x00])

        for i, item in data:
            self._data[i] = item


class FUNC_ZW_AES_ECB_RSP(DATA_FRAME):
    id = 0x67
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 16)
    ]

    @property
    def data(self) -> bytearray:
        res = bytearray()

        for i in range(16):
            if self._data[i] == 0x00:
                break

            res.append(self._data[i])

        return res
