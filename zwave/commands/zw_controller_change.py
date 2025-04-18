"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import controller_change
from ..command_classes import COMMAND_CLASS
from .. import zw_types


class FUNC_ZW_CONTROLLER_CHANGE_CMD(DATA_FRAME):
    """
    Add Primary Controller Command

    This command is used to include a controller node and assign it the Primary Controller Role.
    """
    id = 0x4D
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_power', uint8_t, 1),
        ('_nwi', uint8_t, 1),
        ('_protocol', uint8_t, 1),
        ('_mode', uint8_t, 5),
        ('_session_id', uint8_t)
    ]

    modes = controller_change.command.mode

    @property
    def packet_length(self):
        return 2

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value  # NOQA

    @property
    def nwi(self):
        return self._nwi

    @nwi.setter
    def nwi(self, value):
        self._nwi = value  # NOQA

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value  # NOQA

    @property
    def mode(self) -> modes:
        return self.modes(self._mode)

    @mode.setter
    def mode(self, value: modes):
        self._mode = value.value  # NOQA

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value  # NOQA


class FUNC_ZW_CONTROLLER_CHANGE_CB(DATA_FRAME):
    id = 0x4D
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t),
        ('_data', uint8_t * 256),
    ]

    statuses = controller_change.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @property
    def __command_class_list_len(self):
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return self._data[2]

    @property
    def basic_device_type(self) -> zw_types.BASIC_TYPE:
        if self._node_id_len == 1:
            return zw_types.BASIC_TYPE(self._data[2])
        else:
            return zw_types.BASIC_TYPE(self._data[3])

    @property
    def generic_device_type(self) -> zw_types.GENERIC_TYPE:
        if self._node_id_len == 1:
            return zw_types.GENERIC_TYPE(self._data[3])
        else:
            return zw_types.GENERIC_TYPE(self._data[4])

    @property
    def specific_device_type(self) -> zw_types.SPECIFIC_TYPES:
        generic_type = self.generic_device_type

        if self._node_id_len == 1:
            return generic_type(self._data[4])
        else:
            return generic_type(self._data[5])

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        if self._node_id_len == 1:
            start = 5
        else:
            start = 6

        stop = start + self.__command_class_list_len

        res = []

        for i in range(start, stop, 1):
            res.append(COMMAND_CLASS.from_id(self._data[i]))

        return res
