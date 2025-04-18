from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_EXPLORE_REQUEST_EXCLUSION_CMD(DATA_FRAME):
    """
    Initiate network wide exclusion while in learn mode
    """
    id = 0x5F
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_EXPLORE_REQUEST_EXCLUSION_RSP(DATA_FRAME):
    id = 0x5F
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_exclusion_request_status', uint8_t)
    ]

    @property
    def exclusion_request_status(self) -> bool:
        return bool(self._exclusion_request_status)
