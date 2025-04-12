# Grouping Name Command Class
# Management
# ==============================
COMMAND_CLASS_GROUPING_NAME = 0x7B

GROUPING_NAME_VERSION = 0x01
# Grouping Name Set
GROUPING_NAME_SET = 0x01
# Grouping Name Get
GROUPING_NAME_GET = 0x02
# Grouping Name Report
GROUPING_NAME_REPORT = 0x03

# Values used for Grouping Name Report command
GROUPING_NAME_REPORT_PROPERTIES1_CHAR_PRESENTATION_MASK = 0x07
GROUPING_NAME_REPORT_PROPERTIES1_RESERVED_MASK = 0xF8
GROUPING_NAME_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x03
# Values used for Grouping Name Set command
GROUPING_NAME_SET_PROPERTIES1_CHAR_PRESENTATION_MASK = 0x07
GROUPING_NAME_SET_PROPERTIES1_RESERVED_MASK = 0xF8
GROUPING_NAME_SET_PROPERTIES1_RESERVED_SHIFT = 0x03



class ZW_GROUPING_NAME_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('groupingIdentifier', uint8_t)]


class ZW_GROUPING_NAME_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('properties1', uint8_t),
        ('groupingName1', uint8_t),
        ('groupingName2', uint8_t),
        ('groupingName3', uint8_t),
        ('groupingName4', uint8_t),
        ('groupingName5', uint8_t),
        ('groupingName6', uint8_t),
        ('groupingName7', uint8_t),
        ('groupingName8', uint8_t),
        ('groupingName9', uint8_t),
        ('groupingName10', uint8_t),
        ('groupingName11', uint8_t),
        ('groupingName12', uint8_t),
        ('groupingName13', uint8_t),
        ('groupingName14', uint8_t),
        ('groupingName15', uint8_t),
        ('groupingName16', uint8_t),
    ]


class ZW_GROUPING_NAME_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('properties1', uint8_t),
        ('groupingName1', uint8_t),
        ('groupingName2', uint8_t),
        ('groupingName3', uint8_t),
        ('groupingName4', uint8_t),
        ('groupingName5', uint8_t),
        ('groupingName6', uint8_t),
        ('groupingName7', uint8_t),
        ('groupingName8', uint8_t),
        ('groupingName9', uint8_t),
        ('groupingName10', uint8_t),
        ('groupingName11', uint8_t),
        ('groupingName12', uint8_t),
        ('groupingName13', uint8_t),
        ('groupingName14', uint8_t),
        ('groupingName15', uint8_t),
        ('groupingName16', uint8_t),
    ]


