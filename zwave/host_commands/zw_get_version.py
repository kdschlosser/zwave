from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums.host import get_version


class ZwGetVersion(HOST_COMMAND):
    id = 0x15
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwGetVersionResponse(HOST_RESPONSE):
    id = 0x15

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
