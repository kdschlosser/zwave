from . import HOST_COMMAND, FRAME_TYPE_ACK


class SerialApiSoftReset(HOST_COMMAND):
    id = 0x08
    frame_type = FRAME_TYPE_ACK
