# Binary Sensor Command Class
# Application
# ==============================
COMMAND_CLASS_SENSOR_BINARY = 0x30

SENSOR_BINARY_VERSION = 0x01
# Binary Sensor Get
SENSOR_BINARY_GET = 0x02

# Values used for Sensor Binary Report command
SENSOR_BINARY_REPORT_IDLE = 0x00
SENSOR_BINARY_REPORT_DETECTED_AN_EVENT = 0xFF

SENSOR_BINARY_VERSION_V2 = 0x02
SENSOR_BINARY_GET_V2 = 0x02
# Binary Sensor Set
SENSOR_BINARY_REPORT_V2 = 0x03
# Binary Sensor Get supported Sensor
SENSOR_BINARY_SUPPORTED_GET_SENSOR_V2 = 0x01
# Binary Sensor Supported Sensor Report
SENSOR_BINARY_SUPPORTED_SENSOR_REPORT_V2 = 0x04

# Values used for Sensor Binary Report command
SENSOR_BINARY_REPORT_IDLE_V2 = 0x00
SENSOR_BINARY_REPORT_DETECTED_AN_EVENT_V2 = 0xFF

class ZW_SENSOR_BINARY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SENSOR_BINARY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('sensorValue', uint8_t)]


class ZW_SENSOR_BINARY_GET_V2_FRAME(ZW_SENSOR_BINARY_GET_FRAME):
    _fields_ = [('sensorType', uint8_t)]


class ZW_SENSOR_BINARY_REPORT_V2_FRAME(ZW_SENSOR_BINARY_REPORT_FRAME):
    _fields_ = [('sensorType', uint8_t)]


class ZW_SENSOR_BINARY_SUPPORTED_GET_SENSOR_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SENSOR_BINARY_SUPPORTED_SENSOR_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('bitMask1', uint8_t)]
