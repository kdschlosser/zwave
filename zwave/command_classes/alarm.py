from . import CommandClass, CommandClassCommands


# Alarm Command Class
# Application
# ==============================


class ALARM_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    GET = 0x04
    # byte 0: alarm type

    REPORT = 0x05
    # byte 0: alarm type
    # byte 1: alarm level

    GET_VALUES = []
    REPORT_VALUES = []


class ALARM_V2_COMMANDS(ALARM_V1_COMMANDS):
    version = 0x02

    SET = 0x06
    # byte 0: zwave alarm type
    # byte 1: zwave alarm status

    SUPPORTED_GET = 0x07
    # no parameters

    SUPPORTED_REPORT = 0x08
    # byte 0: Properties 1
    # byte 1: zwave alarm type

    GET = 0x04
    # byte 0: alarm type
    # byte 1: zwave alarm type

    GET_BYTE1_VALUES = {
        0x00: 'Reserved',
        0x01: 'Smoke',
        0x02: 'CO',
        0x03: 'CO2',
        0x04: 'Heat',
        0x05: 'Water',
        0x06: 'Access Control',
        0x07: 'Burglar',
        0x08: 'Power Management',
        0x09: 'System',
        0x0A: 'Emergency',
        0x0B: 'Clock',
        0xFF: 'First'
    }

    REPORT = 0x05
    # byte 0: alarm type
    # byte 1: alarm level
    # byte 2: zensor net source node id
    # byte 3: zwave alarm status
    # byte 4: zwave alarm type
    # byte 5: zwave alarm event
    # byte 6: number of events
    # byte 7+: event parameter (number of parameters is dictated by byte 6)

    REPORT_BYTE3_VALUES = {
        0x00: 'Off',
        0xFF: 'On'
    }

    REPORT_BYTE4_VALUES = GET_BYTE1_VALUES
    SUPPORTED_REPORT_BYTE2_VALUES = GET_BYTE1_VALUES
    SET_BYTE0_VALUES = GET_BYTE1_VALUES
    SET_BYTE1_VALUES = REPORT_BYTE3_VALUES


from .notification import COMMAND_CLASS_NOTIFICATION  # NOQA


class COMMAND_CLASS_ALARM(CommandClass):
    """
    Command Class Alarm

    [DEPRECATED]
    """

    id = 0x71

    ALTERNATE_CC = COMMAND_CLASS_NOTIFICATION

    versions = [
        ALARM_V1_COMMANDS,
        ALARM_V2_COMMANDS
    ]

    def __init__(self, device, node_id):
        super().__init__(device, node_id)

        self._send(ALARM_V2_COMMANDS.SUPPORTED_GET)


# Values used for Alarm Type Supported Report command
ALARM_TYPE_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_BIT_MASKS_MASK_V2 = 0x1F
ALARM_TYPE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0x60
ALARM_TYPE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x05
ALARM_TYPE_SUPPORTED_REPORT_PROPERTIES1_V1_ALARM_BIT_MASK_V2 = 0x80


from . import ZW_COMMON_FRAME
import ctypes


uint8_t = ctypes.c_uint8


class ZW_ALARM_GET_V1_FRAME(ZW_COMMON_FRAME):
    _CC = 0x71
    _CMD = 0x04

    _fields_ = [('alarm_type', uint8_t)]

    @property
    def alarm_type(self):
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, value):
        self._alarm_type = value

    def __init__(self, alarm_type):
        self.alarmType = alarm_type



class ZW_ALARM_GET_V2_FRAME(ZW_ALARM_GET_V1_FRAME):
    _fields_ = [('zwaveAlarmType', uint8_t)]


class ZW_ALARM_REPORT_V1_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('alarmType', uint8_t),
        ('alarmLevel', uint8_t),
    ]


class ZW_ALARM_REPORT_V2_FRAME(ZW_ALARM_REPORT_V1_FRAME):
    _fields_ = [
        ('zensorNetSourceNodeId', uint8_t),
        ('zwaveAlarmStatus', uint8_t),
        ('zwaveAlarmType', uint8_t),
        ('zwaveAlarmEvent', uint8_t),
        ('numberOfEventParameters', uint8_t),
        ('eventParameter1', uint8_t),
    ]


class ZW_ALARM_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zwaveAlarmType', uint8_t),
        ('zwaveAlarmStatus', uint8_t),
    ]


class ZW_ALARM_TYPE_SUPPORTED_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ALARM_TYPE_SUPPORTED_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('bitMask1', uint8_t),
    ]


