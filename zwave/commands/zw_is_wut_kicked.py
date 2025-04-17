"""
???
"""


from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_IS_WUT_KICKED_CMD(DATA_FRAME):
    """
    ???
    """
    id = 0xB5
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_IS_WUT_KICKED_RSP(DATA_FRAME):
    """
    ???
    """
    id = 0xB5
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_is_kicked', uint8_t)]

    @property
    def is_kicked(self) -> bool:
        return bool(self._is_kicked)
