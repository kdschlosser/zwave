
COMMAND_CLASS_SECURITY_PANEL_ZONE_SENSOR = 0x2F

SECURITY_PANEL_ZONE_SENSOR_VERSION = 0x01
COMMAND_CLASS_SECURITY_PANEL_ZONE_SENSOR_INSTALLED_REPORT = 0x02
SECURITY_PANEL_ZONE_SENSOR_TYPE_GET = 0x03
SECURITY_PANEL_ZONE_SENSOR_TYPE_REPORT = 0x04
SECURITY_PANEL_ZONE_SENSOR_INSTALLED_GET = 0x01
SECURITY_PANEL_ZONE_SENSOR_STATE_GET = 0x05
SECURITY_PANEL_ZONE_SENSOR_STATE_REPORT = 0x06

class ZW_SECURITY_PANEL_ZONE_SENSOR_INSTALLED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zoneNumber', uint8_t),
        ('numberOfSensors', uint8_t),
    ]


class ZW_SECURITY_PANEL_ZONE_SENSOR_TYPE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zoneNumber', uint8_t),
        ('sensorNumber', uint8_t),
    ]


class ZW_SECURITY_PANEL_ZONE_SENSOR_TYPE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zoneNumber', uint8_t),
        ('sensorNumber', uint8_t),
        ('zwaveAlarmType', uint8_t),
    ]


class ZW_SECURITY_PANEL_ZONE_SENSOR_INSTALLED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('zoneNumber', uint8_t)]


class ZW_SECURITY_PANEL_ZONE_SENSOR_STATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zoneNumber', uint8_t),
        ('sensorNumber', uint8_t),
    ]


class ZW_SECURITY_PANEL_ZONE_SENSOR_STATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zoneNumber', uint8_t),
        ('sensorNumber', uint8_t),
        ('zwaveAlarmType', uint8_t),
        ('zwaveAlarmEvent', uint8_t),
        ('eventParameters', uint8_t),
    ]
