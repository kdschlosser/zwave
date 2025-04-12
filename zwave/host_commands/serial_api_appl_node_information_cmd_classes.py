from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from .. import command_classes


class SerialApiApplNodeInformationCmdClasses(HOST_COMMAND):
    id = 0x0C
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_data', uint8_t * 256)]

    @property
    def not_included_command_classes(self) -> list[command_classes.COMMAND_CLASS]:
        res = []
        for i in range(self._data[0]):
            res.append(command_classes.COMMAND_CLASS.from_id(self._data[i + 1]))

        return res

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
        res = []
        offset = self._data[0] + 1
        count = self._data[offset]

        for i in range(offset, offset + count + 1):
            res.append(command_classes.COMMAND_CLASS.from_id(self._data[i + 1]))

        return res

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
        res = []
        offset = self._data[0] + 1
        offset += self._data[offset] + 1

        count = self._data[offset]

        for i in range(offset, offset + count + 1):
            res.append(command_classes.COMMAND_CLASS.from_id(self._data[i + 1]))

        return res

    @securely_included_command_classes.setter
    def securely_included_command_classes(self, value: list[command_classes.COMMAND_CLASS]):
        offset = self._data[0] + 1
        offset += self._data[offset] + 1

        for i, cc in enumerate(value):
            self._data[offset + i + 1] = cc.id

        self._data[offset] = len(value)  # NOQA


class SerialApiApplNodeInformationCmdClassesResponse(HOST_RESPONSE):
    id = 0x0C

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def is_ok(self):
        return bool(self._command_status)

