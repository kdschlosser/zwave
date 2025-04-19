"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import set_ext_int_level


class FUNC_ZW_SET_EXT_INT_LEVEL_CMD(DATA_FRAME):
    """
    This function MAY be used to set the trigger level for external interrupts.
    """
    id = 0xB9
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_int_src', uint8_t),
        ('_trigger_level', uint8_t)
    ]

    int_srcs = set_ext_int_level.command.int_src

    @property
    def packet_length(self):
        return 2

    @property
    def int_src(self) -> int_srcs:
        return self.int_srcs(self._int_src)

    @int_src.setter
    def int_src(self, value: int_srcs):
        self._int_src = value.value  # NOQA

    @property
    def trigger_level(self) -> int:
        return self._trigger_level

    @trigger_level.setter
    def trigger_level(self, value: int):
        self._trigger_level = int(bool(value))  # NOQA
