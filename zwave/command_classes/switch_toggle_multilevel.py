# Multilevel Toggle Switch Command Class
# Application
# ==============================
COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL = 0x29

SWITCH_TOGGLE_MULTILEVEL_VERSION = 0x01
# Multilevel Toggle Switch Set
SWITCH_TOGGLE_MULTILEVEL_SET = 0x01
# Multilevel Toggle Switch Get
SWITCH_TOGGLE_MULTILEVEL_GET = 0x02
# Multilevel Toggle Switch Report
SWITCH_TOGGLE_MULTILEVEL_REPORT = 0x03
# Multilevel Toggle Switch Start Level Change
SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE = 0x04
# Multilevel Toggle Switch Stop Level Change
SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE = 0x05

# Values used for Switch Toggle Multilevel Start Level Change command
SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE_LEVEL_RESERVED1_MASK = 0x1F
SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE_LEVEL_IGNORE_START_LEVEL_BIT_MASK = 0x20
SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE_LEVEL_RESERVED2_BIT_MASK = 0x40
SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE_LEVEL_ROLL_OVER_BIT_MASK = 0x80

class ZW_SWITCH_TOGGLE_MULTILEVEL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SWITCH_TOGGLE_MULTILEVEL_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SWITCH_TOGGLE_MULTILEVEL_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


class ZW_SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('startLevel', uint8_t),
    ]


class ZW_SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = []

