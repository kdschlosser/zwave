from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    FRAME_TYPE_CALLBACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)

from ..enums import remove_node_from_network
from ..command_classes import COMMAND_CLASS
from .. import zw_types


class ZwRemoveNodeFromNetwork(DATA_FRAME):
    id = 0x4B
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_power', uint8_t, 1),
        ('_nwi', uint8_t, 1),
        ('_protocol', uint8_t, 1),
        ('_mode', uint8_t, 5),
        ('_session_id', uint8_t)
    ]

    modes = remove_node_from_network.command.mode

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


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256),
    ]


class _ZwRemoveNodeFromNetworkCallbackFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class ZwRemoveNodeFromNetworkCallback(DATA_FRAME):
    id = 0x4B
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_status', uint8_t),
        ('_anon_union', _ZwRemoveNodeFromNetworkCallbackFields),
    ]

    _anonymous_ = ('_anon_union',)

    statuses = remove_node_from_network.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @property
    def basic_type(self) -> zw_types.BASIC_TYPE:
        return zw_types.BASIC_TYPE(self._fields.basic_type)

    @property
    def generic_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._fields.generic_type)

    @property
    def specific_type(self) -> zw_types.SPECIFIC_TYPES:
        return self.generic_type(self._fields.specific_type)

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        return [
            COMMAND_CLASS.from_id(self._fields.command_classes[i])
            for i in range(self._fields.command_class_list_len)
        ]
