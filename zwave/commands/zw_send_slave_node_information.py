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
    uint16_t
)

from ..enums import send_slave_node_information


class _NodeID8(NODE_ID_8_FRAME):

    _fields_ = [
        ('dst_node_id', uint8_t),
        ('tx_option', uint8_t),
        ('session_id', uint8_t),
    ]


class _NodeID16(NODE_ID_16_FRAME):
    _fields_ = [
        ('dst_node_id', uint16_t),
        ('tx_option', uint8_t),
        ('session_id', uint8_t),
    ]


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', _NodeID8),
        ('_node_id_16', _NodeID16),
    ]


class FUNC_ZW_SEND_SLAVE_NODE_INFORMATION_CMD(DATA_FRAME):
    """
    Send the NIF of a virtual node owned by the Z-Wave API module
    """
    id = 0xA2
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    tx_options = send_slave_node_information.command.tx_option

    @property
    def packet_length(self):
        return self._node_id_len * 2 + 2

    @property
    def src_node_id(self) -> int:
        return self._fields.node_id

    @src_node_id.setter
    def src_node_id(self, value: int):
        self._fields.node_id = value

    @property
    def dst_node_id(self) -> int:
        return self._fields.dst_node_id

    @dst_node_id.setter
    def dst_node_id(self, value: int):
        self._fields.dst_node_id = value

    @property
    def tx_option(self) -> tx_options:
        return self.tx_options(self._fields.tx_option)

    @tx_option.setter
    def tx_option(self, value: tx_options):
        self._fields.tx_option = value.value  # NOQA

    @property
    def session_id(self) -> int:
        return self._fields.session_id

    @session_id.setter
    def session_id(self, value: int):
        self._fields.session_id = value


class FUNC_ZW_SEND_SLAVE_NODE_INFO_RSP(DATA_FRAME):
    id = 0xA2
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response_status', uint8_t),
    ]

    @property
    def response_status(self):
        return self._response_status


class FUNC_ZW_SEND_SLAVE_NODE_INFO_CB(DATA_FRAME):
    id = 0xA2
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_tx_status', uint8_t),
    ]

    tx_statuses = send_slave_node_information.callback.tx_status

    @property
    def session_id(self):
        return self._session_id

    @property
    def tx_status(self) -> tx_statuses:
        return self.tx_statuses(self._tx_status)
