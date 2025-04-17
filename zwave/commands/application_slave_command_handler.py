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


class FUNC_APPLICATION_SLAVE_COMMAND_HANDLER_CMD(DATA_FRAME):
    """
    Slave command handler

    Not in Specification

    NOT USED
    """
    id = 0xA1
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
