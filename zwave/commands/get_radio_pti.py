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


class GetRadioPTI(DATA_FRAME):
    """
    Radio debugging data. similiar to using a Zniffer
    """

    id = 0xE8
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
