# Thermostat Mode Command Class
# Application
# ==============================
COMMAND_CLASS_THERMOSTAT_MODE = 0x40

THERMOSTAT_MODE_VERSION = 0x01
# Thermostat Mode Set
THERMOSTAT_MODE_SET = 0x01
# Thermostat Mode Get
THERMOSTAT_MODE_GET = 0x02
# Thermostat Mode Report
THERMOSTAT_MODE_REPORT = 0x03
# Thermostat Mode Supported Get
THERMOSTAT_MODE_SUPPORTED_GET = 0x04
# Thermostat Mode Supported Report
THERMOSTAT_MODE_SUPPORTED_REPORT = 0x05

# Values used for Thermostat Mode Report command
THERMOSTAT_MODE_REPORT_LEVEL_MODE_MASK = 0x1F
THERMOSTAT_MODE_REPORT_MODE_OFF = 0x00
THERMOSTAT_MODE_REPORT_MODE_HEAT = 0x01
THERMOSTAT_MODE_REPORT_MODE_COOL = 0x02
THERMOSTAT_MODE_REPORT_MODE_AUTO = 0x03
THERMOSTAT_MODE_REPORT_MODE_AUXILIARY_HEAT = 0x04
THERMOSTAT_MODE_REPORT_MODE_RESUME = 0x05
THERMOSTAT_MODE_REPORT_MODE_FAN_ONLY = 0x06
THERMOSTAT_MODE_REPORT_MODE_FURNACE = 0x07
THERMOSTAT_MODE_REPORT_MODE_DRY_AIR = 0x08
THERMOSTAT_MODE_REPORT_MODE_MOIST_AIR = 0x09
THERMOSTAT_MODE_REPORT_MODE_AUTO_CHANGEOVER = 0x0A
THERMOSTAT_MODE_REPORT_LEVEL_RESERVED_MASK = 0xE0
THERMOSTAT_MODE_REPORT_LEVEL_RESERVED_SHIFT = 0x05
# Values used for Thermostat Mode Set command
THERMOSTAT_MODE_SET_LEVEL_MODE_MASK = 0x1F
THERMOSTAT_MODE_SET_MODE_OFF = 0x00
THERMOSTAT_MODE_SET_MODE_HEAT = 0x01
THERMOSTAT_MODE_SET_MODE_COOL = 0x02
THERMOSTAT_MODE_SET_MODE_AUTO = 0x03
THERMOSTAT_MODE_SET_MODE_AUXILIARY_HEAT = 0x04
THERMOSTAT_MODE_SET_MODE_RESUME = 0x05
THERMOSTAT_MODE_SET_MODE_FAN_ONLY = 0x06
THERMOSTAT_MODE_SET_MODE_FURNACE = 0x07
THERMOSTAT_MODE_SET_MODE_DRY_AIR = 0x08
THERMOSTAT_MODE_SET_MODE_MOIST_AIR = 0x09
THERMOSTAT_MODE_SET_MODE_AUTO_CHANGEOVER = 0x0A
THERMOSTAT_MODE_SET_LEVEL_RESERVED_MASK = 0xE0
THERMOSTAT_MODE_SET_LEVEL_RESERVED_SHIFT = 0x05

THERMOSTAT_MODE_VERSION_V2 = 0x02
THERMOSTAT_MODE_GET_V2 = 0x02
THERMOSTAT_MODE_REPORT_V2 = 0x03
THERMOSTAT_MODE_SET_V2 = 0x01
THERMOSTAT_MODE_SUPPORTED_GET_V2 = 0x04
THERMOSTAT_MODE_SUPPORTED_REPORT_V2 = 0x05
# Values used for Thermostat Mode Report command
THERMOSTAT_MODE_REPORT_LEVEL_MODE_MASK_V2 = 0x1F
THERMOSTAT_MODE_REPORT_MODE_OFF_V2 = 0x00
THERMOSTAT_MODE_REPORT_MODE_HEAT_V2 = 0x01
THERMOSTAT_MODE_REPORT_MODE_COOL_V2 = 0x02
THERMOSTAT_MODE_REPORT_MODE_AUTO_V2 = 0x03
THERMOSTAT_MODE_REPORT_MODE_AUXILIARY_HEAT_V2 = 0x04
THERMOSTAT_MODE_REPORT_MODE_RESUME_V2 = 0x05
THERMOSTAT_MODE_REPORT_MODE_FAN_ONLY_V2 = 0x06
THERMOSTAT_MODE_REPORT_MODE_FURNACE_V2 = 0x07
THERMOSTAT_MODE_REPORT_MODE_DRY_AIR_V2 = 0x08
THERMOSTAT_MODE_REPORT_MODE_MOIST_AIR_V2 = 0x09
THERMOSTAT_MODE_REPORT_MODE_AUTO_CHANGEOVER_V2 = 0x0A
THERMOSTAT_MODE_REPORT_MODE_ENERGY_SAVE_HEAT_V2 = 0x0B
THERMOSTAT_MODE_REPORT_MODE_ENERGY_SAVE_COOL_V2 = 0x0C
THERMOSTAT_MODE_REPORT_MODE_AWAY_V2 = 0x0D
THERMOSTAT_MODE_REPORT_LEVEL_RESERVED_MASK_V2 = 0xE0
THERMOSTAT_MODE_REPORT_LEVEL_RESERVED_SHIFT_V2 = 0x05
# Values used for Thermostat Mode Set command
THERMOSTAT_MODE_SET_LEVEL_MODE_MASK_V2 = 0x1F
THERMOSTAT_MODE_SET_MODE_OFF_V2 = 0x00
THERMOSTAT_MODE_SET_MODE_HEAT_V2 = 0x01
THERMOSTAT_MODE_SET_MODE_COOL_V2 = 0x02
THERMOSTAT_MODE_SET_MODE_AUTO_V2 = 0x03
THERMOSTAT_MODE_SET_MODE_AUXILIARY_HEAT_V2 = 0x04
THERMOSTAT_MODE_SET_MODE_RESUME_V2 = 0x05
THERMOSTAT_MODE_SET_MODE_FAN_ONLY_V2 = 0x06
THERMOSTAT_MODE_SET_MODE_FURNACE_V2 = 0x07
THERMOSTAT_MODE_SET_MODE_DRY_AIR_V2 = 0x08
THERMOSTAT_MODE_SET_MODE_MOIST_AIR_V2 = 0x09
THERMOSTAT_MODE_SET_MODE_AUTO_CHANGEOVER_V2 = 0x0A
THERMOSTAT_MODE_SET_MODE_ENERGY_SAVE_HEAT_V2 = 0x0B
THERMOSTAT_MODE_SET_MODE_ENERGY_SAVE_COOL_V2 = 0x0C
THERMOSTAT_MODE_SET_MODE_AWAY_V2 = 0x0D
THERMOSTAT_MODE_SET_LEVEL_RESERVED_MASK_V2 = 0xE0
THERMOSTAT_MODE_SET_LEVEL_RESERVED_SHIFT_V2 = 0x05

THERMOSTAT_MODE_VERSION_V3 = 0x03
THERMOSTAT_MODE_GET_V3 = 0x02
THERMOSTAT_MODE_REPORT_V3 = 0x03
THERMOSTAT_MODE_SET_V3 = 0x01
THERMOSTAT_MODE_SUPPORTED_GET_V3 = 0x04
THERMOSTAT_MODE_SUPPORTED_REPORT_V3 = 0x05
# Values used for Thermostat Mode Report command
THERMOSTAT_MODE_REPORT_LEVEL_MODE_MASK_V3 = 0x1F
THERMOSTAT_MODE_REPORT_MODE_OFF_V3 = 0x00
THERMOSTAT_MODE_REPORT_MODE_HEAT_V3 = 0x01
THERMOSTAT_MODE_REPORT_MODE_COOL_V3 = 0x02
THERMOSTAT_MODE_REPORT_MODE_AUTO_V3 = 0x03
THERMOSTAT_MODE_REPORT_MODE_AUXILIARY_HEAT_V3 = 0x04
THERMOSTAT_MODE_REPORT_MODE_RESUME_V3 = 0x05
THERMOSTAT_MODE_REPORT_MODE_FAN_ONLY_V3 = 0x06
THERMOSTAT_MODE_REPORT_MODE_FURNACE_V3 = 0x07
THERMOSTAT_MODE_REPORT_MODE_DRY_AIR_V3 = 0x08
THERMOSTAT_MODE_REPORT_MODE_MOIST_AIR_V3 = 0x09
THERMOSTAT_MODE_REPORT_MODE_AUTO_CHANGEOVER_V3 = 0x0A
THERMOSTAT_MODE_REPORT_MODE_ENERGY_SAVE_HEAT_V3 = 0x0B
THERMOSTAT_MODE_REPORT_MODE_ENERGY_SAVE_COOL_V3 = 0x0C
THERMOSTAT_MODE_REPORT_MODE_AWAY_V3 = 0x0D
THERMOSTAT_MODE_REPORT_MODE_RESERVED_V3 = 0x0E
THERMOSTAT_MODE_REPORT_MODE_FULL_POWER_V3 = 0x0F
THERMOSTAT_MODE_REPORT_MODE_RESERVED0_V3 = 0x10
THERMOSTAT_MODE_REPORT_MODE_RESERVED1_V3 = 0x11
THERMOSTAT_MODE_REPORT_MODE_RESERVED2_V3 = 0x12
THERMOSTAT_MODE_REPORT_MODE_RESERVED3_V3 = 0x13
THERMOSTAT_MODE_REPORT_MODE_RESERVED4_V3 = 0x14
THERMOSTAT_MODE_REPORT_MODE_RESERVED5_V3 = 0x15
THERMOSTAT_MODE_REPORT_MODE_RESERVED6_V3 = 0x16
THERMOSTAT_MODE_REPORT_MODE_RESERVED7_V3 = 0x17
THERMOSTAT_MODE_REPORT_MODE_RESERVED8_V3 = 0x18
THERMOSTAT_MODE_REPORT_MODE_RESERVED9_V3 = 0x19
THERMOSTAT_MODE_REPORT_MODE_RESERVEDA_V3 = 0x1A
THERMOSTAT_MODE_REPORT_MODE_RESERVEDB_V3 = 0x1B
THERMOSTAT_MODE_REPORT_MODE_RESERVEDC_V3 = 0x1C
THERMOSTAT_MODE_REPORT_MODE_RESERVEDD_V3 = 0x1D
THERMOSTAT_MODE_REPORT_MODE_RESERVEDE_V3 = 0x1E
THERMOSTAT_MODE_REPORT_MODE_MANUFACTURER_SPECIFC_V3 = 0x1F
THERMOSTAT_MODE_REPORT_LEVEL_NO_OF_MANUFACTURER_DATA_FIELDS_MASK_V3 = 0xE0
THERMOSTAT_MODE_REPORT_LEVEL_NO_OF_MANUFACTURER_DATA_FIELDS_SHIFT_V3 = 0x05
# Values used for Thermostat Mode Set command
THERMOSTAT_MODE_SET_LEVEL_MODE_MASK_V3 = 0x1F
THERMOSTAT_MODE_SET_MODE_OFF_V3 = 0x00
THERMOSTAT_MODE_SET_MODE_HEAT_V3 = 0x01
THERMOSTAT_MODE_SET_MODE_COOL_V3 = 0x02
THERMOSTAT_MODE_SET_MODE_AUTO_V3 = 0x03
THERMOSTAT_MODE_SET_MODE_AUXILIARY_HEAT_V3 = 0x04
THERMOSTAT_MODE_SET_MODE_RESUME_V3 = 0x05
THERMOSTAT_MODE_SET_MODE_FAN_ONLY_V3 = 0x06
THERMOSTAT_MODE_SET_MODE_FURNACE_V3 = 0x07
THERMOSTAT_MODE_SET_MODE_DRY_AIR_V3 = 0x08
THERMOSTAT_MODE_SET_MODE_MOIST_AIR_V3 = 0x09
THERMOSTAT_MODE_SET_MODE_AUTO_CHANGEOVER_V3 = 0x0A
THERMOSTAT_MODE_SET_MODE_ENERGY_SAVE_HEAT_V3 = 0x0B
THERMOSTAT_MODE_SET_MODE_ENERGY_SAVE_COOL_V3 = 0x0C
THERMOSTAT_MODE_SET_MODE_AWAY_V3 = 0x0D
THERMOSTAT_MODE_SET_MODE_RESERVED_V3 = 0x0E
THERMOSTAT_MODE_SET_MODE_FULL_POWER_V3 = 0x0F
THERMOSTAT_MODE_SET_MODE_RESERVED0_V3 = 0x10
THERMOSTAT_MODE_SET_MODE_RESERVED1_V3 = 0x11
THERMOSTAT_MODE_SET_MODE_RESERVED2_V3 = 0x12
THERMOSTAT_MODE_SET_MODE_RESERVED3_V3 = 0x13
THERMOSTAT_MODE_SET_MODE_RESERVED4_V3 = 0x14
THERMOSTAT_MODE_SET_MODE_RESERVED5_V3 = 0x15
THERMOSTAT_MODE_SET_MODE_RESERVED6_V3 = 0x16
THERMOSTAT_MODE_SET_MODE_RESERVED7_V3 = 0x17
THERMOSTAT_MODE_SET_MODE_RESERVED8_V3 = 0x18
THERMOSTAT_MODE_SET_MODE_RESERVED9_V3 = 0x19
THERMOSTAT_MODE_SET_MODE_RESERVEDA_V3 = 0x1A
THERMOSTAT_MODE_SET_MODE_RESERVEDB_V3 = 0x1B
THERMOSTAT_MODE_SET_MODE_RESERVEDC_V3 = 0x1C
THERMOSTAT_MODE_SET_MODE_RESERVEDD_V3 = 0x1D
THERMOSTAT_MODE_SET_MODE_RESERVEDE_V3 = 0x1E
THERMOSTAT_MODE_SET_MODE_MANUFACTURER_SPECIFC_V3 = 0x1F
THERMOSTAT_MODE_SET_LEVEL_NO_OF_MANUFACTURER_DATA_FIELDS_MASK_V3 = 0xE0
THERMOSTAT_MODE_SET_LEVEL_NO_OF_MANUFACTURER_DATA_FIELDS_SHIFT_V3 = 0x05


class ZW_THERMOSTAT_MODE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_THERMOSTAT_MODE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_THERMOSTAT_MODE_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('bitMask1', uint8_t)]


class ZW_THERMOSTAT_MODE_GET_V2_FRAME(ZW_THERMOSTAT_MODE_GET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_REPORT_V2_FRAME(ZW_THERMOSTAT_MODE_REPORT_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_SET_V2_FRAME(ZW_THERMOSTAT_MODE_SET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_SUPPORTED_GET_V2_FRAME(ZW_THERMOSTAT_MODE_SUPPORTED_GET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_SUPPORTED_REPORT_V2_FRAME(ZW_THERMOSTAT_MODE_SUPPORTED_REPORT_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_GET_V3_FRAME(ZW_THERMOSTAT_MODE_GET_V2_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_REPORT_V3_FRAME(ZW_THERMOSTAT_MODE_REPORT_V2_FRAME):
    _fields_ = [('manufacturerData1', uint8_t)]


class ZW_THERMOSTAT_MODE_SET_V3_FRAME(ZW_THERMOSTAT_MODE_SET_V2_FRAME):
    _fields_ = [('manufacturerData1', uint8_t)]


class ZW_THERMOSTAT_MODE_SUPPORTED_GET_V3_FRAME(ZW_THERMOSTAT_MODE_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_MODE_SUPPORTED_REPORT_V3_FRAME(ZW_THERMOSTAT_MODE_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = []
