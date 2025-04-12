# Thermostat Fan State Command Class
# Application
# ==============================
COMMAND_CLASS_THERMOSTAT_FAN_STATE = 0x45

THERMOSTAT_FAN_STATE_VERSION = 0x01
# Thermostat Fan State Get
THERMOSTAT_FAN_STATE_GET = 0x02
# Thermostat Fan State Report
THERMOSTAT_FAN_STATE_REPORT = 0x03

# Values used for Thermostat Fan State Report command
THERMOSTAT_FAN_STATE_REPORT_LEVEL_FAN_OPERATING_STATE_MASK = 0x0F
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_IDLE = 0x00
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RUNNING = 0x01
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RUNNING_HIGH = 0x02
THERMOSTAT_FAN_STATE_REPORT_LEVEL_RESERVED_MASK = 0xF0
THERMOSTAT_FAN_STATE_REPORT_LEVEL_RESERVED_SHIFT = 0x04

THERMOSTAT_FAN_STATE_VERSION_V2 = 0x02
THERMOSTAT_FAN_STATE_GET_V2 = 0x02
THERMOSTAT_FAN_STATE_REPORT_V2 = 0x03
# Values used for Thermostat Fan State Report command
THERMOSTAT_FAN_STATE_REPORT_LEVEL_FAN_OPERATING_STATE_MASK_V2 = 0x0F
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_IDLE_V2 = 0x00
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RUNNING_V2 = 0x01
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RUNNING_HIGH_V2 = 0x02
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RUNNING_MEDIUM_V2 = 0x03
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_CIRCULATION_V2 = 0x04
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_HUMIDITY_CIRCULATION_V2 = 0x05
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_RIGHT_LEFT_CIRCULATION_V2 = 0x06
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_UP_DOWN_CIRCULATION_V2 = 0x07
THERMOSTAT_FAN_STATE_REPORT_FAN_OPERATING_STATE_QUIET_CIRCULATION_V2 = 0x08
THERMOSTAT_FAN_STATE_REPORT_LEVEL_RESERVED_MASK_V2 = 0xF0
THERMOSTAT_FAN_STATE_REPORT_LEVEL_RESERVED_SHIFT_V2 = 0x04


class ZW_THERMOSTAT_FAN_STATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_STATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('level', uint8_t)]


class ZW_THERMOSTAT_FAN_STATE_GET_V2_FRAME(ZW_THERMOSTAT_FAN_STATE_GET_FRAME):
    _fields_ = []


class ZW_THERMOSTAT_FAN_STATE_REPORT_V2_FRAME(ZW_THERMOSTAT_FAN_STATE_REPORT_FRAME):
    _fields_ = []

