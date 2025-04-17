from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_EXPLORE_REQUEST_INCLUSION_CMD(DATA_FRAME):
    """
    Initiate network wide inclusion while in learn mode
    """
    id = 0x5E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_EXPLORE_REQUEST_INCLUSION_RSP(DATA_FRAME):
    id = 0x5E
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_inclusion_request_status', uint8_t)
    ]

    @property
    def inclusion_request_status(self) -> bool:
        return bool(self._inclusion_request_status)
