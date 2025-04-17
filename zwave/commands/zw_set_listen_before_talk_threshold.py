from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import set_listen_before_talk_threshold
from .. import _utils


class ZwSetListenBeforeTalkThreshold(DATA_FRAME):
    """
    Set the RSSI threshold above which the stick will not transmit
    """
    id = 0x3C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_channel', uint8_t),
        ('_rssi_thresh', uint8_t)
    ]

    channels = set_listen_before_talk_threshold.command.channel

    @property
    def packet_length(self):
        return 2

    @property
    def channel(self) -> channels:
        return self.channels(self._channel)

    @channel.setter
    def channel(self, value: channels):
        self._channel = value.value  # NOQA

    @property
    def rssi_thresh(self) -> str:
        return _utils.to_rssi(self._rssi_thresh)

    @rssi_thresh.setter
    def rssi_thresh(self, value: int | str):
        self._rssi_thresh = _utils.from_rssi(value)  # NOQA


class ZwSetListenBeforeTalkThresholdResponse(DATA_FRAME):
    id = 0x3C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_status', uint8_t)]

    @property
    def is_accpeted(self) -> bool:
        return bool(self._status)
