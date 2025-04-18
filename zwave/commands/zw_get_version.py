"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import get_version


class FUNC_ZW_GET_VERSION_CMD(DATA_FRAME):
    """
    Get Library Version Command

    This command is used to request the Z-Wave library basis version that runs on a Z-Wave Module.
    """
    id = 0x15
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_VERSION_RSP(DATA_FRAME):
    id = 0x15
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_library_version', uint8_t * 12),
        ('_library_type', uint8_t)
    ]

    library_types = get_version.response.library_type

    @property
    def library_version(self) -> str:
        res = bytearray(12)

        for i in range(12):
            res[i] = self._library_version[i]

        return res.decode('utf-8')

    @property
    def library_type(self) -> library_types:
        return self.library_types(self._library_type)
