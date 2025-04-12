from . import CommandClass, CommandClassCommands


# Basic Command Class
# ==============================
# Application


class BASIC_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    SET = 0x01
    GET = 0x02
    REPORT = 0x03


class BASIC_V2_COMMANDS(BASIC_V1_COMMANDS):
    version = 0x02


class COMMAND_CLASS_BASIC(CommandClass):
    id = 0x20
    versions = [
        BASIC_V1_COMMANDS,
        BASIC_V2_COMMANDS
    ]



class ZW_BASIC_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_BASIC_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


class ZW_BASIC_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


class ZW_BASIC_GET_V2_FRAME(ZW_BASIC_GET_FRAME):
    _fields_ = []


class ZW_BASIC_REPORT_V2_FRAME(ZW_BASIC_REPORT_FRAME):
    _fields_ = [
        ('currentValue', uint8_t),
        ('targetValue', uint8_t),
        ('duration', uint8_t),
    ]


class ZW_BASIC_SET_V2_FRAME(ZW_BASIC_SET_FRAME):
    _fields_ = []



