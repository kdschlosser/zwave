from . import (
    DATA_FRAME,
    FRAME_TYPE_UNSOLICITED,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)

from ..enums import application_command_handler
from .. import _utils


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('payload_len', uint8_t),
        ('data', uint8_t * 256),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('payload_len', uint8_t),
        ('data', uint8_t * 256),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_APPLICATION_COMMAND_HANDLER_CMD(DATA_FRAME):
    id = 0x04
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK

    _fields_ = [
        ('_rx_status', uint8_t),
        ('_anon_union', _Fields)
    ]

    _anonymous_ = ('_anon_union',)

    rx_statuses = application_command_handler.unsolicited.rx_status

    @property
    def packet_length(self):
        return self._fields.payload_len + self._node_id_len + 2

    @property
    def rx_status(self) -> rx_statuses:
        return self.rx_statuses(self._rx_status)

    @property
    def node_id(self) -> int:
        return self._fields.node_id  # NOQA

    @property
    def payload(self) -> bytearray:
        res = bytearray(self._fields.payload_len)

        for i in range(self._fields.payload_len):
            res[i] = self._fields.data[i]

        return res

    @property
    def rx_rssi(self) -> str:
        index = self._fields.payload_len + 1
        return _utils.to_rssi(self._fields.data[index])
