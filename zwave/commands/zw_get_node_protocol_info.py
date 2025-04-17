from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_GET_NODE_PROTOCOL_INFO_CMD(DATA_FRAME):
    """
    Get protocol info (baud rate, listening, etc.) for a given node
    """
    id = 0x41
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value


class FUNC_ZW_GET_NODE_PROTOCOL_INFO_RSP(DATA_FRAME):
    id = 0x41
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_listening', uint8_t, 1),
        ('_routing', uint8_t, 1),
        ('_supported_speed', uint8_t, 3),
        ('_protocol_version', uint8_t, 3),
        ('_optional_functionality', uint8_t, 1),
        ('_sensor_1000', uint8_t, 1),
        ('_sensor_250', uint8_t, 1),
        ('_beam_cap', uint8_t, 1),
        ('_routing_node', uint8_t, 1),
        ('_specific_device', uint8_t, 1),
        ('_controller_node', uint8_t, 1),
        ('_security', uint8_t, 1),
        ('_reserved', uint8_t, 5),
        ('_speed_extension', uint8_t, 3),
        ('_basic_device_type', uint8_t),
        ('_generic_device_class', uint8_t),
        ('_specific_device_class', uint8_t),
    ]
