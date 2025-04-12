# Schedule Entry Lock Command Class
# Application
# ==============================
COMMAND_CLASS_SCHEDULE_ENTRY_LOCK = 0x4E


SCHEDULE_ENTRY_LOCK_VERSION = 0x01
# Schedule Entry Lock Enable Set
SCHEDULE_ENTRY_LOCK_ENABLE_SET = 0x01
# Schedule Entry Lock Enable All Set
SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET = 0x02
# Schedule Entry Lock Week Day Schedule Set
SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET = 0x03
# Schedule Entry Lock Week Days Schedule Get
SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET = 0x04
# Schedule Entry Lock Week Day Schedule Report
SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT = 0x05
# Schedule Entry Lock Year Day Schedule Set
SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET = 0x06
# Schedule Entry Lock Year Day Schedule Get
SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET = 0x07
# Schedule Entry Lock Year Day Schedule Report
SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT = 0x08
# Schedule Entry Lock Supported Get
SCHEDULE_ENTRY_TYPE_SUPPORTED_GET = 0x09
# Schedule Entry Lock Supported Report
SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT = 0x0A


SCHEDULE_ENTRY_LOCK_VERSION_V2 = 0x02
SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V2 = 0x02
SCHEDULE_ENTRY_LOCK_ENABLE_SET_V2 = 0x01
SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V2 = 0x04
SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V2 = 0x05
SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V2 = 0x03
SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V2 = 0x07
SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V2 = 0x08
SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V2 = 0x06
SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V2 = 0x09
SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V2 = 0x0A
# Schedule Entry Lock Time Offset Get
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V2 = 0x0B
# Schedule Entry Lock Time Offset Report
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V2 = 0x0C
# Schedule Entry Lock Time Offset Set
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V2 = 0x0D


# Values used for Schedule Entry Lock Time Offset Report command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_HOUR_TZO_MASK_V2 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_SIGN_TZO_BIT_MASK_V2 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_MINUTE_OFFSET_DST_MASK_V2 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V2 = 0x80
# Values used for Schedule Entry Lock Time Offset Set command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_HOUR_TZO_MASK_V2 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_SIGN_TZO_BIT_MASK_V2 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_MINUTE_OFFSET_DST_MASK_V2 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V2 = 0x80

SCHEDULE_ENTRY_LOCK_VERSION_V3 = 0x03
SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V3 = 0x02
SCHEDULE_ENTRY_LOCK_ENABLE_SET_V3 = 0x01
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V3 = 0x0B
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V3 = 0x0C
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V3 = 0x0D
SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V3 = 0x04
SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V3 = 0x05
SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V3 = 0x03
SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V3 = 0x07
SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V3 = 0x08
SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V3 = 0x06
SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V3 = 0x09
SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V3 = 0x0A
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V3 = 0x0E
# Schedule Entry Lock Daily Repeating Report
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V3 = 0x0F
# Schedule Entry Lock Daily Repeating Set
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V3 = 0x10


# Values used for Schedule Entry Lock Time Offset Report command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_HOUR_TZO_MASK_V3 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_SIGN_TZO_BIT_MASK_V3 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_MINUTE_OFFSET_DST_MASK_V3 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V3 = 0x80
# Values used for Schedule Entry Lock Time Offset Set command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_HOUR_TZO_MASK_V3 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_SIGN_TZO_BIT_MASK_V3 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_MINUTE_OFFSET_DST_MASK_V3 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V3 = 0x80

SCHEDULE_ENTRY_LOCK_VERSION_V4 = 0x04
SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V4 = 0x02
SCHEDULE_ENTRY_LOCK_ENABLE_SET_V4 = 0x01
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V4 = 0x0B
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V4 = 0x0C
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V4 = 0x0D
SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V4 = 0x04
SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V4 = 0x05
SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V4 = 0x03
SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V4 = 0x07
SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V4 = 0x08
SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V4 = 0x06
SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V4 = 0x09
SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V4 = 0x0A
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V4 = 0x0E
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V4 = 0x0F
SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V4 = 0x10
EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V4 = 0x11
EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET_V4 = 0x12
EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET_V4 = 0x13
EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_REPORT_V4 = 0x14
EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET_V4 = 0x15
EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET_V4 = 0x16
EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_REPORT_V4 = 0x17
EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V4 = 0x18
EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V4 = 0x19
EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V4 = 0x1A
# Values used for Schedule Entry Lock Time Offset Report command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_HOUR_TZO_MASK_V4 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL_SIGN_TZO_BIT_MASK_V4 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_MINUTE_OFFSET_DST_MASK_V4 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V4 = 0x80
# Values used for Schedule Entry Lock Time Offset Set command
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_HOUR_TZO_MASK_V4 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL_SIGN_TZO_BIT_MASK_V4 = 0x80
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_MINUTE_OFFSET_DST_MASK_V4 = 0x7F
SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_LEVEL2_SIGN_OFFSET_DST_BIT_MASK_V4 = 0x80
# Values used for Extended Schedule Entry Lock Enable Set command
EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET_PROPERTIES1_ENABLED_BIT_MASK_V4 = 0x01
EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET_PROPERTIES1_RESERVED_MASK_V4 = 0xFE
EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET_PROPERTIES1_RESERVED_SHIFT_V4 = 0x01


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('enabled', uint8_t)]


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('enabled', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('dayOfWeek', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('dayOfWeek', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('startYear', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopYear', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('startYear', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopYear', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfSlotsWeekDay', uint8_t),
        ('numberOfSlotsYearDay', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minuteTzo', uint8_t),
        ('level2', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('minuteTzo', uint8_t),
        ('level2', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V2_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V2_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V2_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V3_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V3_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V3_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = [('numberOfSlotsDailyRepeating', uint8_t)]


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('weekDayBitmask', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('durationHour', uint8_t),
        ('durationMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifier', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('weekDayBitmask', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('durationHour', uint8_t),
        ('durationMinute', uint8_t),
    ]


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_TIME_OFFSET_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V4_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_GET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V4_FRAME(ZW_SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V4_FRAME(ZW_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V3_FRAME):
    _fields_ = []


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('dayOfWeek', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('dayOfWeek', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('startYear', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopYear', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('startYear', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('stopYear', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHour', uint8_t),
        ('stopMinute', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('setAction', uint8_t),
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('weekDayBitmask', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('durationHour', uint8_t),
        ('durationMinute', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
    ]


class ZW_EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userIdentifierMsb', uint8_t),
        ('userIdentifierLsb', uint8_t),
        ('scheduleSlotId', uint8_t),
        ('weekDayBitmask', uint8_t),
        ('startHour', uint8_t),
        ('startMinute', uint8_t),
        ('durationHour', uint8_t),
        ('durationMinute', uint8_t),
    ]
