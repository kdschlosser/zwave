from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_INITIATE_SHUTDOWN_CMD(DATA_FRAME):
    """
    Instruct the Z-Wave API to shut down in order to safely remove the power
    """
    id = 0xD9
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_INITIATE_SHUTDOWN_RSP(DATA_FRAME):
    id = 0xD9
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def status(self) -> int:
        return self._status
