from . import (
    DATA_FRAME,
    FRAME_TYPE_UNSOLICITED,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


class FUNC_APPLICATION_SECURITY_EVENT_CMD(DATA_FRAME):
    """
    The protocol uses this function to notify the application of security events.

    This function is only required in slave_routing and slave_enhanced_232 based applications.

    (500 series)
    """

    id = 0x9D
    frame_type = FRAME_TYPE_UNSOLICITED | FRAME_TYPE_ACK

    _fields_ = [
        ('_event', uint8_t),
        ('_event_data_len', uint8_t),
        ('_event_data', uint8_t * 256)
    ]

    @property
    def packet_length(self):
        return 0

    @property
    def event(self) -> int:
        return self._event

    @property
    def event_data(self) -> bytearray:
        return bytearray(self._data[:self._event_data_len])