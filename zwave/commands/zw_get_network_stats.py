"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint16_t
)


class FUNC_ZW_GET_NETWORK_STATS_CMD(DATA_FRAME):
    """
    Get Network Statistics Command

    This command is used to request the current Network Statistics as collected by a library runs on the Z-
    Wave Module. It is expected that the library will continuously update any Network Statistics counter
    until it reaches 65535, which then indicates that the specific counter has reached 65535 or more occur-
    rences. The Network Statistics counters shall be cleared either on module startup, or by receiving Clear
    Network Statistics Command.
    """
    id = 0x3A
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_NETWORK_STATS_RSP(DATA_FRAME):
    id = 0x3A
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_tx_frames', uint16_t),
        ('_tx_lbt_backoffs', uint16_t),
        ('_rx_frames', uint16_t),
        ('_rx_checksum_errors', uint16_t),
        ('_rx_crc16_errors', uint16_t),
        ('_rx_foreign_home_id', uint16_t),
    ]

    @property
    def tx_frames(self) -> int:
        return self._tx_frames

    @property
    def tx_lbt_backoffs(self) -> int:
        return self._tx_lbt_backoffs

    @property
    def rx_frames(self) -> int:
        return self._rx_frames

    @property
    def rx_checksum_errors(self) -> int:
        return self._rx_checksum_errors

    @property
    def rx_crc16_errors(self) -> int:
        return self._rx_crc16_errors

    @property
    def rx_foreign_home_id(self) -> int:
        return self._rx_foreign_home_id
