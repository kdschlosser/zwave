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


class FUNC_ZW_NETWORK_MANAGEMENT_SET_MAX_INCLUSION_REQUEST_INTERVALS_CMD(DATA_FRAME):
    """
    Set the maximum interval between SmartStart inclusion requests
    """
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


class FUNC_ZW_NETWORK_MANAGEMENT_SET_MAX_INCLUSION_REQUEST_INTERVALS_RSP(DATA_FRAME):
    id = 0xD6
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_command_status', uint8_t)
    ]

    @property
    def command_status(self) -> int:
        return self._command_status
