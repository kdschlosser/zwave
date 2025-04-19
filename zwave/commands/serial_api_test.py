from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_SERIAL_API_TEST_CMD(DATA_FRAME):
    """
    Not in specification
    """
    id = 0x95
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
