from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_RESERVED_SSD_CMD(DATA_FRAME):
    """
    Not in specification
    """
    id = 0xA7
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
