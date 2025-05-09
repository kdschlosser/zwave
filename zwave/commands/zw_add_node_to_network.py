"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    FRAME_TYPE_CALLBACK,
    uint8_t,
    uint32_t
)

from ..enums import add_node_to_network
from ..command_classes import COMMAND_CLASS
from .. import zw_types


class FUNC_ZW_ADD_NODE_TO_NETWORK_CMD(DATA_FRAME):
    """
    Add Node To Network Command

    This command is used to trigger a node inclusion to a Z-Wave network.
    """
    id = 0x4A
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_power', uint8_t, 1),
        ('_nwi', uint8_t, 1),
        ('_protocol', uint8_t, 1),
        ('_mode', uint8_t, 5),
        ('_session_id', uint8_t),
        ('_home_id', uint32_t),
        ('_auth_home_id', uint32_t),
    ]

    modes = add_node_to_network.command.mode

    @property
    def packet_length(self):
        return 10

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int):
        self._power = value  # NOQA

    @property
    def nwi(self) -> int:
        return self._nwi

    @nwi.setter
    def nwi(self, value: int):
        self._nwi = value  # NOQA

    @property
    def protocol(self) -> int:
        return self._protocol

    @protocol.setter
    def protocol(self, value: int):
        self._protocol = value  # NOQA

    @property
    def mode(self) -> modes:
        return self.modes(self._mode)

    @mode.setter
    def mode(self, value: modes):
        self._mode = value.value  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA

    @property
    def home_id(self) -> int:
        return (
            (self._home_id_1 << 24) |
            (self._home_id_2 << 16) |
            (self._home_id_3 << 8) |
            self._home_id_4
        )

    @home_id.setter
    def home_id(self, value: int):
        self._home_id_1 = (value >> 24) & 0xFF  # NOQA
        self._home_id_2 = (value >> 16) & 0xFF  # NOQA
        self._home_id_3 = (value >> 8) & 0xFF  # NOQA
        self._home_id_4 = value & 0xFF  # NOQA

    @property
    def auth_home_id(self) -> int:
        return (
            (self._auth_home_id_1 << 24) |
            (self._auth_home_id_2 << 16) |
            (self._auth_home_id_3 << 8) |
            self._auth_home_id_4
        )

    @auth_home_id.setter
    def auth_home_id(self, value: int):
        self._auth_home_id_1 = (value >> 24) & 0xFF  # NOQA
        self._auth_home_id_2 = (value >> 16) & 0xFF  # NOQA
        self._auth_home_id_3 = (value >> 8) & 0xFF  # NOQA
        self._auth_home_id_4 = value & 0xFF  # NOQA


class FUNC_ZW_ADD_NODE_TO_NETWORK_CB(DATA_FRAME):
    id = 0x4A
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t),
        ('_data', uint8_t * 256),
    ]

    statuses = add_node_to_network.callback.status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def node_id(self) -> int:
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
