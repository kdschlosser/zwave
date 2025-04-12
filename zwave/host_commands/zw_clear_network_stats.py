from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwClearNetworkStats(HOST_COMMAND):
    id = 0x39
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class ZwClearNetworkStatsResponse(HOST_RESPONSE):
    id = 0x39

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self):
        return self._command_status
