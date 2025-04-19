"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

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


class FUNC_STORE_NODEINFO_CMD(DATA_FRAME):
    # TODO: Unclear what NODEINFO is
    """
    Can be used to restore protocol node information from a backup or
    the like. The format of the node info frame should be identical with the format used by
    ZW_GET_NODE_STATE.
    """
    id = 0x83
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id', uint8_t),
    ]

    @property
    def packet_length(self):
        return 0
