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
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)

from ..enums import set_learn_mode


class FUNC_ZW_SET_LEARN_MODE_CMD(DATA_FRAME):
    """
    Set Learn Mode Command

    This command is used to start or stop Learn Mode
    """
    id = 0x50
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_learn_mode', uint8_t),
        ('_session_id', uint8_t)
    ]

    learn_modes = set_learn_mode.command.learn_mode

    @property
    def packet_length(self):
        return 2

    @property
    def learn_mode(self) -> learn_modes:
        return self.learn_modes(self._learn_mode)

    @learn_mode.setter
    def learn_mode(self, value: learn_modes):
        self._learn_mode = value.value  # NOQA

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class FUNC_ZW_SET_LEARN_MODE_RSP(DATA_FRAME):
    id = 0x50
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self) -> int:
        return self._response_status


class _Fields(NODE_ID_FIELDS):
    _fields_ = [
        ('_node_id_8', NODE_ID_8_FRAME),
        ('_node_id_16', NODE_ID_16_FRAME),
    ]


class FUNC_ZW_SET_LEARN_MODE_CB(DATA_FRAME):
    id = 0x50
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [
        ('_session_id', uint8_t),
        ('_learn_mode_status', uint8_t),
        ('_anon_union', _Fields),
    ]

    _anonymous_ = ('_anon_union',)

    learn_mode_statuses = set_learn_mode.callback.learn_mode_status

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def learn_mode_status(self) -> learn_mode_statuses:
        return self.learn_mode_statuses(self._learn_mode_status)

    @property
    def node_id(self) -> int:
        return self._fields.node_id
