
from . import CommandClass, CommandClassCommands


# Association Command Configuration Command Class
# Management
# ==============================

class ASSOCIATION_COMMAND_CONFIGURATION_V1_COMMANDS(CommandClassCommands):
    version = 0x01
    RECORDS_SUPPORTED_GET = 0x01
    RECORDS_SUPPORTED_REPORT = 0x02
    CONFIGURATION_SET = 0x03
    CONFIGURATION_GET = 0x04
    CONFIGURATION_REPORT = 0x05

    SET_VALUES = []
    GET_VALUES = []
    REPORT_VALUES = []


class COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION(CommandClass):
    id = 0x9B
    versions = [
        ASSOCIATION_COMMAND_CONFIGURATION_V1_COMMANDS
    ]


# Values used for Command Configuration Report command
COMMAND_CONFIGURATION_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_MASK = 0x0F
COMMAND_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_MASK = 0x70
COMMAND_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x04
COMMAND_CONFIGURATION_REPORT_PROPERTIES1_FIRST_BIT_MASK = 0x80
# Values used for Command Records Supported Report command
COMMAND_RECORDS_SUPPORTED_REPORT_PROPERTIES1_CONF_CMD_BIT_MASK = 0x01
COMMAND_RECORDS_SUPPORTED_REPORT_PROPERTIES1_V_C_BIT_MASK = 0x02
COMMAND_RECORDS_SUPPORTED_REPORT_PROPERTIES1_MAX_COMMAND_LENGTH_MASK = 0xFC
COMMAND_RECORDS_SUPPORTED_REPORT_PROPERTIES1_MAX_COMMAND_LENGTH_SHIFT = 0x02






class ZW_COMMAND_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_COMMAND_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId', uint8_t),
        ('properties1', uint8_t),
        ('commandLength', uint8_t),
        ('commandClassIdentifier', uint8_t),
        ('commandIdentifier', uint8_t),
        ('commandByte1', uint8_t),
    ]


class ZW_COMMAND_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId', uint8_t),
        ('commandLength', uint8_t),
        ('commandClassIdentifier', uint8_t),
        ('commandIdentifier', uint8_t),
        ('commandByte1', uint8_t),
    ]





class ZW_COMMAND_RECORDS_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_COMMAND_RECORDS_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('freeCommandRecords1', uint8_t),
        ('freeCommandRecords2', uint8_t),
        ('maxCommandRecords1', uint8_t),
        ('maxCommandRecords2', uint8_t),
    ]


