from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t
from ..enums import set_rf_receive_mode


class ZwSetRfReceiveMode(DATA_FRAME):
    id = 0x10
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_mode', uint8_t)]

    modes = set_rf_receive_mode.command.mode

    @property
    def mode(self) -> modes:
        return self.modes(self._mode)

    @mode.setter
    def mode(self, value: modes):
        self._modes = value.value  # NOQA


class ZwSetRfReceiveModeResponse(DATA_FRAME):
    id = 0x10
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    statuses = set_rf_receive_mode.response.status

    @property
    def status(self) -> statuses:
        return self._statuses(self._status)
