"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


from ..enums import is_node_within_direct_range


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_IS_NODE_WITHIN_DIRECT_RANGE_CMD(DATA_FRAME):
    """
    Is Node Within Direct Range Command

    This command is used to check if a given NodeID is marked as a direct range node (A node that can be
    reached with a direct range communication from a Z-Wave API module) in any of the existing return
    routes.
    """
    id = 0x5D
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    @property
    def packet_length(self):
        return self._node_id_len

    @property
    def node_id(self) -> int:
        return self._fields.node_id

    @node_id.setter
    def node_id(self, value: int):
        self._fields.node_id = value


class FUNC_ZW_IS_NODE_WITHIN_DIRECT_RANGE_RSP(DATA_FRAME):
    id = 0x5D
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_direct_range_status', uint8_t)
    ]

    direct_range_statuses = is_node_within_direct_range.response.direct_range_status

    @property
    def direct_range_status(self) -> direct_range_statuses:
        return self.direct_range_statuses(self._direct_range_status)
