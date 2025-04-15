from . import DATA_FRAME, FRAME_TYPE_REQUEST


class ZwWatchdogStart(DATA_FRAME):
    id = 0xD2
    frame_type = FRAME_TYPE_REQUEST

    @property
    def packet_length(self):
        return 0


