from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwNetworkManagementSetMaxInclusionRequestIntervals(HOST_COMMAND):
    id = 0xD6
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [
        ('_requested_intervals', uint8_t)
    ]

    @property
    def requested_intervals(self) -> int:
        return self._requested_intervals

    @requested_intervals.setter
    def requested_intervals(self, value: int):
        self._requested_intervals = value  # NOQA


class ZwNetworkManagementSetMaxInclusionRequestIntervalsResponse(HOST_RESPONSE):
    id = 0xD6

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def command_status(self) -> int:
        return self._command_status
