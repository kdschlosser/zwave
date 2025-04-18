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
    uint8_t
)

from ..enums import set_rf_receive_mode


class FUNC_ZW_SET_RF_RECEIVE_MODE_CMD(DATA_FRAME):
    """
    Set RF Receive Mode Command

    This command is used to to power down the RF when not in use e.g., expects nothing to be received. It
    can also be used to set the RF into receive mode. This functionality is useful in battery powered Z-Wave
    nodes. The RF is automatic powered up when transmitting data.
    """
    id = 0x10
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_mode', uint8_t)]

    modes = set_rf_receive_mode.command.mode

    @property
    def packet_length(self):
        return 1

    @property
    def mode(self) -> modes:
        return self.modes(self._mode)

    @mode.setter
    def mode(self, value: modes):
        self._modes = value.value  # NOQA


class FUNC_ZW_SET_RF_RECEIVE_MODE_RSP(DATA_FRAME):
    id = 0x10
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    statuses = set_rf_receive_mode.response.status

    @property
    def status(self) -> statuses:
        return self._statuses(self._status)
