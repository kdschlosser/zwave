from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import get_protocol_version


class ZwGetProtocolVersion(DATA_FRAME):
    id = 0x09
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class ZwGetProtocolVersionResponse(DATA_FRAME):
    id = 0x09
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

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
