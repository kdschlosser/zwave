# Door Lock Logging Command Class
# Application
# ==============================
COMMAND_CLASS_DOOR_LOCK_LOGGING = 0x4C

DOOR_LOCK_LOGGING_VERSION = 0x01
# Door Lock Logging Records Supported Get
DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET = 0x01
# Door Lock Logging Records Supported Report
DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT = 0x02
# Door Lock Logging Record Get
RECORD_GET = 0x03
# Door Lock Logging Record Report
RECORD_REPORT = 0x04

# Values used for Record Report command
RECORD_REPORT_PROPERTIES1_HOUR_LOCAL_TIME_MASK = 0x1F
RECORD_REPORT_PROPERTIES1_RECORD_STATUS_MASK = 0xE0
RECORD_REPORT_PROPERTIES1_RECORD_STATUS_SHIFT = 0x05



class ZW_DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('maxRecordsStored', uint8_t)]


class ZW_RECORD_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('recordNumber', uint8_t)]


class ZW_RECORD_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('recordNumber', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('properties1', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
        ('eventType', uint8_t),
        ('userIdentifier', uint8_t),
        ('userCodeLength', uint8_t),
        ('userCode1', uint8_t),
    ]

