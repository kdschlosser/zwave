
from . import CommandClass, CommandClassCommands

# Application Capability Command Class
# Management
# ==============================


class APPLICATION_CAPABILITY_V1_COMMANDS(CommandClassCommands):
    version = 0x01
    NOT_SUPPORTED = 0x01


class COMMAND_CLASS_APPLICATION_CAPABILITY(CommandClass):
    id = 0x57
    versions = [
        APPLICATION_CAPABILITY_V1_COMMANDS
    ]


# Values used for Command Command Class Not Supported command
COMMAND_COMMAND_CLASS_NOT_SUPPORTED_PROPERTIES1_RESERVED_MASK = 0x7F
COMMAND_COMMAND_CLASS_NOT_SUPPORTED_PROPERTIES1_DYNAMIC_BIT_MASK = 0x80

class ZW_COMMAND_COMMAND_CLASS_NOT_SUPPORTED_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('offendingCommandClass', uint8_t),
        ('offendingCommand', uint8_t),
    ]
