# Alarm Silence Command Class
# Application
# ==============================
COMMAND_CLASS_SILENCE_ALARM = 0x9D

SILENCE_ALARM_VERSION = 0x01
# Alarm Silence Set
SENSOR_ALARM_SET = 0x01


class ZW_SENSOR_ALARM_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('mode', uint8_t),
        ('seconds1', uint8_t),
        ('seconds2', uint8_t),
        ('numberOfBitMasks', uint8_t),
        ('bitMask1', uint8_t),
    ]

