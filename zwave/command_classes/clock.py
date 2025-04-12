# Clock Command Class
# Application
# ==============================
COMMAND_CLASS_CLOCK = 0x81

CLOCK_VERSION = 0x01
# Clock Set
CLOCK_SET = 0x04
# Clock Get
CLOCK_GET = 0x05
# Clock Report
CLOCK_REPORT = 0x06

# Values used for Clock Report command
CLOCK_REPORT_LEVEL_HOUR_MASK = 0x1F
CLOCK_REPORT_LEVEL_WEEKDAY_MASK = 0xE0
CLOCK_REPORT_LEVEL_WEEKDAY_SHIFT = 0x05
CLOCK_REPORT_WEEKDAY_MONDAY = 0x01
CLOCK_REPORT_WEEKDAY_TUESDAY = 0x02
CLOCK_REPORT_WEEKDAY_WEDNESDAY = 0x03
CLOCK_REPORT_WEEKDAY_THURSDAY = 0x04
CLOCK_REPORT_WEEKDAY_FRIDAY = 0x05
CLOCK_REPORT_WEEKDAY_SATURDAY = 0x06
CLOCK_REPORT_WEEKDAY_SUNDAY = 0x07
# Values used for Clock Set command
CLOCK_SET_LEVEL_HOUR_MASK = 0x1F
CLOCK_SET_LEVEL_WEEKDAY_MASK = 0xE0
CLOCK_SET_LEVEL_WEEKDAY_SHIFT = 0x05
CLOCK_SET_WEEKDAY_MONDAY = 0x01
CLOCK_SET_WEEKDAY_TUESDAY = 0x02
CLOCK_SET_WEEKDAY_WEDNESDAY = 0x03
CLOCK_SET_WEEKDAY_THURSDAY = 0x04
CLOCK_SET_WEEKDAY_FRIDAY = 0x05
CLOCK_SET_WEEKDAY_SATURDAY = 0x06
CLOCK_SET_WEEKDAY_SUNDAY = 0x07






class ZW_CLOCK_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_CLOCK_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minute', uint8_t),
    ]


class ZW_CLOCK_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minute', uint8_t),
    ]


