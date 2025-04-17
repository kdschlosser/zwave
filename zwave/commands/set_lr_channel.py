"""
Serial API Host Appl. Prg. Guide
INS12350
2022-12-01
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import set_lr_channel


class FUNC_SET_LR_CHANNEL_CMD(DATA_FRAME):
    """
    Command to set the active Long Range rf-channel. Introduced in Serial API version 9.
    """
    id = 0xDC
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_zwave_lr_channel', uint8_t)]

    long_range_channels = set_lr_channel.command.long_range

    @property
    def packet_length(self):
        return 1

    @property
    def long_range_channel(self) -> long_range_channels:
        return self.long_range_channels(self._zwave_lr_channel)

    @long_range_channel.setter
    def long_range_channel(self, value: long_range_channels):
        self._zwave_lr_channel = value.value  # NOQA


class FUNC_SET_LR_CHANNEL_RSP(DATA_FRAME):
    id = 0xDC
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_response_status', uint8_t)]

    @property
    def response_status(self):
        return self._response_status
