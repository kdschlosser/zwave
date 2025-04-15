from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t
from .. import _utils


class ZwSetListenBeforeTalkThreshold(DATA_FRAME):
    id = 0x3C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_channel', uint8_t),
        ('_rssi_thresh', uint8_t)
    ]

    @property
    def packet_length(self):
        return 0

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if value < 0 or value > 3:
            raise ValueError

        self._channel = value  # NOQA

    @property
    def rssi_thresh(self) -> str:
        return _utils.to_rssi(self._rssi_thresh)

    @rssi_thresh.setter
    def rssi_thresh(self, value: int | str):
        if isinstance(value, str):
            value = value.replace('dBm', '')
            value = int(value)

        if value < 0:
            value += 128

        self._rssi_thresh = value  # NOQA


class ZwSetListenBeforeTalkThresholdResponse(DATA_FRAME):
    id = 0x3C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def is_accpeted(self) -> bool:
        return bool(self._status)
