
from . import CommandClass, CommandClassCommands

# Application Status Command Class
# Management
# ==============================


class APPLICATION_STATUS_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    BUSY = 0x01
    REJECTED_REQUEST = 0x02

    BUSY_VALUES = [
        'Try Again Later',
        'Try Again In Wait Time Seconds',
        'Request Queued Executed Later'
    ]


class COMMAND_CLASS_APPLICATION_STATUS(CommandClass):
    id = 0x22
    versions = [
        APPLICATION_STATUS_V1_COMMANDS
    ]



class ZW_APPLICATION_BUSY_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('status', uint8_t),
        ('waitTime', uint8_t),
    ]


class ZW_APPLICATION_REJECTED_REQUEST_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('status', uint8_t)]


