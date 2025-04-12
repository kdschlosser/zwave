# Pulse Meter Command Class
# Application
# ==============================
COMMAND_CLASS_METER_PULSE = 0x35

METER_PULSE_VERSION = 0x01
# Pulse Meter Get
METER_PULSE_GET = 0x04
# Pulse Meter Report
METER_PULSE_REPORT = 0x05



class ZW_METER_PULSE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_PULSE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('pulseCount1', uint8_t),
        ('pulseCount2', uint8_t),
        ('pulseCount3', uint8_t),
        ('pulseCount4', uint8_t),
    ]

