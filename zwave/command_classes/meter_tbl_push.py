# Meter Table Push Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_METER_TBL_PUSH = 0x3E

METER_TBL_PUSH_VERSION = 0x01
# Meter Table Push Configuration Set
METER_TBL_PUSH_CONFIGURATION_SET = 0x01
# Meter Table Push Configuration Get
METER_TBL_PUSH_CONFIGURATION_GET = 0x02
# Meter Table Push Configuration Report
METER_TBL_PUSH_CONFIGURATION_REPORT = 0x03

# Values used for Meter Tbl Push Configuration Report command
METER_TBL_PUSH_CONFIGURATION_REPORT_PROPERTIES1_OPERATING_STATUS_PUSH_MODE_MASK = 0x0F
METER_TBL_PUSH_CONFIGURATION_REPORT_PROPERTIES1_PS_BIT_MASK = 0x10
METER_TBL_PUSH_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
METER_TBL_PUSH_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05
# Values used for Meter Tbl Push Configuration Set command
METER_TBL_PUSH_CONFIGURATION_SET_PROPERTIES1_OPERATING_STATUS_PUSH_MODE_MASK = 0x0F
METER_TBL_PUSH_CONFIGURATION_SET_PROPERTIES1_PS_BIT_MASK = 0x10
METER_TBL_PUSH_CONFIGURATION_SET_PROPERTIES1_RESERVED_MASK = 0xE0
METER_TBL_PUSH_CONFIGURATION_SET_PROPERTIES1_RESERVED_SHIFT = 0x05



class ZW_METER_TBL_PUSH_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_TBL_PUSH_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('pushDataset1', uint8_t),
        ('pushDataset2', uint8_t),
        ('pushDataset3', uint8_t),
        ('intervalMonths', uint8_t),
        ('intervalDays', uint8_t),
        ('intervalHours', uint8_t),
        ('intervalMinutes', uint8_t),
        ('pushNodeId', uint8_t),
    ]


class ZW_METER_TBL_PUSH_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('pushDataset1', uint8_t),
        ('pushDataset2', uint8_t),
        ('pushDataset3', uint8_t),
        ('intervalMonths', uint8_t),
        ('intervalDays', uint8_t),
        ('intervalHours', uint8_t),
        ('intervalMinutes', uint8_t),
        ('pushNodeId', uint8_t),
    ]




