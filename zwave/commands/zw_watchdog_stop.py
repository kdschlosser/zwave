from . import DATA_FRAME, FRAME_TYPE_REQUEST


class ZwWatchdogStop(DATA_FRAME):
    id = 0xD3
    frame_type = FRAME_TYPE_REQUEST

