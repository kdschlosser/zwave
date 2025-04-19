"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import lock_unlock_last_route


class FUNC_LOCK_ROUTE_RESPONSE_CMD(DATA_FRAME):
    """
    Lock Unlock Last Route Command

    This command is used to lock or unlock all last working route.
    """
    id = 0x90
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_lock_mode', uint8_t)
    ]

    lock_modes = lock_unlock_last_route.command.lock_mode

    @property
    def packet_length(self):
        return 1

    @property
    def lock_mode(self) -> lock_modes:
        return self.lock_modes(self._lock_mode)

    @lock_mode.setter
    def lock_mode(self, value: lock_modes):
        self._lock_mode = value.value  # NOQA
