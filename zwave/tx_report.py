import ctypes
from . import _utils

uint8_t = ctypes.c_uint8


class TXReport(ctypes.Structure):
    _fields_ = [
        ('_transmit_ticks_h', uint8_t),
        ('_transmit_ticks_l', uint8_t),
        ('_repeaters', uint8_t),
        ('_ack_rssi', uint8_t),
        ('_repeater_0_rssi', uint8_t),
        ('_repeater_1_rssi', uint8_t),
        ('_repeater_2_rssi', uint8_t),
        ('_repeater_3_rssi', uint8_t),
        ('_ack_channel_no', uint8_t),
        ('_tx_channel_no', uint8_t),
        ('_route_scheme_state', uint8_t),
        ('_repeater_0', uint8_t),
        ('_repeater_1', uint8_t),
        ('_repeater_2', uint8_t),
        ('_repeater_3', uint8_t),
        ('_reserved1', uint8_t, 1),
        ('_beam1000', uint8_t, 1),
        ('_beam250', uint8_t, 1),
        ('_reserved2', uint8_t, 2),
        ('_last_route_speed', uint8_t, 3),
        ('_routing_attempts', uint8_t),
        ('_functional_node_id', uint8_t),
        ('_non_functional_node_id', uint8_t),
        ('_tx_power', uint8_t),
        ('_noise_floor', uint8_t),
        ('_mpdu_tx_power', uint8_t),
        ('_mpdu_rssi', uint8_t),
        ('_mpdu_noise_floor', uint8_t)
    ]

    @property
    def ticks(self) -> int:
        return ((
                    self._transmit_ticks_h << 8) | self._transmit_ticks_l) * 10

    @property
    def number_of_repeaters(self) -> int:
        return self._repeaters

    @property
    def ack_rssi(self) -> str:
        return _utils.to_rssi(self._ask_rssi)

    @property
    def repeater_0_rssi(self) -> str:
        return _utils.to_rssi(self._repeater_0_rssi)

    @property
    def repeater_1_rssi(self) -> str:
        return _utils.to_rssi(self._repeater_1_rssi)

    @property
    def repeater_2_rssi(self) -> str:
        return _utils.to_rssi(self._repeater_2_rssi)

    @property
    def repeater_3_rssi(self) -> str:
        return _utils.to_rssi(self._repeater_3_rssi)

    @property
    def ack_channel_no(self) -> int:
        return self._ack_channel_no

    @property
    def tx_channel_no(self) -> int:
        return self.tx_channel_no

    @property
    def route_scheme_state(self) -> int:
        return self._route_scheme_state

    @property
    def repeater_0(self) -> int:
        return self._repeater_0

    @property
    def repeater_1(self) -> int:
        return self._repeater_1

    @property
    def repeater_2(self) -> int:
        return self._repeater_2

    @property
    def repeater_3(self) -> int:
        return self._repeater_3

    @property
    def beam1000(self) -> bool:
        return bool(self._beam1000)

    @property
    def beam250(self) -> bool:
        return bool(self._beam250)

    @property
    def last_route_speed(self) -> int:
        return self._last_route_speed

    @property
    def routing_attempts(self) -> int:
        return self._routing_attempts

    @property
    def functional_node_id(self) -> int:
        return self._functional_node_id

    @property
    def non_functional_node_id(self) -> int:
        return self._non_functional_node_id

    @property
    def tx_power(self) -> int:
        return self._tx_power

    @property
    def noise_floor(self) -> int:
        return self._noise_floor

    @property
    def mpdu_tx_power(self) -> int:
        return self._mpdu_tx_power

    @property
    def mpdu_rssi(self) -> str:
        return _utils.to_rssi(self._mpdu_rssi)

    @property
    def mpdu_noise_floor(self) -> int:
        return self._mpdu_noise_floor
