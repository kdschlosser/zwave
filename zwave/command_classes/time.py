# Time Command Class
# Management
# ==============================
COMMAND_CLASS_TIME = 0x8A

TIME_VERSION = 0x01
# Time Get
TIME_GET = 0x01
# Time Report
TIME_REPORT = 0x02
# Date Get
DATE_GET = 0x03
# Date Report
DATE_REPORT = 0x04

# Values used for Time Report command
TIME_REPORT_PROPERTIES1_HOUR_LOCAL_TIME_MASK = 0x1F
TIME_REPORT_PROPERTIES1_RESERVED_MASK = 0x60
TIME_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05
TIME_REPORT_PROPERTIES1_RTC_FAILURE_BIT_MASK = 0x80

TIME_VERSION_V2 = 0x02
DATE_GET_V2 = 0x03
DATE_REPORT_V2 = 0x04
TIME_GET_V2 = 0x01
TIME_REPORT_V2 = 0x02
# Time Offset Set
TIME_OFFSET_SET_V2 = 0x05
# Time Offset Get
TIME_OFFSET_GET_V2 = 0x06
# Time Offset Report
TIME_OFFSET_REPORT_V2 = 0x07

# Values used for Time Offset Report command
TIME_OFFSET_REPORT_LEVEL_HOUR_TZO_MASK_V2 = 0x7F
TIME_OFFSET_REPORT_LEVEL_SIGN_TZO_BIT_MASK_V2 = 0x80
TIME_OFFSET_REPORT_LEVEL2_MINUTE_OFFSET_DST_MASK_V2 = 0x7F
TIME_OFFSET_REPORT_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V2 = 0x80
# Values used for Time Offset Set command
TIME_OFFSET_SET_LEVEL_HOUR_TZO_MASK_V2 = 0x7F
TIME_OFFSET_SET_LEVEL_SIGN_TZO_BIT_MASK_V2 = 0x80
TIME_OFFSET_SET_LEVEL2_MINUTE_OFFSET_DST_MASK_V2 = 0x7F
TIME_OFFSET_SET_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V2 = 0x80
# Values used for Time Report command
TIME_REPORT_PROPERTIES1_HOUR_LOCAL_TIME_MASK_V2 = 0x1F
TIME_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0x60
TIME_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x05
TIME_REPORT_PROPERTIES1_RTC_FAILURE_BIT_MASK_V2 = 0x80

class ZW_DATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_DATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
    ]


class ZW_TIME_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_TIME_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
    ]


class ZW_DATE_GET_V2_FRAME(ZW_DATE_GET_FRAME):
    _fields_ = []


class ZW_DATE_REPORT_V2_FRAME(ZW_DATE_REPORT_FRAME):
    _fields_ = []


class ZW_TIME_GET_V2_FRAME(ZW_TIME_GET_FRAME):
    _fields_ = []


class ZW_TIME_OFFSET_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_TIME_OFFSET_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minuteTzo', uint8_t),
        ('level2', uint8_t),
        ('monthStartDst', uint8_t),
        ('dayStartDst', uint8_t),
        ('hourStartDst', uint8_t),
        ('monthEndDst', uint8_t),
        ('dayEndDst', uint8_t),
        ('hourEndDst', uint8_t),
    ]


class ZW_TIME_OFFSET_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minuteTzo', uint8_t),
        ('level2', uint8_t),
        ('monthStartDst', uint8_t),
        ('dayStartDst', uint8_t),
        ('hourStartDst', uint8_t),
        ('monthEndDst', uint8_t),
        ('dayEndDst', uint8_t),
        ('hourEndDst', uint8_t),
    ]


class ZW_TIME_REPORT_V2_FRAME(ZW_TIME_REPORT_FRAME):
    _fields_ = []

