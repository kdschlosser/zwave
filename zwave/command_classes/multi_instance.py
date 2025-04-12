COMMAND_CLASS_MULTI_INSTANCE = 0x60  # [OBSOLETED]

MULTI_INSTANCE_VERSION = 0x01
MULTI_INSTANCE_CMD_ENCAP = 0x06
MULTI_INSTANCE_GET = 0x04
MULTI_INSTANCE_REPORT = 0x05



class ZW_MULTI_INSTANCE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('commandClass', uint8_t)]


class ZW_MULTI_INSTANCE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('commandClass', uint8_t),
        ('instances', uint8_t),
    ]


