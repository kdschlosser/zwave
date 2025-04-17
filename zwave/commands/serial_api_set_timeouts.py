from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_SERIAL_API_SET_TIMEOUTS_CMD(DATA_FRAME):
    """
    """
    id = 0x06
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_rx_ack_timeout', uint8_t),
        ('_rx_byte_timeout', uint8_t),
    ]

    @property
    def packet_length(self):
        return 2

    @property
    def rx_ack_timeout(self):
        return self._rx_ack_timeout * 10

    @rx_ack_timeout.setter
    def rx_ack_timeout(self, value):
        self._rx_ack_timeout = value // 10  # NOQA

    @property
    def rx_byte_timeout(self):
        return self._rx_byte_timeout * 10

    @rx_byte_timeout.setter
    def rx_byte_timeout(self, value):
        self._rx_byte_timeout = value // 10  # NOQA


class FUNC_SERIAL_API_SET_TIMEOUTS_RSP(DATA_FRAME):
    id = 0x06
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_old_rx_ack_timeout', uint8_t),
        ('_old_rx_byte_timeout', uint8_t),
    ]

    @property
    def old_rx_ack_timeout(self):
        return self._old_rx_ack_timeout * 10

    @old_rx_ack_timeout.setter
    def old_rx_ack_timeout(self, value):
        self._old_rx_ack_timeout = value // 10  # NOQA

    @property
    def old_rx_byte_timeout(self):
        return self._old_rx_byte_timeout * 10

    @old_rx_byte_timeout.setter
    def old_rx_byte_timeout(self, value):
        self._old_rx_byte_timeout = value // 10  # NOQA
