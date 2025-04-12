import ctypes


uint8_t = ctypes.c_uint8

FRAME_TYPE_NOACK = 0x00
FRAME_TYPE_ACK = 0x01
FRAME_TYPE_RESPONSE = 0x02
FRAME_TYPE_CALLBACK = 0x04
FRAME_TYPE_UNSOLICITED = 0x08


class HOST_COMMAND(ctypes.Structure):
    id = 0x00
    frame_type = FRAME_TYPE_UNSOLICITED


class HOST_RESPONSE(ctypes.Structure):
    id = 0x00

