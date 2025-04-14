from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK


class ClearTXTimers(DATA_FRAME):
    id = 0x37
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
