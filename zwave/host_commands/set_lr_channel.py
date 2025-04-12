from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t

from ..enums.host import set_lr_channel


class SetLRChannel(HOST_COMMAND):
    id = 0xDC
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE

    _fields_ = [('_zwave_lr_channel', uint8_t)]

    long_range_channels = set_lr_channel.command.long_range

    @property
    def long_range_channel(self) -> long_range_channels:
        return self.long_range_channels(self._zwave_lr_channel)

    @long_range_channel.setter
    def long_range_channel(self, value: long_range_channels):
        self._zwave_lr_channel = value.value  # NOQA


class SetLRChannelResponse(HOST_RESPONSE):
    id = 0xDC

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self):
        return self._response_status
