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


class FUNC_ZW_SET_PROMISCUOUS_MODE_CMD(DATA_FRAME):
    """
    Set controller into promiscuous mode to listen to all messages
    """
    id = 0xD0
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
