from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK


class SerialApiSoftReset(DATA_FRAME):
    id = 0x08
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
