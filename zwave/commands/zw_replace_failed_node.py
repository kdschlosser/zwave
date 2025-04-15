from . import DATA_FRAME, FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import replace_failed_node
from ..command_classes import COMMAND_CLASS
from .. import zw_types


class ZwReplaceFailedNode(DATA_FRAME):
    id = 0x63
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 3)
    ]

    @property
    def packet_length(self):
        return 0

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @node_id.setter
    def node_id(self, value):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value << 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def session_id(self):
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return self._data[2]

    @session_id.setter
    def session_id(self, value):
        if self._node_id_len == 1:
            self._data[1] = value  # NOQA
        else:
            self._data[2] = value  # NOQA


class ZwReplaceFailedNodeResponse(DATA_FRAME):
    id = 0x63
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    statuses = replace_failed_node.response.status

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)


class ZwReplaceFailedNodeCallback(DATA_FRAME):
    id = 0x63
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
    ]

    statuses = replace_failed_node.callback.status

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
