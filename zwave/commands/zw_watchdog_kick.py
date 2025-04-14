from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_RESPONSE, FRAME_TYPE_CALLBACK, FRAME_TYPE_ACK, uint8_t


class ZwWatchdogKick(DATA_FRAME):
    id = 0xB8
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
    frame_type = FRAME_TYPE_CALLBACK | FRAME_TYPE_ACK

