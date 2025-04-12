# Binary Toggle Switch Command Class
# Application
# ==============================
COMMAND_CLASS_SWITCH_TOGGLE_BINARY = 0x28

SWITCH_TOGGLE_BINARY_VERSION = 0x01
# Binary Toggle Switch Set
SWITCH_TOGGLE_BINARY_SET = 0x01
# Binary Toggle Switch Get
SWITCH_TOGGLE_BINARY_GET = 0x02
# Binary Toggle Switch Report
SWITCH_TOGGLE_BINARY_REPORT = 0x03

class ZW_SWITCH_TOGGLE_BINARY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SWITCH_TOGGLE_BINARY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SWITCH_TOGGLE_BINARY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]

