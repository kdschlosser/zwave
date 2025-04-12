from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums.host import get_protocol_version


class ZwGetProtocolVersion(HOST_COMMAND):
    id = 0x09
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwGetProtocolVersionResponse(HOST_RESPONSE):
    id = 0x09

    _fields_ = [
        ('_protocol_type', uint8_t),
        ('_major', uint8_t),
        ('_minor', uint8_t),
        ('_revision', uint8_t),
        ('_build_number1', uint8_t),
        ('_build_number2', uint8_t),
        ('_git_commit_hash', uint8_t * 16)
    ]

    protocol_types = get_protocol_version.response.protocol_type

    @property
    def protocol_type(self) -> protocol_types:
        return self.protocol_types(self._protocol_type)

    @property
    def protocol_version(self) -> str:
        return f'{self._major}.{self._minor}.{self._revision}'

    @property
    def build_number(self) -> int:
        return (self._build_number1 << 8) | self._build_number2

    @property
    def git_commit(self) -> str:
        res = ''
        for i in range(32):
            res += hex(self._git_commit_hash[i])[2:]
        return res
