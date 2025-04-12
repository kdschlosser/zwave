from . import CommandClass, CommandClassCommands


# Barrier Operator Command Class
# Application
# ==============================

class BARRIER_OPERATOR_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    VERSION = 0x01
    SET = 0x01
    GET = 0x02
    REPORT = 0x03
    SIGNAL_SUPPORTED_GET = 0x04
    SIGNAL_SUPPORTED_REPORT = 0x05
    EVENT_SIGNALING_SET = 0x06
    EVENT_SIGNALING_GET = 0x07
    EVENT_SIGNALING_REPORT = 0x08

    SET_VALUES = {
        0x00: 'Close',
        0xFF: 'Open'
    }

    REPORT_VALUES = {
        0x00: 'Closed',
        0xFC: 'Closing',
        0xFD: 'Stopped',
        0xFE: 'Opening',
        0xFF: 'Open'
    }
    EVENT_SIGNALING_SET_VALUES = {
        0x00: 'Off',
        0xFF: 'On'
    }

    EVENT_SIGNALING_REPORT_VALUES = EVENT_SIGNALING_SET_VALUES


class COMMAND_CLASS_BARRIER_OPERATOR(CommandClass):
    id = 0x66
    versions = [
        BARRIER_OPERATOR_V1_COMMANDS
    ]


class ZW_BARRIER_OPERATOR_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('targetValue', uint8_t)]


class ZW_BARRIER_OPERATOR_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_BARRIER_OPERATOR_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('state', uint8_t)]


class ZW_BARRIER_OPERATOR_SIGNAL_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_BARRIER_OPERATOR_SIGNAL_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('bitMask1', uint8_t)]


class ZW_BARRIER_OPERATOR_EVENT_SIGNAL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('subsystemType', uint8_t),
        ('subsystemState', uint8_t),
    ]


class ZW_BARRIER_OPERATOR_EVENT_SIGNALING_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('subsystemType', uint8_t)]


class ZW_BARRIER_OPERATOR_EVENT_SIGNALING_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('subsystemType', uint8_t),
        ('subsystemState', uint8_t),
    ]
