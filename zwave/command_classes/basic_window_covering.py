from . import CommandClass, CommandClassCommands


# Basic Window Covering Command Class
# Application
# ==============================


class BASIC_WINDOW_COVERING_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    START_LEVEL_CHANGE = 0x01
    STOP_LEVEL_CHANGE = 0x02


class COMMAND_CLASS_BASIC_WINDOW_COVERING(CommandClass):
    id = 0x50
    versions = [
        BASIC_WINDOW_COVERING_V1_COMMANDS
    ]


# Values used for Basic Window Covering Start Level Change command
BASIC_WINDOW_COVERING_START_LEVEL_CHANGE_LEVEL_RESERVED1_MASK = 0x3F
BASIC_WINDOW_COVERING_START_LEVEL_CHANGE_LEVEL_OPEN_CLOSE_BIT_MASK = 0x40
BASIC_WINDOW_COVERING_START_LEVEL_CHANGE_LEVEL_RESERVED2_BIT_MASK = 0x80




class ZW_BASIC_WINDOW_COVERING_START_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = []



