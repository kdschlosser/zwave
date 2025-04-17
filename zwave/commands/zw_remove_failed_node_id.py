from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t,
)

from ..enums import remove_failed_node_id
from ..command_classes import COMMAND_CLASS
from .. import zw_types


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('session_id', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_REMOVE_FAILED_NODE_ID_CMD(DATA_FRAME):
    """
    Mark a specified node id as failed
    """
    id = 0x61
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len + 1

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class FUNC_ZW_REMOVE_FAILED_NODE_ID_RSP(DATA_FRAME):
    id = 0x61
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    statuses = remove_failed_node_id.response.status

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)


class FUNC_ZW_REMOVE_FAILED_NODE_ID_CB(DATA_FRAME):
    id = 0x61
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = remove_failed_node_id.callback.status

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
    def command_class_list_len(self):
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

        stop = start + self.command_class_list_len

        res = []

        for i in range(start, stop, 1):
            res.append(COMMAND_CLASS.from_id(self._data[i]))

        return res
