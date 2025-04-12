from . import CommandClass, CommandClassCommands


class AV_TAGGING_MD_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    GET = 0x01
    REPORT = 0x02


class COMMAND_CLASS_AV_TAGGING_MD(CommandClass):
    id = 0x99
    versions = [
        AV_TAGGING_MD_V1_COMMANDS
    ]


class ZW_AV_TAGGING_MD_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_AV_TAGGING_MD_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


