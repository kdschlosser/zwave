# Schedule Command Class
# Application
# ==============================
COMMAND_CLASS_SCHEDULE = 0x53

SCHEDULE_VERSION = 0x01
# Schedule Supported Get
SCHEDULE_SUPPORTED_GET = 0x01
# Schedule Supported Report
SCHEDULE_SUPPORTED_REPORT = 0x02
# Schedule Set
COMMAND_SCHEDULE_SET = 0x03
# Schedule Get
COMMAND_SCHEDULE_GET = 0x04
# Schedule Report
COMMAND_SCHEDULE_REPORT = 0x05
# Schedule Remove
SCHEDULE_REMOVE = 0x06
# Schedule State Set
SCHEDULE_STATE_SET = 0x07
# Schedule State Get
SCHEDULE_STATE_GET = 0x08
# Schedule State Report
SCHEDULE_STATE_REPORT = 0x09

# Values used for Schedule Supported Report command
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_START_TIME_SUPPORT_MASK = 0x3F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_FALLBACK_SUPPORT_BIT_MASK = 0x40
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_SUPPORT_ENABLE_DISABLE_BIT_MASK = 0x80
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_SUPPORTED_OVERRIDE_TYPES_MASK = 0x7F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_OVERRIDE_SUPPORT_BIT_MASK = 0x80
# Values used for Command Schedule Set command
COMMAND_SCHEDULE_SET_PROPERTIES1_START_MONTH_MASK = 0x0F
COMMAND_SCHEDULE_SET_PROPERTIES1_RESERVED1_MASK = 0xF0
COMMAND_SCHEDULE_SET_PROPERTIES1_RESERVED1_SHIFT = 0x04
COMMAND_SCHEDULE_SET_PROPERTIES2_START_DAY_OF_MONTH_MASK = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED2_MASK = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED2_SHIFT = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES3_START_WEEKDAY_MASK = 0x7F
COMMAND_SCHEDULE_SET_PROPERTIES3_RES_BIT_MASK = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES4_START_HOUR_MASK = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_MASK = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_SHIFT = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES5_START_MINUTE_MASK = 0x3F
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_MASK = 0xC0
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_SHIFT = 0x06
# Values used for Command Schedule Report command
COMMAND_SCHEDULE_REPORT_PROPERTIES1_START_MONTH_MASK = 0x0F
COMMAND_SCHEDULE_REPORT_PROPERTIES1_ACTIVE_ID_MASK = 0xF0
COMMAND_SCHEDULE_REPORT_PROPERTIES1_ACTIVE_ID_SHIFT = 0x04
COMMAND_SCHEDULE_REPORT_PROPERTIES2_START_DAY_OF_MONTH_MASK = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RESERVED2_MASK = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RESERVED2_SHIFT = 0x05
COMMAND_SCHEDULE_REPORT_PROPERTIES3_START_WEEKDAY_MASK = 0x7F
COMMAND_SCHEDULE_REPORT_PROPERTIES3_RES_BIT_MASK = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES4_START_HOUR_MASK = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_MASK = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_SHIFT = 0x05
COMMAND_SCHEDULE_REPORT_PROPERTIES5_START_MINUTE_MASK = 0x3F
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED3_MASK = 0xC0
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED3_SHIFT = 0x06
# Values used for Schedule State Report command
SCHEDULE_STATE_REPORT_PROPERTIES1_OVERRIDE_BIT_MASK = 0x01
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_MASK = 0xFE
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_SHIFT = 0x01

SCHEDULE_VERSION_V2 = 0x02
SCHEDULE_SUPPORTED_GET_V2 = 0x01
SCHEDULE_SUPPORTED_REPORT_V2 = 0x02
COMMAND_SCHEDULE_SET_V2 = 0x03
COMMAND_SCHEDULE_GET_V2 = 0x04
COMMAND_SCHEDULE_REPORT_V2 = 0x05
SCHEDULE_REMOVE_V2 = 0x06
SCHEDULE_STATE_SET_V2 = 0x07
SCHEDULE_STATE_GET_V2 = 0x08
SCHEDULE_STATE_REPORT_V2 = 0x09
# Values used for Schedule Supported Report command
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_START_TIME_SUPPORT_MASK_V2 = 0x3F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_FALLBACK_SUPPORT_BIT_MASK_V2 = 0x40
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_SUPPORT_ENABLE_DISABLE_BIT_MASK_V2 = 0x80
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_SUPPORTED_OVERRIDE_TYPES_MASK_V2 = 0x7F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_OVERRIDE_SUPPORT_BIT_MASK_V2 = 0x80
# Values used for Command Schedule Set command
COMMAND_SCHEDULE_SET_PROPERTIES1_START_MONTH_MASK_V2 = 0x0F
COMMAND_SCHEDULE_SET_PROPERTIES1_RESERVED0_MASK_V2 = 0xF0
COMMAND_SCHEDULE_SET_PROPERTIES1_RESERVED0_SHIFT_V2 = 0x04
COMMAND_SCHEDULE_SET_PROPERTIES2_START_DAY_OF_MONTH_MASK_V2 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED1_MASK_V2 = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED1_SHIFT_V2 = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES3_START_WEEKDAY_MASK_V2 = 0x7F
COMMAND_SCHEDULE_SET_PROPERTIES3_RESERVED2_BIT_MASK_V2 = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES4_START_HOUR_MASK_V2 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_MASK_V2 = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_SHIFT_V2 = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES5_START_MINUTE_MASK_V2 = 0x3F
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_MASK_V2 = 0xC0
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_SHIFT_V2 = 0x06
# Values used for Command Schedule Report command
COMMAND_SCHEDULE_REPORT_PROPERTIES1_START_MONTH_MASK_V2 = 0x0F
COMMAND_SCHEDULE_REPORT_PROPERTIES1_ACTIVE_ID_MASK_V2 = 0xF0
COMMAND_SCHEDULE_REPORT_PROPERTIES1_ACTIVE_ID_SHIFT_V2 = 0x04
COMMAND_SCHEDULE_REPORT_PROPERTIES2_START_DAY_OF_MONTH_MASK_V2 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RESERVED0_MASK_V2 = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RESERVED0_SHIFT_V2 = 0x05
COMMAND_SCHEDULE_REPORT_RESERVED0_REPEAT_EVERY_N_HOURS_V2 = 0x00
COMMAND_SCHEDULE_REPORT_RESERVED0_REPEAT_EVERY_N_DAYS_V2 = 0x01
COMMAND_SCHEDULE_REPORT_RESERVED0_REPEAT_EVERY_N_WEEKS_V2 = 0x02
COMMAND_SCHEDULE_REPORT_PROPERTIES3_START_WEEKDAY_MASK_V2 = 0x7F
COMMAND_SCHEDULE_REPORT_PROPERTIES3_RESERVED1_BIT_MASK_V2 = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES4_START_HOUR_MASK_V2 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_MASK_V2 = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_SHIFT_V2 = 0x05
COMMAND_SCHEDULE_REPORT_PROPERTIES5_START_MINUTE_MASK_V2 = 0x3F
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED2_MASK_V2 = 0xC0
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED2_SHIFT_V2 = 0x06
# Values used for Schedule State Report command
SCHEDULE_STATE_REPORT_PROPERTIES1_OVERRIDE_BIT_MASK_V2 = 0x01
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_MASK_V2 = 0xFE
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_SHIFT_V2 = 0x01

SCHEDULE_VERSION_V3 = 0x03
SCHEDULE_SUPPORTED_GET_V3 = 0x01
SCHEDULE_SUPPORTED_REPORT_V3 = 0x02
COMMAND_SCHEDULE_SET_V3 = 0x03
COMMAND_SCHEDULE_GET_V3 = 0x04
COMMAND_SCHEDULE_REPORT_V3 = 0x05
SCHEDULE_REMOVE_V3 = 0x06
SCHEDULE_STATE_SET_V3 = 0x07
SCHEDULE_STATE_GET_V3 = 0x08
SCHEDULE_STATE_REPORT_V3 = 0x09
# Values used for Schedule Supported Report command
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_START_TIME_SUPPORT_MASK_V3 = 0x3F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_FALLBACK_SUPPORT_BIT_MASK_V3 = 0x40
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_SUPPORT_ENABLE_DISABLE_BIT_MASK_V3 = 0x80
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_SUPPORTED_OVERRIDE_TYPES_MASK_V3 = 0x7F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_OVERRIDE_SUPPORT_BIT_MASK_V3 = 0x80
# Values used for Command Schedule Set command
COMMAND_SCHEDULE_SET_PROPERTIES1_START_MONTH_MASK_V3 = 0x0F
COMMAND_SCHEDULE_SET_PROPERTIES1_RECURRENCE_OFFSET_MASK_V3 = 0xF0
COMMAND_SCHEDULE_SET_PROPERTIES1_RECURRENCE_OFFSET_SHIFT_V3 = 0x04
COMMAND_SCHEDULE_SET_PROPERTIES2_START_DAY_OF_MONTH_MASK_V3 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES2_RECURRENCE_MODE_MASK_V3 = 0x60
COMMAND_SCHEDULE_SET_PROPERTIES2_RECURRENCE_MODE_SHIFT_V3 = 0x05
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_HOURS_V3 = 0x00
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_DAYS_V3 = 0x01
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_WEEKS_V3 = 0x02
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED1_BIT_MASK_V3 = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES3_START_WEEKDAY_MASK_V3 = 0x7F
COMMAND_SCHEDULE_SET_PROPERTIES3_RESERVED2_BIT_MASK_V3 = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES4_START_HOUR_MASK_V3 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_MASK_V3 = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_SHIFT_V3 = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES5_START_MINUTE_MASK_V3 = 0x3F
COMMAND_SCHEDULE_SET_PROPERTIES5_RELATIVE_BIT_MASK_V3 = 0x40
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_BIT_MASK_V3 = 0x80
# Values used for Command Schedule Get command
COMMAND_SCHEDULE_GET_PROPERTIES1_RESERVED_MASK_V3 = 0x7F
COMMAND_SCHEDULE_GET_PROPERTIES1_AID_RO_CTL_BIT_MASK_V3 = 0x80
# Values used for Command Schedule Report command
COMMAND_SCHEDULE_REPORT_PROPERTIES1_START_MONTH_MASK_V3 = 0x0F
COMMAND_SCHEDULE_REPORT_PROPERTIES1_AID_RO_MASK_V3 = 0xF0
COMMAND_SCHEDULE_REPORT_PROPERTIES1_AID_RO_SHIFT_V3 = 0x04
COMMAND_SCHEDULE_REPORT_PROPERTIES2_START_DAY_OF_MONTH_MASK_V3 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RECURRENCE_MODE_MASK_V3 = 0x60
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RECURRENCE_MODE_SHIFT_V3 = 0x05
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_HOURS_V3 = 0x00
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_DAYS_V3 = 0x01
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_WEEKS_V3 = 0x02
COMMAND_SCHEDULE_REPORT_PROPERTIES2_AID_RO_CTL_BIT_MASK_V3 = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES3_START_WEEKDAY_MASK_V3 = 0x7F
COMMAND_SCHEDULE_REPORT_PROPERTIES3_RESERVED1_BIT_MASK_V3 = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES4_START_HOUR_MASK_V3 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_MASK_V3 = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_SHIFT_V3 = 0x05
COMMAND_SCHEDULE_REPORT_PROPERTIES5_START_MINUTE_MASK_V3 = 0x3F
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RELATIVE_BIT_MASK_V3 = 0x40
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED2_BIT_MASK_V3 = 0x80
# Values used for Schedule State Report command
SCHEDULE_STATE_REPORT_PROPERTIES1_OVERRIDE_BIT_MASK_V3 = 0x01
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_MASK_V3 = 0xFE
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_SHIFT_V3 = 0x01

SCHEDULE_VERSION_V4 = 0x04
SCHEDULE_SUPPORTED_GET_V4 = 0x01
SCHEDULE_SUPPORTED_REPORT_V4 = 0x02
COMMAND_SCHEDULE_SET_V4 = 0x03
COMMAND_SCHEDULE_GET_V4 = 0x04
COMMAND_SCHEDULE_REPORT_V4 = 0x05
SCHEDULE_REMOVE_V4 = 0x06
SCHEDULE_STATE_SET_V4 = 0x07
SCHEDULE_STATE_GET_V4 = 0x08
SCHEDULE_STATE_REPORT_V4 = 0x09
# Schedule Supported Commands Get
SCHEDULE_SUPPORTED_COMMANDS_GET_V4 = 0x0A
# Schedule Supported Commands Report
SCHEDULE_SUPPORTED_COMMANDS_REPORT_V4 = 0x0B


# Values used for Schedule Supported Report command
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_START_TIME_SUPPORT_MASK_V4 = 0x3F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_FALLBACK_SUPPORT_BIT_MASK_V4 = 0x40
SCHEDULE_SUPPORTED_REPORT_PROPERTIES1_SUPPORT_ENABLE_DISABLE_BIT_MASK_V4 = 0x80
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_SUPPORTED_OVERRIDE_TYPES_MASK_V4 = 0x7F
SCHEDULE_SUPPORTED_REPORT_PROPERTIES3_OVERRIDE_SUPPORT_BIT_MASK_V4 = 0x80
# Values used for Command Schedule Set command
COMMAND_SCHEDULE_SET_PROPERTIES1_START_MONTH_MASK_V4 = 0x0F
COMMAND_SCHEDULE_SET_PROPERTIES1_RECURRENCE_OFFSET_MASK_V4 = 0xF0
COMMAND_SCHEDULE_SET_PROPERTIES1_RECURRENCE_OFFSET_SHIFT_V4 = 0x04
COMMAND_SCHEDULE_SET_PROPERTIES2_START_DAY_OF_MONTH_MASK_V4 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES2_RECURRENCE_MODE_MASK_V4 = 0x60
COMMAND_SCHEDULE_SET_PROPERTIES2_RECURRENCE_MODE_SHIFT_V4 = 0x05
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_HOURS_V4 = 0x00
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_DAYS_V4 = 0x01
COMMAND_SCHEDULE_SET_RECURRENCE_MODE_REPEAT_EVERY_N_WEEKS_V4 = 0x02
COMMAND_SCHEDULE_SET_PROPERTIES2_RESERVED1_BIT_MASK_V4 = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES3_START_WEEKDAY_MASK_V4 = 0x7F
COMMAND_SCHEDULE_SET_PROPERTIES3_RESERVED2_BIT_MASK_V4 = 0x80
COMMAND_SCHEDULE_SET_PROPERTIES4_START_HOUR_MASK_V4 = 0x1F
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_MASK_V4 = 0xE0
COMMAND_SCHEDULE_SET_PROPERTIES4_DURATION_TYPE_SHIFT_V4 = 0x05
COMMAND_SCHEDULE_SET_PROPERTIES5_START_MINUTE_MASK_V4 = 0x3F
COMMAND_SCHEDULE_SET_PROPERTIES5_RELATIVE_BIT_MASK_V4 = 0x40
COMMAND_SCHEDULE_SET_PROPERTIES5_RESERVED3_BIT_MASK_V4 = 0x80
# Values used for Command Schedule Get command
COMMAND_SCHEDULE_GET_PROPERTIES1_RESERVED_MASK_V4 = 0x7F
COMMAND_SCHEDULE_GET_PROPERTIES1_AID_RO_CTL_BIT_MASK_V4 = 0x80
# Values used for Command Schedule Report command
COMMAND_SCHEDULE_REPORT_PROPERTIES1_START_MONTH_MASK_V4 = 0x0F
COMMAND_SCHEDULE_REPORT_PROPERTIES1_AID_RO_MASK_V4 = 0xF0
COMMAND_SCHEDULE_REPORT_PROPERTIES1_AID_RO_SHIFT_V4 = 0x04
COMMAND_SCHEDULE_REPORT_PROPERTIES2_START_DAY_OF_MONTH_MASK_V4 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RECURRENCE_MODE_MASK_V4 = 0x60
COMMAND_SCHEDULE_REPORT_PROPERTIES2_RECURRENCE_MODE_SHIFT_V4 = 0x05
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_HOURS_V4 = 0x00
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_DAYS_V4 = 0x01
COMMAND_SCHEDULE_REPORT_RECURRENCE_MODE_REPEAT_EVERY_N_WEEKS_V4 = 0x02
COMMAND_SCHEDULE_REPORT_PROPERTIES2_AID_RO_CTL_BIT_MASK_V4 = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES3_START_WEEKDAY_MASK_V4 = 0x7F
COMMAND_SCHEDULE_REPORT_PROPERTIES3_RESERVED1_BIT_MASK_V4 = 0x80
COMMAND_SCHEDULE_REPORT_PROPERTIES4_START_HOUR_MASK_V4 = 0x1F
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_MASK_V4 = 0xE0
COMMAND_SCHEDULE_REPORT_PROPERTIES4_DURATION_TYPE_SHIFT_V4 = 0x05
COMMAND_SCHEDULE_REPORT_PROPERTIES5_START_MINUTE_MASK_V4 = 0x3F
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RELATIVE_BIT_MASK_V4 = 0x40
COMMAND_SCHEDULE_REPORT_PROPERTIES5_RESERVED2_BIT_MASK_V4 = 0x80
# Values used for Schedule State Report command
SCHEDULE_STATE_REPORT_PROPERTIES1_OVERRIDE_BIT_MASK_V4 = 0x01
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_MASK_V4 = 0xFE
SCHEDULE_STATE_REPORT_PROPERTIES1_REPORTS_TO_FOLLOW_SHIFT_V4 = 0x01

class ZW_SCHEDULE_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class VG_SCHEDULE_SUPPORTED_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('supportedCc', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_SCHEDULE_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfSupportedScheduleId', uint8_t),
        ('properties1', uint8_t),
        ('numberOfSupportedCc', uint8_t),
        ('variantgroup1', VG_SCHEDULE_SUPPORTED_REPORT_VG),
        ('properties3', uint8_t),
    ]


class VG_COMMAND_SCHEDULE_SET_VG(ctypes.Structure):
    _fields_ = [
        ('cmdLength', uint8_t),
        ('cmdByte1', uint8_t),
    ]


class ZW_COMMAND_SCHEDULE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('scheduleId', uint8_t),
        ('userIdentifier', uint8_t),
        ('startYear', uint8_t),
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('properties3', uint8_t),
        ('properties4', uint8_t),
        ('properties5', uint8_t),
        ('durationByte1', uint8_t),
        ('durationByte2', uint8_t),
        ('reportsToFollow', uint8_t),
        ('numberOfCmdToFollow', uint8_t),
        ('variantgroup1', VG_COMMAND_SCHEDULE_SET_VG),
    ]


class ZW_COMMAND_SCHEDULE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('scheduleId', uint8_t)]


class VG_COMMAND_SCHEDULE_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('cmdLength', uint8_t),
        ('cmdByte1', uint8_t),
    ]


class ZW_COMMAND_SCHEDULE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('scheduleId', uint8_t),
        ('userIdentifier', uint8_t),
        ('startYear', uint8_t),
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('properties3', uint8_t),
        ('properties4', uint8_t),
        ('properties5', uint8_t),
        ('durationByte1', uint8_t),
        ('durationByte2', uint8_t),
        ('reportsToFollow', uint8_t),
        ('numberOfCmdToFollow', uint8_t),
        ('variantgroup1', VG_COMMAND_SCHEDULE_REPORT_VG),
    ]


class ZW_SCHEDULE_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('scheduleId', uint8_t)]


class ZW_SCHEDULE_STATE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('scheduleId', uint8_t),
        ('scheduleState', uint8_t),
    ]


class ZW_SCHEDULE_STATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class VG_SCHEDULE_STATE_REPORT_VG(ctypes.Structure):
    _fields_ = [('properties2', uint8_t)]


class ZW_SCHEDULE_STATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfSupportedScheduleId', uint8_t),
        ('properties1', uint8_t),
        ('variantgroup1', VG_SCHEDULE_STATE_REPORT_VG),
    ]


class ZW_SCHEDULE_SUPPORTED_GET_V2_FRAME(ZW_SCHEDULE_SUPPORTED_GET_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class VG_SCHEDULE_SUPPORTED_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('supportedCc', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_SCHEDULE_SUPPORTED_REPORT_V2_FRAME(ZW_SCHEDULE_SUPPORTED_REPORT_FRAME):
    _fields_ = [
        ('scheduleIdBlock', uint8_t),
        ('numberOfSupportedScheduleBlocks', uint8_t),
    ]


class ZW_COMMAND_SCHEDULE_SET_V2_FRAME(ZW_COMMAND_SCHEDULE_SET_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_COMMAND_SCHEDULE_GET_V2_FRAME(ZW_COMMAND_SCHEDULE_GET_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_COMMAND_SCHEDULE_REPORT_V2_FRAME(ZW_COMMAND_SCHEDULE_REPORT_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_SCHEDULE_REMOVE_V2_FRAME(ZW_SCHEDULE_REMOVE_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_SCHEDULE_STATE_SET_V2_FRAME(ZW_SCHEDULE_STATE_SET_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_SCHEDULE_STATE_GET_V2_FRAME(ZW_SCHEDULE_STATE_GET_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class VG_SCHEDULE_STATE_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [('properties2', uint8_t)]


class ZW_SCHEDULE_STATE_REPORT_V2_FRAME(ZW_SCHEDULE_STATE_REPORT_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class ZW_SCHEDULE_SUPPORTED_GET_V3_FRAME(ZW_SCHEDULE_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class VG_SCHEDULE_SUPPORTED_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('supportedCc', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_SCHEDULE_SUPPORTED_REPORT_V3_FRAME(ZW_SCHEDULE_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = []


class ZW_COMMAND_SCHEDULE_SET_V3_FRAME(ZW_COMMAND_SCHEDULE_SET_V2_FRAME):
    _fields_ = []


class ZW_COMMAND_SCHEDULE_GET_V3_FRAME(ZW_COMMAND_SCHEDULE_GET_V2_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_COMMAND_SCHEDULE_REPORT_V3_FRAME(ZW_COMMAND_SCHEDULE_REPORT_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_REMOVE_V3_FRAME(ZW_SCHEDULE_REMOVE_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_STATE_SET_V3_FRAME(ZW_SCHEDULE_STATE_SET_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_STATE_GET_V3_FRAME(ZW_SCHEDULE_STATE_GET_V2_FRAME):
    _fields_ = []


class VG_SCHEDULE_STATE_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [('properties2', uint8_t)]


class ZW_SCHEDULE_STATE_REPORT_V3_FRAME(ZW_SCHEDULE_STATE_REPORT_V2_FRAME):
    _fields_ = []


class ZW_SCHEDULE_SUPPORTED_GET_V4_FRAME(ZW_SCHEDULE_SUPPORTED_GET_V3_FRAME):
    _fields_ = []


class VG_SCHEDULE_SUPPORTED_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [
        ('supportedCc', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_SCHEDULE_SUPPORTED_REPORT_V4_FRAME(ZW_SCHEDULE_SUPPORTED_REPORT_V3_FRAME):
    _fields_ = []


class ZW_COMMAND_SCHEDULE_SET_V4_FRAME(ZW_COMMAND_SCHEDULE_SET_V3_FRAME):
    _fields_ = []


class ZW_COMMAND_SCHEDULE_GET_V4_FRAME(ZW_COMMAND_SCHEDULE_GET_V3_FRAME):
    _fields_ = []


class ZW_COMMAND_SCHEDULE_REPORT_V4_FRAME(ZW_COMMAND_SCHEDULE_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_REMOVE_V4_FRAME(ZW_SCHEDULE_REMOVE_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_STATE_SET_V4_FRAME(ZW_SCHEDULE_STATE_SET_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_STATE_GET_V4_FRAME(ZW_SCHEDULE_STATE_GET_V3_FRAME):
    _fields_ = []


class VG_SCHEDULE_STATE_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [('properties2', uint8_t)]



class ZW_SCHEDULE_STATE_REPORT_V4_FRAME(ZW_SCHEDULE_STATE_REPORT_V3_FRAME):
    _fields_ = []


class ZW_SCHEDULE_SUPPORTED_COMMANDS_GET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('scheduleIdBlock', uint8_t)]


class VG_SCHEDULE_SUPPORTED_COMMANDS_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [
        ('commandClass', uint8_t),
        ('supportedCommandListLength', uint8_t),
        ('supportedCommand1', uint8_t),
    ]


class ZW_SCHEDULE_SUPPORTED_COMMANDS_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('scheduleIdBlock', uint8_t),
        ('commandClassListLength', uint8_t),
        ('variantgroup1', VG_SCHEDULE_SUPPORTED_COMMANDS_REPORT_V4_VG),
    ]

