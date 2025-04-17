"""
Serial API Host Appl. Prg. Guide
INS12350
2022-12-01
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import set_lr_virtual_ids


class FUNC_ZW_SET_LR_VIRTUAL_IDS_CMD(DATA_FRAME):
    # TODO: get more information on this
    """
    Four Long Range node IDs are reserved for virtual nodes. IDs: 4002, 4003, 4004 and 4005. By default, all
    frames with virtual node IDs are rejected by Z-wave controllers. To accept application level frames with
    a virtual node ID, that node ID must be enabled.

    Command to enable virtual node IDs. Introduced in Serial API version 9.

    Notice: The command is not persistent. Must be re-issued after a reset or power-cycle of the Serial API
            Controller. I.e. the Host should subscribe to the Serial API started Command [7.16] to be notified of any
            Controller restart and re-issue the command accordingly.
    """

    id = 0xDD
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_node_ids', uint8_t)]

    nodes = set_lr_virtual_ids.command.node_ids

    @property
    def packet_length(self):
        return 1

    @property
    def node_ids(self) -> nodes:
        return self.lr_shadow(self._node_ids)

    @node_ids.setter
    def node_ids(self, value: nodes):
        self._node_ids = value.value  # NOQA
