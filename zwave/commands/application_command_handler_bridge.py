from . import DATA_FRAME, FRAME_TYPE_UNSOLICITED, FRAME_TYPE_ACK, uint8_t
from ..enums import application_command_handler_bridge
from .. import _utils


class ApplicationCommandHandlerBridge(DATA_FRAME):
    id = 0xA8
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK

    _fields_ = [
        ('_rx_status', uint8_t),
        ('_data', uint8_t * 256)
    ]

    rx_statuses = application_command_handler_bridge.unsolicited.rx_status

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._rx_status)

    @property
    def dst_node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @property
    def src_node_id(self) -> int:
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return (self._data[2] << 8) | self._data[3]

    @property
    def payload(self) -> bytearray:
        if self._node_id_len == 1:
            offset = 2
        else:
            offset = 4

        payload_len = self._data[offset]
        offset += 1

        res = bytearray(payload_len)

        for i in range(payload_len):
            res[i] = self._data[offset + i]

        return res

    @property
    def multicast_dest_node_masks(self) -> bytearray:
        if self._node_id_len == 1:
            offset = 2
        else:
            offset = 4

        payload_len = self._data[offset]
        offset += 2 + payload_len

        node_mask_len = self._data[offset]
        offset += 1

        res = bytearray(node_mask_len)

        for i in range(node_mask_len):
            res[i] = self._data[offset + i]

        return res

    @property
    def recv_rssi(self) -> str:
        if self._node_id_len == 1:
            offset = 2
        else:
            offset = 4

        payload_len = self._data[offset]
        offset += 2 + payload_len

        node_mask_len = self._data[offset]
        offset += 2 + node_mask_len

        return _utils.to_rssi(self._data[offset])
