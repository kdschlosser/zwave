from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwGetNodeProtocolInfo(HOST_COMMAND):
    id = 0x41
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_node_id', uint8_t * 2)]

    @property
    def node_id(self):
        if self._node_id_len == 1:
            return self._node_id[0]
        else:
            return (self._node_id[0] << 8) | self._node_id[1]

    @node_id.setter
    def node_id(self, value):
        if self._node_id_len == 1:
            self._node_id[0] = value
        else:
            self._node_id[0] = (value >> 8) & 0xFF
            self._node_id[1] = value & 0xFF


class ZwGetNodeProtocolInfoResponse(HOST_RESPONSE):
    id = 0x41

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