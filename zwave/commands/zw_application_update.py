from . import (
    DATA_FRAME,
    FRAME_TYPE_ACK,
    FRAME_TYPE_UNSOLICITED,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint32_t,
    uint8_t
)

from ..enums import application_update
from ..command_classes import COMMAND_CLASS
from .. import zw_types


# this command is a bit tricky because it can be formatted 3 different ways.
class FUNC_ZW_APPLICATION_UPDATE_CMD(DATA_FRAME):
    """
    Get a list of supported (and controller) command classes
    """
    id = 0x49
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK
    min_bytes = 256

    _fields_ = [
        ('_event', uint8_t)
    ]

    events = application_update.unsolicited.event
    rx_statuses = application_update.unsolicited.rx_status

    @property
    def packet_length(self):
        return 0

    @property
    def _offset(self):
        if self._node_id_len == 1:
            return 1
        else:
            return 2

    @property
    def event(self) -> events:
        return self.events(self._event)

    @property
    def node_id(self) -> int:
        return self._fields.node_id


class _GenericNodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256)
    ]


class _GenericNodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256)
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _GenericNodeID8),
        ('_node_id_16', _GenericNodeID16),
    ]


class ZwApplicationUpdateGeneric(FUNC_ZW_APPLICATION_UPDATE_CMD):
    min_bytes = 10

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

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


class _SmartStartNodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('rx_status', uint8_t),
        ('home_id', uint32_t),
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256)
    ]


class _SmartStartNodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('rx_status', uint8_t),
        ('home_id', uint32_t),
        ('command_class_list_len', uint8_t),
        ('basic_type', uint8_t),
        ('generic_type', uint8_t),
        ('specific_type', uint8_t),
        ('command_classes', uint8_t * 256)
    ]


class _Fields2(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _SmartStartNodeID8),
        ('_node_id_16', _SmartStartNodeID16),
    ]


class ZwApplicationUpdateSmartStart(FUNC_ZW_APPLICATION_UPDATE_CMD):

    _fields_ = [('_anon_union', _Fields2)]
    _anonymous_ = ('_anon_union',)

    rx_statuses = FUNC_ZW_APPLICATION_UPDATE_CMD.rx_statuses

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._fields.rx_status)

    @property
    def nwi_home_id(self) -> int:
        return self._fields.home_id

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

    def __init__(self, *data):
        super().__init__(*data)

        if self.event not in (
            self.events.NodeInfoSmartstartHomeIDReceived,
            self.events.LRNodeInfoSmartstartHomeIDReceived
        ):
            raise ValueError


class _IncludeNodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('reserved', uint8_t),
        ('rx_status', uint8_t),
        ('home_id', uint32_t),
    ]


class _IncludeNodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('reserved', uint8_t),
        ('rx_status', uint8_t),
        ('home_id', uint32_t),
    ]


class _Fields3(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _IncludeNodeID8),
        ('_node_id_16', _IncludeNodeID16),
    ]


class ZwApplicationUpdateIncludeNode(FUNC_ZW_APPLICATION_UPDATE_CMD):

    _fields_ = [('_anon_union', _Fields3),]
    _anonymous_ = ('_anon_union',)

    rx_statuses = FUNC_ZW_APPLICATION_UPDATE_CMD.rx_statuses

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.event != self.events.IncludedNodeInfoReceived:
            raise ValueError

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._fields.rx_status)

    @property
    def nwi_home_id(self) -> int:
        return self._fields.home_id
