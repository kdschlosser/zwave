# Node Naming and Location Command Class
# Management
# ==============================
COMMAND_CLASS_NODE_NAMING = 0x77

NODE_NAMING_VERSION = 0x01
# Node Name Set
NODE_NAMING_NODE_NAME_SET = 0x01
# Node Name Get
NODE_NAMING_NODE_NAME_GET = 0x02
# Node Name Report
NODE_NAMING_NODE_NAME_REPORT = 0x03
# Node Location Set
NODE_NAMING_NODE_LOCATION_SET = 0x04
# Node Location Get
NODE_NAMING_NODE_LOCATION_GET = 0x05
# Node Location Report
NODE_NAMING_NODE_LOCATION_REPORT = 0x06

# Values used for Node Naming Node Location Report command
NODE_NAMING_NODE_LOCATION_REPORT_LEVEL_CHAR_PRESENTATION_MASK = 0x07
NODE_NAMING_NODE_LOCATION_REPORT_LEVEL_RESERVED_MASK = 0xF8
NODE_NAMING_NODE_LOCATION_REPORT_LEVEL_RESERVED_SHIFT = 0x03
# Values used for Node Naming Node Location Set command
NODE_NAMING_NODE_LOCATION_SET_LEVEL_CHAR_PRESENTATION_MASK = 0x07
NODE_NAMING_NODE_LOCATION_SET_LEVEL_RESERVED_MASK = 0xF8
NODE_NAMING_NODE_LOCATION_SET_LEVEL_RESERVED_SHIFT = 0x03
# Values used for Node Naming Node Name Report command
NODE_NAMING_NODE_NAME_REPORT_LEVEL_CHAR_PRESENTATION_MASK = 0x07
NODE_NAMING_NODE_NAME_REPORT_LEVEL_RESERVED_MASK = 0xF8
NODE_NAMING_NODE_NAME_REPORT_LEVEL_RESERVED_SHIFT = 0x03
# Values used for Node Naming Node Name Set command
NODE_NAMING_NODE_NAME_SET_LEVEL_CHAR_PRESENTATION_MASK = 0x07
NODE_NAMING_NODE_NAME_SET_LEVEL_RESERVED_MASK = 0xF8
NODE_NAMING_NODE_NAME_SET_LEVEL_RESERVED_SHIFT = 0x03


class ZW_NODE_NAMING_NODE_LOCATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('nodeLocationChar1', uint8_t),
        ('nodeLocationChar2', uint8_t),
        ('nodeLocationChar3', uint8_t),
        ('nodeLocationChar4', uint8_t),
        ('nodeLocationChar5', uint8_t),
        ('nodeLocationChar6', uint8_t),
        ('nodeLocationChar7', uint8_t),
        ('nodeLocationChar8', uint8_t),
        ('nodeLocationChar9', uint8_t),
        ('nodeLocationChar10', uint8_t),
        ('nodeLocationChar11', uint8_t),
        ('nodeLocationChar12', uint8_t),
        ('nodeLocationChar13', uint8_t),
        ('nodeLocationChar14', uint8_t),
        ('nodeLocationChar15', uint8_t),
        ('nodeLocationChar16', uint8_t),
    ]


class ZW_NODE_NAMING_NODE_LOCATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('nodeLocationChar1', uint8_t),
        ('nodeLocationChar2', uint8_t),
        ('nodeLocationChar3', uint8_t),
        ('nodeLocationChar4', uint8_t),
        ('nodeLocationChar5', uint8_t),
        ('nodeLocationChar6', uint8_t),
        ('nodeLocationChar7', uint8_t),
        ('nodeLocationChar8', uint8_t),
        ('nodeLocationChar9', uint8_t),
        ('nodeLocationChar10', uint8_t),
        ('nodeLocationChar11', uint8_t),
        ('nodeLocationChar12', uint8_t),
        ('nodeLocationChar13', uint8_t),
        ('nodeLocationChar14', uint8_t),
        ('nodeLocationChar15', uint8_t),
        ('nodeLocationChar16', uint8_t),
    ]


class ZW_NODE_NAMING_NODE_LOCATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_NODE_NAMING_NODE_NAME_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_NODE_NAMING_NODE_NAME_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('nodeNameChar1', uint8_t),
        ('nodeNameChar2', uint8_t),
        ('nodeNameChar3', uint8_t),
        ('nodeNameChar4', uint8_t),
        ('nodeNameChar5', uint8_t),
        ('nodeNameChar6', uint8_t),
        ('nodeNameChar7', uint8_t),
        ('nodeNameChar8', uint8_t),
        ('nodeNameChar9', uint8_t),
        ('nodeNameChar10', uint8_t),
        ('nodeNameChar11', uint8_t),
        ('nodeNameChar12', uint8_t),
        ('nodeNameChar13', uint8_t),
        ('nodeNameChar14', uint8_t),
        ('nodeNameChar15', uint8_t),
        ('nodeNameChar16', uint8_t),
    ]


class ZW_NODE_NAMING_NODE_NAME_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('level', uint8_t),
        ('nodeNameChar1', uint8_t),
        ('nodeNameChar2', uint8_t),
        ('nodeNameChar3', uint8_t),
        ('nodeNameChar4', uint8_t),
        ('nodeNameChar5', uint8_t),
        ('nodeNameChar6', uint8_t),
        ('nodeNameChar7', uint8_t),
        ('nodeNameChar8', uint8_t),
        ('nodeNameChar9', uint8_t),
        ('nodeNameChar10', uint8_t),
        ('nodeNameChar11', uint8_t),
        ('nodeNameChar12', uint8_t),
        ('nodeNameChar13', uint8_t),
        ('nodeNameChar14', uint8_t),
        ('nodeNameChar15', uint8_t),
        ('nodeNameChar16', uint8_t),
    ]

