from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_SERIAL_API_EXT_CMD(DATA_FRAME):
    """
    Not in specification
    """
    id = 0x98
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
