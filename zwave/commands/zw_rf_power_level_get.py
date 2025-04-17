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


class FUNC_ZW_RF_POWER_LEVEL_GET_CMD(DATA_FRAME):
    """
    Get RF Power level
    """
    id = 0xBA
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_RF_POWER_LEVEL_GET_RSP(DATA_FRAME):
    id = 0xBA
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    @property
    def power_level(self):

