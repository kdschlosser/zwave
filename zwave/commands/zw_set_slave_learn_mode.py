"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import set_slave_learn_mode


class FUNC_ZW_SET_SLAVE_LEARN_MODE_CMD(DATA_FRAME):
    """
    Set Virtual Node To Learn Mode Command

    This command is used to enable or disable a virtual end node to Learn Mode operation that facilitates
    the node to be included or removed to/from a Z-Wave Network.
    """
    id = 0xA4
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_node_id', uint8_t),
        ('_mode', uint8_t),
        ('_session_id', uint8_t),
    ]

    modes = set_slave_learn_mode.command.mode

    @property
    def packet_length(self):
        return 3

    @property
    def node_id(self) -> int:
        return self._node_id

    @node_id.setter
    def node_id(self, value: int):
        self._node_id = value  # NOQA

    @property
    def mode(self) -> modes:
        return self.modes(self._mode)

    @mode.setter
    def mode(self, value: modes):
        self._mode = value.value  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class FUNC_ZW_SET_SLAVE_LEARN_MODE_RSP(DATA_FRAME):
    id = 0xA4
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_response_status', uint8_t),
    ]

    @property
    def response_status(self):
        return self._response_status


class FUNC_ZW_SET_SLAVE_LEARN_MODE_CB(DATA_FRAME):
    id = 0xA4
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_sesion_id', uint8_t),
        ('_status', uint8_t),
        ('_original_node_id', uint8_t),
        ('_new_node_id', uint8_t),
    ]

    statuses = set_slave_learn_mode.callback.status

    @property
    def session_id(self):
        return self._session_id

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def original_node_id(self) -> int:
        return self._original_node_id

    @property
    def new_node_id(self) -> int:
        return self._new_node_id
