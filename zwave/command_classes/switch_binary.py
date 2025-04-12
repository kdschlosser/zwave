# Binary Switch Command Class
# Application
# ==============================
COMMAND_CLASS_SWITCH_BINARY = 0x25

SWITCH_BINARY_VERSION = 0x01
# Binary Switch Set
SWITCH_BINARY_SET = 0x01
# Binary Switch Get
SWITCH_BINARY_GET = 0x02
# Binary Switch Report
SWITCH_BINARY_REPORT = 0x03


SWITCH_BINARY_VERSION_V2 = 0x02
SWITCH_BINARY_GET_V2 = 0x02
SWITCH_BINARY_REPORT_V2 = 0x03
SWITCH_BINARY_SET_V2 = 0x01
# Values used for Switch Binary Report command
SWITCH_BINARY_REPORT_OFF_0_V2 = 0x00
SWITCH_BINARY_REPORT_UNKNOWN_V2 = 0xFE
SWITCH_BINARY_REPORT_ON_100_V2 = 0xFF
SWITCH_BINARY_REPORT_ALREADY_AT_THE_TARGET_VALUE_V2 = 0x00
SWITCH_BINARY_REPORT_UNKNOWN_DURATION_V2 = 0xFE
SWITCH_BINARY_REPORT_RESERVED_V2 = 0xFF
# Values used for Switch Binary Set command
SWITCH_BINARY_SET_OFF_0_V2 = 0x00
SWITCH_BINARY_SET_ON_100_V2 = 0xFF
SWITCH_BINARY_SET_INSTANTLY_V2 = 0x00
SWITCH_BINARY_SET_DEFAULT_V2 = 0xFF


class ZW_SWITCH_BINARY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SWITCH_BINARY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


class ZW_SWITCH_BINARY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('switchValue', uint8_t)]


class ZW_SWITCH_BINARY_GET_V2_FRAME(ZW_SWITCH_BINARY_GET_FRAME):
    _fields_ = []


class ZW_SWITCH_BINARY_REPORT_V2_FRAME(ZW_SWITCH_BINARY_REPORT_FRAME):
    _fields_ = [
        ('currentValue', uint8_t),
        ('targetValue', uint8_t),
        ('duration', uint8_t),
    ]


class ZW_SWITCH_BINARY_SET_V2_FRAME(ZW_SWITCH_BINARY_SET_FRAME):
    _fields_ = [
        ('targetValue', uint8_t),
        ('duration', uint8_t),
    ]
