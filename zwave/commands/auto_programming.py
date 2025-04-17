from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)



class EnterBootloader(DATA_FRAME):
    """
    Leave Serial API and enter bootloader (700+ series only).
    """
    id = 0x27
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_AUTO_PROGRAMMING_CMD(DATA_FRAME):
    """
    Leave Serial API and enter auto-programming mode (500 series only).
    """
    id = 0x27
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
