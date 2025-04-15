from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, uint8_t
from ..enums import set_lr_virtual_ids


class ZwSetLrVirtualIds(DATA_FRAME):
    id = 0xDD
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_node_ids', uint8_t)]

    nodes = set_lr_virtual_ids.command.node_ids

    @property
    def packet_length(self):
        return 0

    @property
    def node_ids(self) -> nodes:
        return self.lr_shadow(self._node_ids)

    @node_ids.setter
    def node_ids(self, value: nodes):
        self._node_ids = value.value  # NOQA
