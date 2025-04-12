from . import HOST_COMMAND, HOST_RESPONSE, HOST_CALLBACK, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, uint8_t
from .. import _utils


class SendNOP(HOST_COMMAND):
    id = 0xE9
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE | FRAME_TYPE_CALLBACK

    _fields_ = [('_data', uint8_t * 5)]

    @property
    def destination_node_id(self):
        if self._node_id_len == 1:
            return self._data[0]
        else:
            return (self._data[0] << 8) | self._data[1]

    @destination_node_id.setter
    def destination_node_id(self, value):
        if self._node_id_len == 1:
            self._data[0] = value
        else:
            self._data[0] = (value >> 8) & 0xFF
            self._data[1] = value & 0xFF

    @property
    def tx_options(self):
        if self._node_id_len == 1:
            return self._data[1]
        else:
            return self._data[2]

    @tx_options.setter
    def tx_options(self, value):
        if self._node_id_len == 1:
            self._data[1] = value
        else:
            self._data[2] = value & 0xFF

    @property
    def session_id(self):
        if self._node_id_len == 1:
            return self._data[2]
        else:
            return self._data[3]

    @session_id.setter
    def session_id(self, value):
        if self._node_id_len == 1:
            self._data[2] = value
        else:
            self._data[3] = value


class SendNOPResponse(HOST_RESPONSE):
    id = 0xE9

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self):
        return self._response_status


class SendNOPCallback(HOST_CALLBACK):
    id = 0xE9

    _fields_ = [
        ('_session_id', uint8_t),
        ('tx_status', uint8_t),
        ('transmit_ticks_h', uint8_t),
        ('transmit_ticks_l', uint8_t),
        ('number_of_repeaters', uint8_t),
        ('ack_rssi', uint8_t),
        ('repeater0_rssi', uint8_t),
        ('repeater1_rssi', uint8_t),
        ('repeater2_rssi', uint8_t),
        ('repeater3_rssi', uint8_t),
        ('ack_channel_no', uint8_t),
        ('tx_channel_no', uint8_t),
        ('route_scheme_state', uint8_t),
        ('last_route_repeater_0', uint8_t),
        ('last_route_repeater_1', uint8_t),
        ('last_route_repeater_2', uint8_t),
        ('last_route_repeater_3', uint8_t),
        ('_reserved1', uint8_t, 1),
        ('beam_1000', uint8_t, 1),
        ('beam_250', uint8_t, 1),
        ('_reserved2', uint8_t, 2),
        ('last_route_speed', uint8_t, 3),
        ('routing_attempts', uint8_t),
        ('last_route_failed_functional_node_id', uint8_t),
        ('last_route_failed_non_functional_node_id', uint8_t),
        ('tx_power', uint8_t),
        ('measured_noise_floor', uint8_t),
        ('destination_ack_mpdu_tx_power', uint8_t),
        ('destination_ack_mpdu_measured_rssi', uint8_t),
        ('destination_ack_mpdu_measured_noise_floor', uint8_t)
    ]

    @property
    def transmit_ticks(self):
        return self._transmit_ticks_h << 8 | self._transmit_ticks_l

    @property
    def number_of_repeaters(self):
        return self._number_of_repeaters

    @property
    def ack_rssi(self):
        value = self._ack_rssi
        return _utils.to_rssi(value)

    @property
    def repeater0_rssi(self):
        value = self._repeater0_rssi
        return _utils.to_rssi(value)

    @property
    def repeater1_rssi(self):
        value = self._repeater1_rssi
        return _utils.to_rssi(value)

    @property
    def repeater2_rssi(self):
        value = self._repeater2_rssi
        return _utils.to_rssi(value)

    @property
    def repeater3_rssi(self):
        value = self._repeater3_rssi
        return _utils.to_rssi(value)

    @property
    def ack_channel_no(self):
        return self._ack_channel_no

    @property
    def tx_channel_no(self):
        return self._tx_channel_no

    @property
    def route_scheme_state(self):
        return self._route_scheme_state

    @property
    def last_route_repeater_0(self):
        return self._last_route_repeater_0

    @property
    def last_route_repeater_1(self):
        return self._last_route_repeater_1

    @property
    def last_route_repeater_2(self):
        return self._last_route_repeater_2

    @property
    def last_route_repeater_3(self):
        return self._last_route_repeater_3

    @property
    def beam_1000(self):
        return bool(self._beam_1000)

    @property
    def beam_250(self):
        return bool(self._beam_250)

    @property
    def last_route_speed(self):

        mapping = {
            0x00: 0.0,
            0x01: 9.6,
            0x02: 40.0,
            0x03: 100.0,
            0x04: 100.0,
        }
        return mapping[self._last_route_speed]

    @property
    def routing_attempts(self):
        return self._routing_attempts

    @property
    def last_route_failed_functional_node_id(self):
        return self._last_route_failed_functional_node_id

    @property
    def last_route_failed_non_functional_node_id(self):
        return self._last_route_failed_non_functional_node_id

    @property
    def tx_power(self):
        value = _utils.from_twos_complement( self._tx_power, 8)
        if value == 127:
            return None

        return value

    @property
    def measured_noise_floor(self):
        return _utils.to_rssi(self._measured_noise_floor)

    @property
    def destination_ack_mpdu_tx_power(self):
        value = _utils.from_twos_complement(self._destination_ack_mpdu_tx_power, 8)
        if value == 127:
            return None

        return value

    @property
    def destination_ack_mpdu_measured_rssi(self):
        return _utils.to_rssi(self._destination_ack_mpdu_measured_rssi)

    @property
    def destination_ack_mpdu_measured_noise_floor(self):
        return _utils.to_rssi(self._destination_ack_mpdu_measured_noise_floor)

