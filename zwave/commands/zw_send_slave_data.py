from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_SEND_SLAVE_DATA_CMD(DATA_FRAME):
    """
    Not in specification

    Send data from slave
    """
    id = 0xA3
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
