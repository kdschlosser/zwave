from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_CLEAR_TX_TIMERS_CMD(DATA_FRAME):
    """
    Reset the Z-Wave module's internal TX timers
    """
    id = 0x37
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
