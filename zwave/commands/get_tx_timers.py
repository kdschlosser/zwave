from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t


class GetTXTimers(DATA_FRAME):
    id = 0x38
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class GetTXTimersResponse(DATA_FRAME):
    id = 0x38
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_tx_timer_ch0', uint8_t),
        ('_tx_timer_ch1', uint8_t),
        ('_tx_timer_ch2', uint8_t),
    ]

    @property
    def tx_timer_ch0(self):
        return self._tx_timer_ch0

    @property
    def tx_timer_ch1(self):
        return self._tx_timer_ch1

    @property
    def tx_timer_ch2(self):
        return self._tx_timer_ch2
