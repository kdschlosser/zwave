from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import appl_slave_node_information
from .. import zw_types
from ..command_classes import COMMAND_CLASS


class SerialApiApplSlaveNodeInformation(DATA_FRAME):
    id = 0xA0
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id', uint8_t),
        ('_device_option_mask', uint8_t),
        ('_generic_device_type', uint8_t),
        ('_specific_device_type', uint8_t),
        ('_command_class_list_len', uint8_t),
        ('_command_classes', uint8_t * 256),

    ]

    options = appl_slave_node_information.command.option

    @property
    def packet_length(self):
        return self._command_class_list_len + 5

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA

    @property
    def option(self) -> options:
        return self.options(self._device_option_mask)

    @option.setter
    def option(self, value: options):
        self._device_option_mask = value.value  # NOQA

    @property
    def generic_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._generic_device_type)

    @generic_type.setter
    def generic_type(self, value: zw_types.GENERIC_TYPE):
        self._generic_device_type = value.id  # NOQA

    @property
    def specific_type(self) -> zw_types.SPECIFIC_TYPES:
        return self.generic_type(self._specific_device_type)

    @specific_type.setter
    def specific_type(self, value: zw_types.SPECIFIC_TYPES):
        self._generic_device_type = value.value  # NOQA

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        return [
            COMMAND_CLASS.from_id(self._command_classes[i])
            for i in range(self._command_class_list_len)
        ]

    @command_classes.setter
    def command_classes(self, value: list[COMMAND_CLASS]):
        for i in range(50):
            self._command_classes[i] = 0

        for i, cc in enumerate(value):
            self._command_classes[i] = cc.id

        self._command_class_list_len = len(value)  # NOQA
