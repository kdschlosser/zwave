from . import CommandClass, CommandClassCommands


class AV_RENDERER_STATUS_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    GET = 0x01
    REPORT = 0x02


class COMMAND_CLASS_AV_RENDERER_STATUS(CommandClass):
    id = 0x96
    versions = [
        AV_RENDERER_STATUS_V1_COMMANDS
    ]


class ZW_AV_RENDERER_STATUS_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_AV_RENDERER_STATUS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = []



