# Thermostat Fan Mode Command Class
# Application
# ==============================
COMMAND_CLASS_THERMOSTAT_FAN_MODE = 0x44

THERMOSTAT_FAN_MODE_VERSION = 0x01
# Thermostat Fan Mode Set
THERMOSTAT_FAN_MODE_SET = 0x01
# Thermostat Fan Mode Get
THERMOSTAT_FAN_MODE_GET = 0x02
# Thermostat Fan Mode Report
THERMOSTAT_FAN_MODE_REPORT = 0x03
# Thermostat Fan Mode Supported Get
THERMOSTAT_FAN_MODE_SUPPORTED_GET = 0x04
# Thermostat Fan Mode Supported Report
THERMOSTAT_FAN_MODE_SUPPORTED_REPORT = 0x05

# Values used for Thermostat Fan Mode Report command
THERMOSTAT_FAN_MODE_REPORT_LEVEL_FAN_MODE_MASK = 0x0F
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_LOW = 0x00
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LOW = 0x01
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_HIGH = 0x02
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HIGH = 0x03
THERMOSTAT_FAN_MODE_REPORT_LEVEL_RESERVED_MASK = 0xF0
THERMOSTAT_FAN_MODE_REPORT_LEVEL_RESERVED_SHIFT = 0x04
# Values used for Thermostat Fan Mode Set command
THERMOSTAT_FAN_MODE_SET_LEVEL_FAN_MODE_MASK = 0x0F
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_LOW = 0x00
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LOW = 0x01
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_HIGH = 0x02
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HIGH = 0x03
THERMOSTAT_FAN_MODE_SET_LEVEL_RESERVED_MASK = 0xF0
THERMOSTAT_FAN_MODE_SET_LEVEL_RESERVED_SHIFT = 0x04

THERMOSTAT_FAN_MODE_VERSION_V2 = 0x02
THERMOSTAT_FAN_MODE_GET_V2 = 0x02
THERMOSTAT_FAN_MODE_REPORT_V2 = 0x03
THERMOSTAT_FAN_MODE_SET_V2 = 0x01
THERMOSTAT_FAN_MODE_SUPPORTED_GET_V2 = 0x04
THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V2 = 0x05
# Values used for Thermostat Fan Mode Report command
THERMOSTAT_FAN_MODE_REPORT_LEVEL_FAN_MODE_MASK_V2 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_LOW_V2 = 0x00
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LOW_V2 = 0x01
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_HIGH_V2 = 0x02
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HIGH_V2 = 0x03
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_MEDIUM_V2 = 0x04
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_MEDIUM_V2 = 0x05
THERMOSTAT_FAN_MODE_REPORT_LEVEL_RESERVED_MASK_V2 = 0xF0
THERMOSTAT_FAN_MODE_REPORT_LEVEL_RESERVED_SHIFT_V2 = 0x04
# Values used for Thermostat Fan Mode Set command
THERMOSTAT_FAN_MODE_SET_LEVEL_FAN_MODE_MASK_V2 = 0x0F
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_LOW_V2 = 0x00
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LOW_V2 = 0x01
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_HIGH_V2 = 0x02
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HIGH_V2 = 0x03
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_MEDIUM_V2 = 0x04
THERMOSTAT_FAN_MODE_SET_FAN_MODE_MEDIUM_V2 = 0x05
THERMOSTAT_FAN_MODE_SET_LEVEL_RESERVED_MASK_V2 = 0x70
THERMOSTAT_FAN_MODE_SET_LEVEL_RESERVED_SHIFT_V2 = 0x04
THERMOSTAT_FAN_MODE_SET_LEVEL_OFF_BIT_MASK_V2 = 0x80

THERMOSTAT_FAN_MODE_VERSION_V3 = 0x03
THERMOSTAT_FAN_MODE_GET_V3 = 0x02
THERMOSTAT_FAN_MODE_REPORT_V3 = 0x03
THERMOSTAT_FAN_MODE_SET_V3 = 0x01
THERMOSTAT_FAN_MODE_SUPPORTED_GET_V3 = 0x04
THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V3 = 0x05
# Values used for Thermostat Fan Mode Report command
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_FAN_MODE_MASK_V3 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_LOW_V3 = 0x00
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LOW_V3 = 0x01
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_HIGH_V3 = 0x02
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HIGH_V3 = 0x03
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_MEDIUM_V3 = 0x04
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_MEDIUM_V3 = 0x05
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_CIRCULATION_V3 = 0x06
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HUMIDITY_V3 = 0x07
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0x70
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x04
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_OFF_BIT_MASK_V3 = 0x80
# Values used for Thermostat Fan Mode Set command
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_FAN_MODE_MASK_V3 = 0x0F
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_LOW_V3 = 0x00
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LOW_V3 = 0x01
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_HIGH_V3 = 0x02
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HIGH_V3 = 0x03
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_MEDIUM_V3 = 0x04
THERMOSTAT_FAN_MODE_SET_FAN_MODE_MEDIUM_V3 = 0x05
THERMOSTAT_FAN_MODE_SET_FAN_MODE_CIRCULATION_V3 = 0x06
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HUMIDITY_V3 = 0x07
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_MASK_V3 = 0x70
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_SHIFT_V3 = 0x04
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_OFF_BIT_MASK_V3 = 0x80

THERMOSTAT_FAN_MODE_VERSION_V4 = 0x04
THERMOSTAT_FAN_MODE_GET_V4 = 0x02
THERMOSTAT_FAN_MODE_REPORT_V4 = 0x03
THERMOSTAT_FAN_MODE_SET_V4 = 0x01
THERMOSTAT_FAN_MODE_SUPPORTED_GET_V4 = 0x04
THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V4 = 0x05
# Values used for Thermostat Fan Mode Report command
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_FAN_MODE_MASK_V4 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_LOW_V4 = 0x00
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LOW_V4 = 0x01
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_HIGH_V4 = 0x02
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HIGH_V4 = 0x03
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_MEDIUM_V4 = 0x04
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_MEDIUM_V4 = 0x05
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_CIRCULATION_V4 = 0x06
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HUMIDITY_V4 = 0x07
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LEFT_RIGHT_V4 = 0x08
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_UP_DOWN_V4 = 0x09
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_QUIET_V4 = 0x0A
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDB_V4 = 0x0B
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDC_V4 = 0x0C
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDD_V4 = 0x0D
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDE_V4 = 0x0E
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDF_V4 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_MASK_V4 = 0x70
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_SHIFT_V4 = 0x04
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_OFF_BIT_MASK_V4 = 0x80
# Values used for Thermostat Fan Mode Set command
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_FAN_MODE_MASK_V4 = 0x0F
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_LOW_V4 = 0x00
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LOW_V4 = 0x01
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_HIGH_V4 = 0x02
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HIGH_V4 = 0x03
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_MEDIUM_V4 = 0x04
THERMOSTAT_FAN_MODE_SET_FAN_MODE_MEDIUM_V4 = 0x05
THERMOSTAT_FAN_MODE_SET_FAN_MODE_CIRCULATION_V4 = 0x06
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HUMIDITY_V4 = 0x07
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LEFT_RIGHT_V4 = 0x08
THERMOSTAT_FAN_MODE_SET_FAN_MODE_UP_DOWN_V4 = 0x09
THERMOSTAT_FAN_MODE_SET_FAN_MODE_QUIET_V4 = 0x0A
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDB_V4 = 0x0B
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDC_V4 = 0x0C
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDD_V4 = 0x0D
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDE_V4 = 0x0E
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDF_V4 = 0x0F
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_MASK_V4 = 0x70
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_SHIFT_V4 = 0x04
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_OFF_BIT_MASK_V4 = 0x80

THERMOSTAT_FAN_MODE_VERSION_V5 = 0x05
THERMOSTAT_FAN_MODE_GET_V5 = 0x02
THERMOSTAT_FAN_MODE_REPORT_V5 = 0x03
THERMOSTAT_FAN_MODE_SET_V5 = 0x01
THERMOSTAT_FAN_MODE_SUPPORTED_GET_V5 = 0x04
THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V5 = 0x05
# Values used for Thermostat Fan Mode Report command
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_FAN_MODE_MASK_V5 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_LOW_V5 = 0x00
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LOW_V5 = 0x01
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_HIGH_V5 = 0x02
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HIGH_V5 = 0x03
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_AUTO_MEDIUM_V5 = 0x04
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_MEDIUM_V5 = 0x05
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_CIRCULATION_V5 = 0x06
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_HUMIDITY_V5 = 0x07
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_LEFT_RIGHT_V5 = 0x08
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_UP_DOWN_V5 = 0x09
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_QUIET_V5 = 0x0A
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_EXTERNAL_CIRCULATION_V5 = 0x0B
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDC_V5 = 0x0C
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDD_V5 = 0x0D
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDE_V5 = 0x0E
THERMOSTAT_FAN_MODE_REPORT_FAN_MODE_RESERVEDF_V5 = 0x0F
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_MASK_V5 = 0x70
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_RESERVED_SHIFT_V5 = 0x04
THERMOSTAT_FAN_MODE_REPORT_PROPERTIES1_OFF_BIT_MASK_V5 = 0x80
# Values used for Thermostat Fan Mode Set command
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_FAN_MODE_MASK_V5 = 0x0F
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_LOW_V5 = 0x00
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LOW_V5 = 0x01
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_HIGH_V5 = 0x02
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HIGH_V5 = 0x03
THERMOSTAT_FAN_MODE_SET_FAN_MODE_AUTO_MEDIUM_V5 = 0x04
THERMOSTAT_FAN_MODE_SET_FAN_MODE_MEDIUM_V5 = 0x05
THERMOSTAT_FAN_MODE_SET_FAN_MODE_CIRCULATION_V5 = 0x06
THERMOSTAT_FAN_MODE_SET_FAN_MODE_HUMIDITY_V5 = 0x07
THERMOSTAT_FAN_MODE_SET_FAN_MODE_LEFT_RIGHT_V5 = 0x08
THERMOSTAT_FAN_MODE_SET_FAN_MODE_UP_DOWN_V5 = 0x09
THERMOSTAT_FAN_MODE_SET_FAN_MODE_QUIET_V5 = 0x0A
THERMOSTAT_FAN_MODE_SET_FAN_MODE_EXTERNAL_CIRCULATION_V5 = 0x0B
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDC_V5 = 0x0C
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDD_V5 = 0x0D
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDE_V5 = 0x0E
THERMOSTAT_FAN_MODE_SET_FAN_MODE_RESERVEDF_V5 = 0x0F
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_MASK_V5 = 0x70
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_RESERVED_SHIFT_V5 = 0x04
THERMOSTAT_FAN_MODE_SET_PROPERTIES1_OFF_BIT_MASK_V5 = 0x80


class ZW_THERMOSTAT_FAN_MODE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_THERMOSTAT_FAN_MODE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('bitMask1', uint8_t)]


class ZW_THERMOSTAT_FAN_MODE_GET_V2_FRAME(ZW_THERMOSTAT_FAN_MODE_GET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_REPORT_V2_FRAME(ZW_THERMOSTAT_FAN_MODE_REPORT_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SET_V2_FRAME(ZW_THERMOSTAT_FAN_MODE_SET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V2_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V2_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_GET_V3_FRAME(ZW_THERMOSTAT_FAN_MODE_GET_V2_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_REPORT_V3_FRAME(ZW_THERMOSTAT_FAN_MODE_REPORT_V2_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_THERMOSTAT_FAN_MODE_SET_V3_FRAME(ZW_THERMOSTAT_FAN_MODE_SET_V2_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V3_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V3_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_GET_V4_FRAME(ZW_THERMOSTAT_FAN_MODE_GET_V3_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_REPORT_V4_FRAME(ZW_THERMOSTAT_FAN_MODE_REPORT_V3_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SET_V4_FRAME(ZW_THERMOSTAT_FAN_MODE_SET_V3_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V4_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V3_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V4_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V3_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_GET_V5_FRAME(ZW_THERMOSTAT_FAN_MODE_GET_V4_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_REPORT_V5_FRAME(ZW_THERMOSTAT_FAN_MODE_REPORT_V4_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SET_V5_FRAME(ZW_THERMOSTAT_FAN_MODE_SET_V4_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V5_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET_V4_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V5_FRAME(ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT_V4_FRAME):
    _fields_ = []

