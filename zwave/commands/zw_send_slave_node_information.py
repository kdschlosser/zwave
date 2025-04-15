from . import DATA_FRAME, FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from ..enums import send_slave_node_information


class ZwSendSlaveNodeInformation(DATA_FRAME):
    id = 0xA2
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_data', uint8_t * 6)
    ]

    options = send_slave_node_information.command.option

    @property
    def packet_length(self):
        return 0

    @property
    def src_node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @src_node_id.setter
    def src_node_id(self, value: int):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value << 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def dst_node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return (self._data[2] << 8) | self._data[3]

    @dst_node_id.setter
    def dst_node_id(self, value: int):
        if self._node_id_len == 1:
            self._data[1] = value
        else:
            self._data[2] = (value << 8) & 0xFF
            self._data[3] = value & 0xFF

    @property
    def option(self) -> options:
        if self._node_id_len == 1:
            return self.options(self._data[2])
        else:
            return self.options(self._data[4])

    @option.setter
    def option(self, value: options):
        if self._node_id_len == 1:
            self._data[2] = value.value  # NOQA
        else:
            self._data[4] = value.value  # NOQA

    @property
    def session_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[3]
        else:
            return self._data[5]

    @session_id.setter
    def session_id(self, value: int):
        if self._node_id_len == 1:
            self._data[3] = value  # NOQA
        else:
            self._data[5] = value  # NOQA


class ZwSendSlaveNodeInformationResponse(DATA_FRAME):
    id = 0xA2
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
    ]

    @property
    def status(self):
        return self._status


class ZwSendSlaveNodeInformationCallback(DATA_FRAME):
    id = 0xA2
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
        ('_original_node_id', uint8_t),
        ('_new_node_id', uint8_t),
    ]

    statuses = send_slave_node_information.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)
