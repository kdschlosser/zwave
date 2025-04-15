from . import FRAME_TYPE_REQUEST, DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class ZwNetworkManagementSetMaxInclusionRequestIntervals(DATA_FRAME):
    id = 0xD6
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_requested_intervals', uint8_t)
    ]

    @property
    def packet_length(self):
        return 1

    @property
    def requested_intervals(self) -> int:
        return self._requested_intervals

    @requested_intervals.setter
    def requested_intervals(self, value: int):
        self._requested_intervals = value  # NOQA


class ZwNetworkManagementSetMaxInclusionRequestIntervalsResponse(DATA_FRAME):
    id = 0xD6
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def command_status(self) -> int:
        return self._command_status
