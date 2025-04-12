# Wake Up Command Class
# Management
# ==============================
COMMAND_CLASS_WAKE_UP = 0x84

WAKE_UP_VERSION = 0x01
# Wake Up Interval Set
WAKE_UP_INTERVAL_SET = 0x04
# Wake Up Interval Get
WAKE_UP_INTERVAL_GET = 0x05
# Wake Up Interval Report
WAKE_UP_INTERVAL_REPORT = 0x06
# Wake Up Notification
WAKE_UP_NOTIFICATION = 0x07
# Wake Up No More Information
WAKE_UP_NO_MORE_INFORMATION = 0x08

WAKE_UP_VERSION_V2 = 0x02
WAKE_UP_INTERVAL_GET_V2 = 0x05
WAKE_UP_INTERVAL_REPORT_V2 = 0x06
WAKE_UP_INTERVAL_SET_V2 = 0x04
WAKE_UP_NO_MORE_INFORMATION_V2 = 0x08
WAKE_UP_NOTIFICATION_V2 = 0x07
# Wake Up Interval Capabilities Get
WAKE_UP_INTERVAL_CAPABILITIES_GET_V2 = 0x09
# Wake Up Interval Capabilities Report
WAKE_UP_INTERVAL_CAPABILITIES_REPORT_V2 = 0x0A



WAKE_UP_VERSION_V3 = 0x03
WAKE_UP_INTERVAL_CAPABILITIES_GET_V3 = 0x09
WAKE_UP_INTERVAL_CAPABILITIES_REPORT_V3 = 0x0A
WAKE_UP_INTERVAL_GET_V3 = 0x05
WAKE_UP_INTERVAL_REPORT_V3 = 0x06
WAKE_UP_INTERVAL_SET_V3 = 0x04
WAKE_UP_NO_MORE_INFORMATION_V3 = 0x08
WAKE_UP_NOTIFICATION_V3 = 0x07
# Values used for Wake Up Interval Capabilities Report command
WAKE_UP_INTERVAL_CAPABILITIES_REPORT_PROPERTIES1_WAKE_UP_ON_DEMAND_BIT_MASK_V3 = 0x01
WAKE_UP_INTERVAL_CAPABILITIES_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0xFE
WAKE_UP_INTERVAL_CAPABILITIES_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x01


class ZW_WAKE_UP_INTERVAL_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seconds1', uint8_t),
        ('seconds2', uint8_t),
        ('seconds3', uint8_t),
        ('nodeid', uint8_t),
    ]


class ZW_WAKE_UP_INTERVAL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seconds1', uint8_t),
        ('seconds2', uint8_t),
        ('seconds3', uint8_t),
        ('nodeid', uint8_t),
    ]


class ZW_WAKE_UP_NO_MORE_INFORMATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_WAKE_UP_NOTIFICATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('minimumWakeUpIntervalSeconds1', uint8_t),
        ('minimumWakeUpIntervalSeconds2', uint8_t),
        ('minimumWakeUpIntervalSeconds3', uint8_t),
        ('maximumWakeUpIntervalSeconds1', uint8_t),
        ('maximumWakeUpIntervalSeconds2', uint8_t),
        ('maximumWakeUpIntervalSeconds3', uint8_t),
        ('defaultWakeUpIntervalSeconds1', uint8_t),
        ('defaultWakeUpIntervalSeconds2', uint8_t),
        ('defaultWakeUpIntervalSeconds3', uint8_t),
        ('wakeUpIntervalStepSeconds1', uint8_t),
        ('wakeUpIntervalStepSeconds2', uint8_t),
        ('wakeUpIntervalStepSeconds3', uint8_t),
    ]


class ZW_WAKE_UP_INTERVAL_GET_V2_FRAME(ZW_WAKE_UP_INTERVAL_GET_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_REPORT_V2_FRAME(ZW_WAKE_UP_INTERVAL_REPORT_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_SET_V2_FRAME(ZW_WAKE_UP_INTERVAL_SET_FRAME):
    _fields_ = []


class ZW_WAKE_UP_NO_MORE_INFORMATION_V2_FRAME(ZW_WAKE_UP_NO_MORE_INFORMATION_FRAME):
    _fields_ = []


class ZW_WAKE_UP_NOTIFICATION_V2_FRAME(ZW_WAKE_UP_NOTIFICATION_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET_V3_FRAME(ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET_V2_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT_V3_FRAME(ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT_V2_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_WAKE_UP_INTERVAL_GET_V3_FRAME(ZW_WAKE_UP_INTERVAL_GET_V2_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_REPORT_V3_FRAME(ZW_WAKE_UP_INTERVAL_REPORT_V2_FRAME):
    _fields_ = []


class ZW_WAKE_UP_INTERVAL_SET_V3_FRAME(ZW_WAKE_UP_INTERVAL_SET_V2_FRAME):
    _fields_ = []


class ZW_WAKE_UP_NO_MORE_INFORMATION_V3_FRAME(ZW_WAKE_UP_NO_MORE_INFORMATION_V2_FRAME):
    _fields_ = []


class ZW_WAKE_UP_NOTIFICATION_V3_FRAME(ZW_WAKE_UP_NOTIFICATION_V2_FRAME):
    _fields_ = []

