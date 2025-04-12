# Alarm Sensor Command Class
# Application
# ==============================
COMMAND_CLASS_SENSOR_ALARM = 0x9C

SENSOR_ALARM_VERSION = 0x01
# Alarm Sensor Get
SENSOR_ALARM_GET = 0x01
# Alarm Sensor Report
SENSOR_ALARM_REPORT = 0x02
# Alarm Sensor Supported Get
SENSOR_ALARM_SUPPORTED_GET = 0x03
# Alarm Sensor Supported Report
SENSOR_ALARM_SUPPORTED_REPORT = 0x04


class ZW_SENSOR_ALARM_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('sensorType', uint8_t)]


class ZW_SENSOR_ALARM_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sourceNodeId', uint8_t),
        ('sensorType', uint8_t),
        ('sensorState', uint8_t),
        ('seconds1', uint8_t),
        ('seconds2', uint8_t),
    ]


class ZW_SENSOR_ALARM_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SENSOR_ALARM_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfBitMasks', uint8_t),
        ('bitMask1', uint8_t),
    ]

