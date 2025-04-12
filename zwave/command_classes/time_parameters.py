# Time Parameters Command Class
# Management
# ==============================
COMMAND_CLASS_TIME_PARAMETERS = 0x8B

TIME_PARAMETERS_VERSION = 0x01
# Time Parameters Set
TIME_PARAMETERS_SET = 0x01
# Time Parameters Get
TIME_PARAMETERS_GET = 0x02
# Time Parameters Report
TIME_PARAMETERS_REPORT = 0x03


class ZW_TIME_PARAMETERS_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_TIME_PARAMETERS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourUtc', uint8_t),
        ('minuteUtc', uint8_t),
        ('secondUtc', uint8_t),
    ]


class ZW_TIME_PARAMETERS_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourUtc', uint8_t),
        ('minuteUtc', uint8_t),
        ('secondUtc', uint8_t),
    ]
