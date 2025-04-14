from . import DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_UNSOLICITED, uint8_t
from ..enums import serial_api_started

from ..command_classes import COMMAND_CLASS

from .. import zw_types


class SerialApiStarted(DATA_FRAME):
    id = 0x0A
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK

    _fields_ = [
        ('_wakeup_reason', uint8_t),
        ('_watchdog_started', uint8_t),
        ('_option_mask', uint8_t),
        ('_generic_type', uint8_t),
        ('_specific_type', uint8_t),
        ('_command_class_list_len', uint8_t),
        ('_command_classes', uint8_t),
    ]

    wakeup_reasons = serial_api_started.unsolicited.wakeup
    options = serial_api_started.unsolicited.option

    @property
    def wakeup_reason(self) -> wakeup_reasons:
        return self.wakeup_reasons(self._wakeup_reason)

    @property
    def watchdog_started(self) -> bool:
        return bool(self._watchdog_started)

    @property
    def option(self) -> options:
        return self.options(self._option_mask)

    @property
    def generic_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._generic_type)

    @property
    def specific_type(self) -> zw_types.SPECIFIC_TYPES:
        return self.generic_type(self._specific_type)

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        res = []

        for i in range(self._command_class_list_len):
            res.append(COMMAND_CLASS.from_id(self._command_classes[i]))

        return res

    @property
    def supports_lr(self) -> bool:
        return bool(self._command_classes[self._command_class_list_len])

