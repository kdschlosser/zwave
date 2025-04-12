

from . import CommandClass, CommandClassCommands


# Authentication Media Write Commmand Class
# Application
# ==============================


class AUTHENTICATION_MEDIA_WRITE_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    VERSION = 0x01
    GET = 0x01
    REPORT = 0x02
    START = 0x03
    STOP = 0x04
    STATUS = 0x05

    STATUS_VALUES = [
        'Operation Not Supported',
        'Forced Stop',
        'Timeout',
        'Another Operation Is Ongoing',
        'Aborted',
        'Proprietary Hex Data Restriction',
        'Non Rewritable Target',
        'Completed With No Status',
        'Success'
    ]


class COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE(CommandClass):
    id = 0xA2
    versions = [
        AUTHENTICATION_MEDIA_WRITE_V1_COMMANDS
    ]


# Values used for Authentication Media Capability Report command
AUTHENTICATION_MEDIA_CAPABILITY_REPORT_PROPERTIES1_DGS_BIT_MASK = 0x01
AUTHENTICATION_MEDIA_CAPABILITY_REPORT_PROPERTIES1_RESERVED1_MASK = 0xFE
AUTHENTICATION_MEDIA_CAPABILITY_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x01
# Values used for Authentication Media Write Start command
AUTHENTICATION_MEDIA_WRITE_START_PROPERTIES1_RESERVED1_MASK = 0x7F
AUTHENTICATION_MEDIA_WRITE_START_PROPERTIES1_GENERATE_DATA_BIT_MASK = 0x80
# Values used for Authentication Media Write Status command


class ZW_AUTHENTICATION_MEDIA_CAPABILITY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_AUTHENTICATION_MEDIA_CAPABILITY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_AUTHENTICATION_MEDIA_WRITE_START_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('timeout', uint8_t),
        ('properties1', uint8_t),
        ('dataLength', uint8_t),
        ('data1', uint8_t),
    ]


class ZW_AUTHENTICATION_MEDIA_WRITE_STOP_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_AUTHENTICATION_MEDIA_WRITE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('status', uint8_t),
        ('dataLength', uint8_t),
        ('data1', uint8_t),
    ]

