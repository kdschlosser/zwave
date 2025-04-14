from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwClearNetworkStats(DATA_FRAME):
    id = 0x39
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class ZwClearNetworkStatsResponse(DATA_FRAME):
    id = 0x39
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self):
        return self._command_status
