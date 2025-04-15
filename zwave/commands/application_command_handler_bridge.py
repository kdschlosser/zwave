from . import (
    DATA_FRAME,
    FRAME_TYPE_UNSOLICITED,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t,
    uint16_t
)
from ..enums import application_command_handler_bridge
from .. import _utils


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('dst_node_id', uint8_t),
        ('payload_len', uint8_t),
        ('data', uint8_t * 256)
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('dst_node_id', uint16_t),
        ('payload_len', uint8_t),
        ('data', uint8_t * 256)

    ]


class _ApplicationCommandHandlerBridgeFields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16)
    ]


class ApplicationCommandHandlerBridge(DATA_FRAME):
    id = 0xA8
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK

    _fields_ = [
        ('_rx_status', uint8_t),
        ('_anon_union', _ApplicationCommandHandlerBridgeFields)
    ]

    _anonymous_ = ('_anon_union',)

    rx_statuses = application_command_handler_bridge.unsolicited.rx_status

    @property
    def packet_length(self):
        data_len = self._fields.payload_len + 1
        data_len += self._data[data_len] + 1
        data_len += self._node_id_len * 2
        data_len += 1
        return data_len

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._rx_status)

    @property
    def dst_node_id(self) -> int:
        return self._fields.node_id

    @property
    def src_node_id(self) -> int:
        return self._fields.src_node_id

    @property
    def payload(self) -> bytearray:
        return bytearray(self._fields.data[:self._fields.payload_len])

    @property
    def multicast_dest_node_masks(self) -> bytearray:
        payload_len = self._fields.payload_len
        offset = payload_len + 1
        node_mask_len = self._data[offset]
        offset += 1
        return bytearray(self._fields.data)[offset:offset + node_mask_len]

    @property
    def recv_rssi(self) -> str:
        offset = self._fields.payload_len + 1
        offset += self._data[offset] + 1
        return _utils.to_rssi(self._fields.data[offset])
