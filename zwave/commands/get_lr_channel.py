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
from ..enums import get_lr_channel


class FUNC_GET_LR_CHANNEL_CMD(DATA_FRAME):
    """
    There are 2 rf-channels available for Z-Wave Long Range communication. A controller can only use one
    frequency at a time. The host can use the commands below to get and set the active Long Range
    channel.
    """
    id = 0xDB
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_GET_LR_CHANNEL_CMD_RSP(DATA_FRAME):
    id = 0xDB
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_zwave_lr_channel', uint8_t)]

    long_range_channels = get_lr_channel.response.long_range

    @property
    def long_range_channel(self) -> long_range_channels:
        return self.long_range_channels(self._zwave_lr_channel)
