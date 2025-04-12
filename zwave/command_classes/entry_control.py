# Entry Control Command Class
# Application
# ==============================
COMMAND_CLASS_ENTRY_CONTROL = 0x6F

ENTRY_CONTROL_VERSION = 0x01
# Entry Control Notification
ENTRY_CONTROL_NOTIFICATION = 0x01
# Entry Control Key Supported Get
ENTRY_CONTROL_KEY_SUPPORTED_GET = 0x02
# Entry Control Key Supported Report
ENTRY_CONTROL_KEY_SUPPORTED_REPORT = 0x03
# Entry Control Event Supported Get
ENTRY_CONTROL_EVENT_SUPPORTED_GET = 0x04
# Entry Control Event Supported Report
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT = 0x05
# Entry Control Configuration Set
ENTRY_CONTROL_CONFIGURATION_SET = 0x06
# Entry Control Configuration Get
ENTRY_CONTROL_CONFIGURATION_GET = 0x07
# Entry Control Configuration Report
ENTRY_CONTROL_CONFIGURATION_REPORT = 0x08

# Values used for Entry Control Notification command
ENTRY_CONTROL_NOTIFICATION_PROPERTIES1_DATA_TYPE_MASK = 0x03
ENTRY_CONTROL_NOTIFICATION_DATA_TYPE_NA = 0x00
ENTRY_CONTROL_NOTIFICATION_DATA_TYPE_RAW = 0x01
ENTRY_CONTROL_NOTIFICATION_DATA_TYPE_ASCII = 0x02
ENTRY_CONTROL_NOTIFICATION_DATA_TYPE_MD5 = 0x03
ENTRY_CONTROL_NOTIFICATION_PROPERTIES1_RESERVED_MASK = 0xFC
ENTRY_CONTROL_NOTIFICATION_PROPERTIES1_RESERVED_SHIFT = 0x02
ENTRY_CONTROL_NOTIFICATION_CACHING = 0x00
ENTRY_CONTROL_NOTIFICATION_CACHED_KEYS = 0x01
ENTRY_CONTROL_NOTIFICATION_ENTER = 0x02
ENTRY_CONTROL_NOTIFICATION_DISARM_ALL = 0x03
ENTRY_CONTROL_NOTIFICATION_ARM_ALL = 0x04
ENTRY_CONTROL_NOTIFICATION_ARM_AWAY = 0x05
ENTRY_CONTROL_NOTIFICATION_ARM_HOME = 0x06
ENTRY_CONTROL_NOTIFICATION_EXIT_DELAY = 0x07
ENTRY_CONTROL_NOTIFICATION_ARM_1 = 0x08
ENTRY_CONTROL_NOTIFICATION_ARM_2 = 0x09
ENTRY_CONTROL_NOTIFICATION_ARM_3 = 0x0A
ENTRY_CONTROL_NOTIFICATION_ARM_4 = 0x0B
ENTRY_CONTROL_NOTIFICATION_ARM_5 = 0x0C
ENTRY_CONTROL_NOTIFICATION_ARM_6 = 0x0D
ENTRY_CONTROL_NOTIFICATION_RFID = 0x0E
ENTRY_CONTROL_NOTIFICATION_BELL = 0x0F
ENTRY_CONTROL_NOTIFICATION_FIRE = 0x10
ENTRY_CONTROL_NOTIFICATION_POLICE = 0x11
ENTRY_CONTROL_NOTIFICATION_ALERT_PANIC = 0x12
ENTRY_CONTROL_NOTIFICATION_ALERT_MEDICAL = 0x13
ENTRY_CONTROL_NOTIFICATION_GATE_OPEN = 0x14
ENTRY_CONTROL_NOTIFICATION_GATE_CLOSE = 0x15
ENTRY_CONTROL_NOTIFICATION_LOCK = 0x16
ENTRY_CONTROL_NOTIFICATION_UNLOCK = 0x17
ENTRY_CONTROL_NOTIFICATION_TEST = 0x18
ENTRY_CONTROL_NOTIFICATION_CANCEL = 0x19
# Values used for Entry Control Event Supported Report command
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES1_DATA_TYPE_SUPPORTED_BIT_MASK_LENGTH_MASK = 0x03
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES1_RESERVED1_MASK = 0xFC
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x02
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES2_EVENT_SUPPORTED_BIT_MASK_LENGTH_MASK = 0x1F
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES2_RESERVED2_MASK = 0xE0
ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_PROPERTIES2_RESERVED2_SHIFT = 0x05

class ZW_ENTRY_CONTROL_NOTIFICATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('properties1', uint8_t),
        ('eventType', uint8_t),
        ('eventDataLength', uint8_t),
        ('eventData1', uint8_t),
    ]


class ZW_ENTRY_CONTROL_KEY_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ENTRY_CONTROL_KEY_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('keySupportedBitMaskLength', uint8_t),
        ('keySupportedBitMask1', uint8_t),
    ]


class ZW_ENTRY_CONTROL_EVENT_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ENTRY_CONTROL_EVENT_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('dataTypeSupportedBitMask1', uint8_t),
        ('properties2', uint8_t),
        ('eventTypeSupportedBitMask1', uint8_t),
        ('keyCachedSizeSupportedMinimum', uint8_t),
        ('keyCachedSizeSupportedMaximum', uint8_t),
        ('keyCachedTimeoutSupportedMinimum', uint8_t),
        ('keyCachedTimeoutSupportedMaximum', uint8_t),
    ]


class ZW_ENTRY_CONTROL_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('keyCacheSize', uint8_t),
        ('keyCacheTimeout', uint8_t),
    ]


class ZW_ENTRY_CONTROL_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ENTRY_CONTROL_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('keyCacheSize', uint8_t),
        ('keyCacheTimeout', uint8_t),
    ]

