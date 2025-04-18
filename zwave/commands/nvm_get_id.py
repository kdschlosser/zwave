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

import ctypes


class FUNC_NVM_GET_ID_CMD(DATA_FRAME):
    """
    Get NVM ID from external NVM.

    The NVM ID is collected using a NVM “read ID” command, but not all
    supported NVMs support this command, so the memoryCapacity is set according to the NVM
    information in the NVR.
    """
    id = 0x29
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_NVM_GET_ID_RSP(DATA_FRAME):
    id = 0x29
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_length', uint8_t),
        ('_nvm_id', uint8_t * 256)
    ]

    @property
    def nvm_id(self) -> bytearray:
        return bytearray(self._nvm_id[:self._length])
