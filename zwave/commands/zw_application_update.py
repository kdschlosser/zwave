from . import DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_UNSOLICITED, uint8_t
from ..enums import application_update
from ..command_classes import COMMAND_CLASS
from .. import zw_types


# this command is a bit tricky because it can be formatted 3 different ways.


class ZwApplicationUpdate(DATA_FRAME):
    id = 0x49
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK
    min_bytes = 256

    _fields_ = [
        ('_event', uint8_t),
        ('_data', uint8_t * 256)
    ]

    events = application_update.unsolicited.event
    rx_statuses = application_update.unsolicited.rx_status

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
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    def __init__(self, command, event, node_id):
        super().__init__(command=command)


class ZwApplicationUpdateGeneric(ZwApplicationUpdate):
    min_bytes = 10

    @property
    def __command_class_list_len(self) -> int:
        return self._data[self._offset]

    @property
    def basic_type(self) -> zw_types.BASIC_TYPE:
        return zw_types.BASIC_TYPE(self._data[self._offset + 1])

    @property
    def generic_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._data[self._offset + 2])

    @property
    def specific_type(self) -> zw_types.SPECIFIC_TYPES:
        return self.generic_type(self._data[self._offset + 3])

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        offset = self._offset + 4
        res = []

        for i in range(self.__command_class_list_len):
            res.append(COMMAND_CLASS.from_id(self._data[i + offset]))

        return res



class ZwApplicationUpdateSmartStart(ZwApplicationUpdate):
    min_bytes = 10

    rx_statuses = ZwApplicationUpdate.rx_statuses

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._data[self._offset])

    @property
    def nwi_home_id(self) -> int:
        offset = self._offset + 1

        return (
            (self._data[offset] << 24) |
            (self._data[offset + 1] << 16) |
            (self._data[offset + 2] << 8) |
            self._data[offset + 3]
        )

    @property
    def __command_class_list_len(self) -> int:
        return self._data[self._offset + 5]

    @property
    def basic_type(self) -> zw_types.BASIC_TYPE:
        return zw_types.BASIC_TYPE(self._data[self._offset + 6])

    @property
    def generic_type(self) -> zw_types.GENERIC_TYPE:
        return zw_types.GENERIC_TYPE(self._data[self._offset + 7])

    @property
    def specific_type(self) -> zw_types.SPECIFIC_TYPES:
        return self.generic_type(self._data[self._offset + 8])

    @property
    def command_classes(self) -> list[COMMAND_CLASS]:
        offset = self._offset + 9
        res = []

        for i in range(self.__command_class_list_len):
            res.append(COMMAND_CLASS.from_id(self._data[i + offset]))

        return res

    def __init__(self, *data):
        super().__init__(*data)

        if self.event not in (
            self.events.NodeInfoSmartstartHomeIDReceived,
            self.events.LRNodeInfoSmartstartHomeIDReceived
        ):
            raise ValueError


class ZwApplicationUpdateIncludeNode(ZwApplicationUpdate):
    min_bytes = 10

    rx_statuses = ZwApplicationUpdate.rx_statuses

    def __init__(self, *data):
        super().__init__(*data)

        if self.event != self.events.IncludedNodeInfoReceived:
            raise ValueError

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._data[self._offset + 1])

    @property
    def nwi_home_id(self) -> int:
        offset = self._offset + 2

        return (
            (self._data[offset] << 24) |
            (self._data[offset + 1] << 16) |
            (self._data[offset + 2] << 8) |
            self._data[offset + 3]
        )


