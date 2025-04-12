# Climate Control Schedule Command Class
# Application
# ==============================
COMMAND_CLASS_CLIMATE_CONTROL_SCHEDULE = 0x46

CLIMATE_CONTROL_SCHEDULE_VERSION = 0x01
# Schedule Set
SCHEDULE_SET = 0x01
# Schedule Get
SCHEDULE_GET = 0x02
# Schedule Report
SCHEDULE_REPORT = 0x03
# Schedule Changed Get
SCHEDULE_CHANGED_GET = 0x04
# Schedule Changed Report
SCHEDULE_CHANGED_REPORT = 0x05
# Schedule Override Set
SCHEDULE_OVERRIDE_SET = 0x06
# Schedule Override Get
SCHEDULE_OVERRIDE_GET = 0x07
# Schedule Override Report
SCHEDULE_OVERRIDE_REPORT = 0x08
# Values used for Schedule Get command
SCHEDULE_GET_PROPERTIES1_WEEKDAY_MASK = 0x07
SCHEDULE_GET_PROPERTIES1_RESERVED_MASK = 0xF8
SCHEDULE_GET_PROPERTIES1_RESERVED_SHIFT = 0x03
# Values used for Schedule Override Report command
SCHEDULE_OVERRIDE_REPORT_PROPERTIES1_OVERRIDE_TYPE_MASK = 0x03
SCHEDULE_OVERRIDE_REPORT_OVERRIDE_TYPE_NO_OVERRIDE = 0x00
SCHEDULE_OVERRIDE_REPORT_OVERRIDE_TYPE_TEMPORARY_OVERRIDE = 0x01
SCHEDULE_OVERRIDE_REPORT_OVERRIDE_TYPE_PERMANENT_OVERRIDE = 0x02
SCHEDULE_OVERRIDE_REPORT_OVERRIDE_TYPE_RESERVED = 0x03
SCHEDULE_OVERRIDE_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
SCHEDULE_OVERRIDE_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
SCHEDULE_OVERRIDE_REPORT_FROST_PROTECTION = 0x79
SCHEDULE_OVERRIDE_REPORT_ENERGY_SAVING_MODE = 0x7A
SCHEDULE_OVERRIDE_REPORT_UNUSED_STATE = 0x7F
# Values used for Schedule Override Set command
SCHEDULE_OVERRIDE_SET_PROPERTIES1_OVERRIDE_TYPE_MASK = 0x03
SCHEDULE_OVERRIDE_SET_OVERRIDE_TYPE_NO_OVERRIDE = 0x00
SCHEDULE_OVERRIDE_SET_OVERRIDE_TYPE_TEMPORARY_OVERRIDE = 0x01
SCHEDULE_OVERRIDE_SET_OVERRIDE_TYPE_PERMANENT_OVERRIDE = 0x02
SCHEDULE_OVERRIDE_SET_OVERRIDE_TYPE_RESERVED = 0x03
SCHEDULE_OVERRIDE_SET_PROPERTIES1_RESERVED_MASK = 0xFC
SCHEDULE_OVERRIDE_SET_PROPERTIES1_RESERVED_SHIFT = 0x02
SCHEDULE_OVERRIDE_SET_FROST_PROTECTION = 0x79
SCHEDULE_OVERRIDE_SET_ENERGY_SAVING_MODE = 0x7A
SCHEDULE_OVERRIDE_SET_UNUSED_STATE = 0x7F
# Values used for Schedule Report command
SCHEDULE_REPORT_PROPERTIES1_WEEKDAY_MASK = 0x07
SCHEDULE_REPORT_PROPERTIES1_RESERVED_MASK = 0xF8
SCHEDULE_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x03
# Values used for Schedule Set command
SCHEDULE_SET_PROPERTIES1_WEEKDAY_MASK = 0x07
SCHEDULE_SET_PROPERTIES1_RESERVED_MASK = 0xF8
SCHEDULE_SET_PROPERTIES1_RESERVED_SHIFT = 0x03





class ZW_SCHEDULE_CHANGED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SCHEDULE_CHANGED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('changecounter', uint8_t)]


class ZW_SCHEDULE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_SCHEDULE_OVERRIDE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SCHEDULE_OVERRIDE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('overrideState', uint8_t),
    ]


class ZW_SCHEDULE_OVERRIDE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('overrideState', uint8_t),
    ]


class ZW_SCHEDULE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('switchpoint01', uint8_t),
        ('switchpoint02', uint8_t),
        ('switchpoint03', uint8_t),
        ('switchpoint11', uint8_t),
        ('switchpoint12', uint8_t),
        ('switchpoint13', uint8_t),
        ('switchpoint21', uint8_t),
        ('switchpoint22', uint8_t),
        ('switchpoint23', uint8_t),
        ('switchpoint31', uint8_t),
        ('switchpoint32', uint8_t),
        ('switchpoint33', uint8_t),
        ('switchpoint41', uint8_t),
        ('switchpoint42', uint8_t),
        ('switchpoint43', uint8_t),
        ('switchpoint51', uint8_t),
        ('switchpoint52', uint8_t),
        ('switchpoint53', uint8_t),
        ('switchpoint61', uint8_t),
        ('switchpoint62', uint8_t),
        ('switchpoint63', uint8_t),
        ('switchpoint71', uint8_t),
        ('switchpoint72', uint8_t),
        ('switchpoint73', uint8_t),
        ('switchpoint81', uint8_t),
        ('switchpoint82', uint8_t),
        ('switchpoint83', uint8_t),
    ]


class ZW_SCHEDULE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('switchpoint01', uint8_t),
        ('switchpoint02', uint8_t),
        ('switchpoint03', uint8_t),
        ('switchpoint11', uint8_t),
        ('switchpoint12', uint8_t),
        ('switchpoint13', uint8_t),
        ('switchpoint21', uint8_t),
        ('switchpoint22', uint8_t),
        ('switchpoint23', uint8_t),
        ('switchpoint31', uint8_t),
        ('switchpoint32', uint8_t),
        ('switchpoint33', uint8_t),
        ('switchpoint41', uint8_t),
        ('switchpoint42', uint8_t),
        ('switchpoint43', uint8_t),
        ('switchpoint51', uint8_t),
        ('switchpoint52', uint8_t),
        ('switchpoint53', uint8_t),
        ('switchpoint61', uint8_t),
        ('switchpoint62', uint8_t),
        ('switchpoint63', uint8_t),
        ('switchpoint71', uint8_t),
        ('switchpoint72', uint8_t),
        ('switchpoint73', uint8_t),
        ('switchpoint81', uint8_t),
        ('switchpoint82', uint8_t),
        ('switchpoint83', uint8_t),
    ]


