from . import HOST_COMMAND, FRAME_TYPE_ACK, uint8_t
from ..enums.host import lock_unlock_last_route


class LockUnlockLastRoute(HOST_COMMAND):
    id = 0x90
    frame_type = FRAME_TYPE_ACK

    _fields_ = [
        ('_lock_mode', uint8_t)
    ]

    lock_modes = lock_unlock_last_route.command.lock_mode

    @property
    def lock_mode(self) -> lock_modes:
        return self.lock_modes(self._lock_mode)

    @lock_mode.setter
    def lock_mode(self, value: lock_modes):
        self._lock_mode = value.value  # NOQA
