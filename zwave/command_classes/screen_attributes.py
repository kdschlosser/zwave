# Screen Attributes Command Class
# Application
# ==============================
COMMAND_CLASS_SCREEN_ATTRIBUTES = 0x93

SCREEN_ATTRIBUTES_VERSION = 0x01
# Screen Attributes Get
SCREEN_ATTRIBUTES_GET = 0x01
# Screen Attributes Report
SCREEN_ATTRIBUTES_REPORT = 0x02

# Values used for Screen Attributes Report command
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_NUMBER_OF_LINES_MASK = 0x1F
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05

SCREEN_ATTRIBUTES_VERSION_V2 = 0x02
SCREEN_ATTRIBUTES_GET_V2 = 0x01
SCREEN_ATTRIBUTES_REPORT_V2 = 0x02
SCREEN_ATTRIBUTES_REPORT_LEGACY_V2 = 0x03
# Values used for Screen Attributes Report command
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_NUMBER_OF_LINES_MASK_V2 = 0x1F
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_ESCAPE_SEQUENCE_BIT_MASK_V2 = 0x20
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xC0
SCREEN_ATTRIBUTES_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x06
# Values used for Screen Attributes Report Legacy command
SCREEN_ATTRIBUTES_REPORT_LEGACY_PROPERTIES1_NUMBER_OF_LINES_MASK_V2 = 0x1F
SCREEN_ATTRIBUTES_REPORT_LEGACY_PROPERTIES1_ESCAPE_SEQUENCE_BIT_MASK_V2 = 0x20
SCREEN_ATTRIBUTES_REPORT_LEGACY_PROPERTIES1_RESERVED_MASK_V2 = 0xC0
SCREEN_ATTRIBUTES_REPORT_LEGACY_PROPERTIES1_RESERVED_SHIFT_V2 = 0x06

class ZW_SCREEN_ATTRIBUTES_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SCREEN_ATTRIBUTES_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('numberOfCharactersPerLine', uint8_t),
        ('sizeOfLineBuffer', uint8_t),
        ('numericalPresentationOfACharacter', uint8_t),
    ]


class ZW_SCREEN_ATTRIBUTES_GET_V2_FRAME(ZW_SCREEN_ATTRIBUTES_GET_FRAME):
    _fields_ = []


class ZW_SCREEN_ATTRIBUTES_REPORT_V2_FRAME(ZW_SCREEN_ATTRIBUTES_REPORT_FRAME):
    _fields_ = [('screenTimeout', uint8_t)]


class ZW_SCREEN_ATTRIBUTES_REPORT_LEGACY_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('numberOfCharactersPerLine', uint8_t),
        ('sizeOfLineBuffer', uint8_t),
        ('numericalPresentationOfACharacter', uint8_t),
        ('screenTimeout', uint8_t),
    ]

