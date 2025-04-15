from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from .. import command_classes


class SerialApiApplNodeInformationCmdClasses(DATA_FRAME):
    id = 0x0C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_data', uint8_t * 256)]

    @property
    def packet_length(self):
        data_len = self._data[0] + 2
        data_len += self._data[data_len] + 1
        data_len += self._data[data_len]

        return data_len

    @property
    def not_included_command_classes(self) -> list[command_classes.COMMAND_CLASS]:
        return [
            command_classes.COMMAND_CLASS.from_id(item)
            for item in bytearray(self._data[1:self._data[0] + 1])
        ]

    @not_included_command_classes.setter
    def not_included_command_classes(self, value: list[command_classes.COMMAND_CLASS]):
        ns_included = self.non_securely_included_command_classes
        s_included = self.securely_included_command_classes

        for i, cc in enumerate(value):
            self._data[i + 1] = cc.id

        self._data[0] = len(value)  # NOQA

        self.non_securely_included_command_classes = ns_included
        self.securely_included_command_classes = s_included

    @property
    def non_securely_included_command_classes(self) -> list[command_classes.COMMAND_CLASS]:
        offset = self._data[0] + 1
        count = self._data[offset]
        offset += 1

        return [
            command_classes.COMMAND_CLASS.from_id(item)
            for item in bytearray(self._data[offset:offset + count])
        ]

    @non_securely_included_command_classes.setter
    def non_securely_included_command_classes(self, value: list[command_classes.COMMAND_CLASS]):
        s_included = self.securely_included_command_classes
        offset = self._data[0] + 1

        for i, cc in enumerate(value):
            self._data[offset + i + 1] = cc.id

        self._data[offset] = len(value)  # NOQA
        self.securely_included_command_classes = s_included

    @property
    def securely_included_command_classes(self) -> list[command_classes.COMMAND_CLASS]:
        offset = self._data[0] + 2
        offset += self._data[offset] + 1
        count = self._data[offset]
        offset += 1

        return [
            command_classes.COMMAND_CLASS.from_id(item)
            for item in bytearray(self._data[offset:offset + count])
        ]

    @securely_included_command_classes.setter
    def securely_included_command_classes(self, value: list[command_classes.COMMAND_CLASS]):
        offset = self._data[0] + 2
        offset += self._data[offset] + 1

        for i, cc in enumerate(value):
            self._data[offset + i + 1] = cc.id
        self._data[offset] = len(value)  # NOQA


class SerialApiApplNodeInformationCmdClassesResponse(DATA_FRAME):
    id = 0x0C

    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status

