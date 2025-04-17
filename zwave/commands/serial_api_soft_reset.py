from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
)


class FUNC_SERIAL_API_SOFT_RESET_CMD(DATA_FRAME):
    """
    """
    id = 0x08
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
