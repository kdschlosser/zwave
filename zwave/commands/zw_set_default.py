"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_SET_DEFAULT_CMD(DATA_FRAME):
    """
    Set Default Command

    This command is used to set the Z-Wave API Module to its default state. It means that the Z-Wave API
    Module will leave its current network and erase all information related to its current Z-Wave network
    (topology, network keys, HomeID, etc.).
    """
    id = 0x42
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def packet_length(self):
        return 1

    @property
    def session_id(self) -> int:
        return self._session_id

    @session_id.setter
    def session_id(self, value: int):
        self._session_id = value  # NOQA


class FUNC_ZW_SET_DEFAULT_CB(DATA_FRAME):
    id = 0x42
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

    _fields_ = [('_session_id', uint8_t)]

    @property
    def session_id(self) -> int:
        return self._session_id
