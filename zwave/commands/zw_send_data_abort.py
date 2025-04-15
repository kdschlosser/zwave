from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class ZwSendDataAbort(DATA_FRAME):
    id = 0x16
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
