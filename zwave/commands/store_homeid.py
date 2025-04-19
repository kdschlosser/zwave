"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint32_t
)


class FUNC_STORE_HOMEID_CMD(DATA_FRAME):
    """
    Function that can be used to restore HomeID and NodeID information from a
    backup.
    """
    id = 0x84
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_home_id', uint32_t)]

    @property
    def packet_length(self):
        return 4

    @property
    def home_id(self)-> int:
        return self._home_id

    @home_id.setter
    def home_id(self, value: int):
        self._home_id = value  # NOQA
