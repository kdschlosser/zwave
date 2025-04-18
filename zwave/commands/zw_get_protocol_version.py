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

from ..enums import get_protocol_version


"""

 zwave    |  serial   |    zwave    |   serial api
protocol  | api apps  |    plus     |   interface
version   |  version  |  framework  |    version
6.09.00       6.09        4.04.01           8
6.08.00       6.08        4.04.00           8
6.07.00       6.07        4.03.00           8
6.06.00       6.06        4.02.00           8
6.05.00       6.05        4.01.03           8
6.04.00       6.04        4.01.02           8
6.03.00       6.01        4.01.02           8
6.02.00       6.01        4.01.01           8
6.01.00       5.14        4.01.00           8
6.01.00       5.14        4.01.00           8
5.03.00       5.50        3.01.01           7
5.02.00       3.01        3.01.00           7 

4.62          5.36                          6
4.61          5.34                          7
4.60          5.29                          7
4.33          5.10                          6
4.54                                        5
4.45          5.19                          6
4.38                                        5
4.34                                        5
4.28          5.05                          6
4.24                                        5
4.12          1.12                          6
4.05                                        5
4.01                                        5 

3.99                                        5
3.95                                        5
3.92                                        5
3.83                                        5
3.79                                        5
3.71                                        5
3.67                                        5
3.53                                        5
3.52                                        5
3.45                                        5
3.42                                        5
3.41                                        5
3.40                                        5
3.38                                        5
3.37                                        5
3.36                                        5
3.35                                        5
3.34                                        5
3.33                                        5
3.28                                        5
3.26                                        5
3.22                                        5
3.20                                        5
3.10                                        5
3.07                                        5
3.06                                        5
3.04                                        5
3.03                                        5

2.99                                        5
2.97                                        5
2.96                                        5
2.78                                        5
2.64                                        5
2.51                                        5
2.48                                        5
2.36                                        5
2.22                                        5
2.16                                        5

"""


class FUNC_ZW_GET_PROTOCOL_VERSION_CMD(DATA_FRAME):
    """
    Used to request the Z-Wave Protocol version data (700 series)
    """
    id = 0x09
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_PROTOCOL_VERSION_RSP(DATA_FRAME):
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
