from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwGetNetworkStats(DATA_FRAME):
    id = 0x3A
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class ZwGetNetworkStatsResponse(DATA_FRAME):
    id = 0x3A
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_tx_frames_h', uint8_t),
        ('_tx_frames_l', uint8_t),
        ('_tx_lbt_backoffs_h', uint8_t),
        ('_tx_lbt_backoffs_l', uint8_t),
        ('_rx_frames_h', uint8_t),
        ('_rx_frames_l', uint8_t),
        ('_rx_checksum_errors_h', uint8_t),
        ('_rx_checksum_errors_l', uint8_t),
        ('_rx_crc16_errors_h', uint8_t),
        ('_rx_crc16_errors_l', uint8_t),
        ('_rx_foreign_home_id_h', uint8_t),
        ('_rx_foreign_home_id_l', uint8_t),
    ]

    @property
    def tx_frames(self) -> int:
        return (self._tx_frames_h << 8) | self._tx_frames_l

    @property
    def tx_lbt_backoffs(self) -> int:
        return (self._tx_lbt_backoffs_h << 8) | self._tx_lbt_backoffs_l

    @property
    def rx_frames(self) -> int:
        return (self._rx_frames_h << 8) | self._rx_frames_l

    @property
    def rx_checksum_errors(self) -> int:
        return (self._rx_checksum_errors_h << 8) | self._rx_checksum_errors_l

    @property
    def rx_crc16_errors(self) -> int:
        return (self._rx_crc16_errors_h << 8) | self._rx_crc16_errors_l

    @property
    def rx_foreign_home_id(self) -> int:
        return (self._rx_foreign_home_id_h << 8) | self._rx_foreign_home_id_l

