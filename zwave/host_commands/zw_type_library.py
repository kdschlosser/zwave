from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums.host import type_library


class ZwTypeLibrary(HOST_COMMAND):
    id = 0xBD
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwTypeLibraryResponse(HOST_RESPONSE):
    id = 0xBD

    _fields_ = [
        ('_library_type', uint8_t)
    ]

    library_types = type_library.response.library_type

    @property
    def library_type(self) -> library_types:
        return self.library_types(self._library_type)
