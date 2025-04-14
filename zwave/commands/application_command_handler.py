from . import DATA_FRAME, FRAME_TYPE_UNSOLICITED, uint8_t
from ..enums import application_command_handler

from .. import _utils


class ApplicationCommandHandler(DATA_FRAME):
    id = 0x04
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_rx_status', uint8_t),
        ('_data', uint8_t * 246)
    ]

    rx_statuses = application_command_handler.unsolicited.rx_status

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._rx_status)

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @property
    def __payload_len(self) -> int:
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return self._data[2]

    @property
    def payload(self) -> bytearray:
        res = bytearray(self.__payload_len)

        if self._node_id_len == 1:
            offset = 2
        else:
            offset = 3

        for i in range(self.__payload_len):
            res[i] = self._data[i + offset]

        return res

    @property
    def rx_rssi(self) -> str:
        if self._node_id_len == 1:
            offset = 2
        else:
            offset = 3

        offset += self.__payload_len

        return _utils.to_rssi(self._data[offset + 1])
