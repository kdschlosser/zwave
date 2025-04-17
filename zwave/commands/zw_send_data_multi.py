

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


class FUNC_ZW_SEND_DATA_MULTI_CMD(DATA_FRAME):
    """
    Send data using multicast
    """
    id = 0x14
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_anon_union', _Fields)]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return 0



