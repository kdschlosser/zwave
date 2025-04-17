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

from ..enums import type_library


class FUNC_ZW_TYPE_LIBRARY_CMD(DATA_FRAME):
    """
    Request the Z-Wave library type running on the Z-Wave module
    """
    id = 0xBD
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_TYPE_LIBRARY_RSP(DATA_FRAME):
    id = 0xBD
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_library_type', uint8_t)
    ]

    library_types = type_library.response.library_type

    @property
    def library_type(self) -> library_types:
        return self.library_types(self._library_type)
