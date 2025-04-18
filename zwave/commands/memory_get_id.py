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
    uint8_t,
    uint32_t
)


class FUNC_ZW_MEMORY_GET_ID_CMD(DATA_FRAME):
    """
    The MemoryGetID function copy the Home-ID and Node-ID from the NVM
    """
    id = 0x20
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_MEMORY_GET_ID_RSP(DATA_FRAME):
    id = 0x20
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_home_id', uint32_t),
        ('_node_id', uint8_t * 2),
    ]

    @property
    def home_id(self):
        return self._home_id

    @property
    def node_id(self) -> int:
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]
