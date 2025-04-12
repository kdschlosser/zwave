from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums.host import get_lr_channel


class GetLRChannel(HOST_COMMAND):
    id = 0xDB
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class GetLRChannelResponse(HOST_RESPONSE):
    id = 0xDB

    _fields_ = [('_zwave_lr_channel', uint8_t)]

    long_range_channels = get_lr_channel.response.long_range

    @property
    def long_range_channel(self) -> long_range_channels:
        return self.long_range_channels(self._zwave_lr_channel)
