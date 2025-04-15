from . import DATA_FRAME, FRAME_TYPE_ACK, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, uint8_t
from ..enums import get_lr_channel


class GetLRChannel(DATA_FRAME):
    id = 0xDB
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class GetLRChannelResponse(DATA_FRAME):
    id = 0xDB
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_zwave_lr_channel', uint8_t)]

    long_range_channels = get_lr_channel.response.long_range

    @property
    def long_range_channel(self) -> long_range_channels:
        return self.long_range_channels(self._zwave_lr_channel)
