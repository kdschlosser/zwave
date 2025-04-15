from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_ACK, uint8_t
from .. import _utils


class ZwGetBackgroundRssi(DATA_FRAME):
    id = 0x3B
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class ZwGetBackgroundRssiResponse(DATA_FRAME):
    id = 0x3B
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_rssi_ch0', uint8_t),
        ('_rssi_ch1', uint8_t),
        ('_rssi_ch2', uint8_t),
    ]

    @property
    def rssi_ch0(self):
        return _utils.to_rssi(self._rssi_ch0)

    @property
    def rssi_ch1(self):
        return _utils.to_rssi(self._rssi_ch1)

    @property
    def rssi_ch2(self):
        return _utils.to_rssi(self._rssi_ch2)
