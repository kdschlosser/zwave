from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_SET_ROUTING_MAX_6_00_CMD(DATA_FRAME):
    """
    Not in specification
    """
    id = 0x65
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
