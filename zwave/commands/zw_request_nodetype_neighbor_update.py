from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK
)


class FUNC_ZW_REQUEST_NODETYPE_NEIGHBOR_UPDATE_CMD(DATA_FRAME):
    """
    Not in specification

    Used by the Z-Wave API module to request encryption of a Z-Wave protocol frame
    """
    id = 0x68
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0
