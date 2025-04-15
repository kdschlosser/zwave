from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from .. import zw_types
from .. import command_classes


class SerialApiApplNodeInformation(DATA_FRAME):
    id = 0x03
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_listening_flag', uint8_t, 1),
        ('_reserved', uint8_t, 7),
        ('_generic_device_type', uint8_t),
        ('_specific_device_type', uint8_t),
        ('_command_class_list_len', uint8_t),
        ('_command_class_list', uint8_t * 256),
    ]

    @property
    def is_always_listening(self):
        return bool(self._listening_flag)

    @is_always_listening.setter
    def is_always_listening(self, value):
        self._listening_flag = int(bool(value))  # NOQA

    @property
    def generic_device_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._generic_device_type)

    @generic_device_type.setter
    def generic_device_type(self, value: zw_types.GENERIC_TYPE):
        self._generic_device_type = value.id  # NOQA

    @property
    def specific_device_type(self) -> zw_types.SPECIFIC_TYPES:
        generic_type = self.generic_device_type
        return generic_type(self._specific_device_type)

    @specific_device_type.setter
    def specific_device_type(self, value: zw_types.SPECIFIC_TYPES):
        self._specific_device_type = value.value  # NOQA

    @property
    def command_class_list(self) -> list[command_classes.COMMAND_CLASS]:
        return [
            command_classes.COMMAND_CLASS.from_id(item)
            for item in bytearray(self._command_class_list[:self.command_class_list_len])
        ]

    @command_class_list.setter
    def command_class_list(self, value: list[command_classes.COMMAND_CLASS]):
        for i, cc in enumerate(value):
            self._command_class_list[i] = cc.id

        self._command_class_list_len = len(value)  # NOQA
