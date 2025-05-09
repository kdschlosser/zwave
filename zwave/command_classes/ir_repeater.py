# IR Repeater Command Class
# Application
# ==============================
COMMAND_CLASS_IR_REPEATER = 0xA0

IR_REPEATER_VERSION = 0x01
# IR Repeater Capabilities Get
IR_REPEATER_CAPABILITIES_GET = 0x01
# IR Repeater Capabilities Report
IR_REPEATER_CAPABILITIES_REPORT = 0x02
# IR Repeater IR Code Learning Start
IR_REPEATER_IR_CODE_LEARNING_START = 0x03
# IR Repeater IR Code Learning Stop
IR_REPEATER_IR_CODE_LEARNING_STOP = 0x04
# IR Repeater IR Code Learning Status
IR_REPEATER_IR_CODE_LEARNING_STATUS = 0x05
# IR Repeater Learnt IR Code Remove
IR_REPEATER_LEARNT_IR_CODE_REMOVE = 0x06
# IR Repeater Learnt IR Code Get
IR_REPEATER_LEARNT_IR_CODE_GET = 0x07
# IR Repeater Learnt IR Code Report
IR_REPEATER_LEARNT_IR_CODE_REPORT = 0x08
# IR Repeater Learnt IR Code Readback Get
IR_REPEATER_LEARNT_IR_CODE_READBACK_GET = 0x09
# IR Repeater Learnt IR Code Readback Report
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT = 0x0A
# IR Repeater Configuration Set
IR_REPEATER_CONFIGURATION_SET = 0x0B
# IR Repeater Configuration Get
IR_REPEATER_CONFIGURATION_GET = 0x0C
# IR Repeater Configuration Report
IR_REPEATER_CONFIGURATION_REPORT = 0x0D
# IR Repeater Repeat Learnt Code
IR_REPEATER_REPEAT_LEARNT_CODE = 0x0E
# IR Repeater Repeat
IR_REPEATER_REPEAT = 0x0F

# Values used for Ir Repeater Capabilities Report command
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_DUTY_CYCLE_BITMASK_MASK = 0x07
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_BES_BIT_MASK = 0x08
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_PES_BIT_MASK = 0x10
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_RLC_BIT_MASK = 0x20
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_LCR_BIT_MASK = 0x40
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES1_IRR_BIT_MASK = 0x80
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES2_MAXIMUM_PULSE_TIME_UNIT_MSB_MASK = 0x0F
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES2_MINIMUM_PULSE_TIME_UNIT_LSB_MASK = 0xF0
IR_REPEATER_CAPABILITIES_REPORT_PROPERTIES2_MINIMUM_PULSE_TIME_UNIT_LSB_SHIFT = 0x04
# Values used for Ir Repeater Ir Code Learning Start command
IR_REPEATER_IR_CODE_LEARNING_START_PROPERTIES1_PULSE_TIME_UNIT_MSB_MASK = 0x0F
IR_REPEATER_IR_CODE_LEARNING_START_PROPERTIES1_RESERVED1_MASK = 0xF0
IR_REPEATER_IR_CODE_LEARNING_START_PROPERTIES1_RESERVED1_SHIFT = 0x04
# Values used for Ir Repeater Ir Code Learning Status command
IR_REPEATER_IR_CODE_LEARNING_STATUS_LEARNING_BUFFER_OVERFLOW = 0x00
IR_REPEATER_IR_CODE_LEARNING_STATUS_FORCED_LEARNING_STOP = 0x01
IR_REPEATER_IR_CODE_LEARNING_STATUS_TIMEOUT = 0x02
IR_REPEATER_IR_CODE_LEARNING_STATUS_SUCCESS = 0xFF
# Values used for Ir Repeater Learnt Ir Code Report command
IR_REPEATER_LEARNT_IR_CODE_REPORT_PROPERTIES1_IR_CODE_IDENFIER_STATUS_LENGTH_MASK = 0x1F
IR_REPEATER_LEARNT_IR_CODE_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
IR_REPEATER_LEARNT_IR_CODE_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05
# Values used for Ir Repeater Learnt Ir Code Readback Get command
IR_REPEATER_LEARNT_IR_CODE_READBACK_GET_PROPERTIES1_REPORT_NUMBER_MSB_MASK = 0x7F
IR_REPEATER_LEARNT_IR_CODE_READBACK_GET_PROPERTIES1_RESERVED1_BIT_MASK = 0x80
# Values used for Ir Repeater Learnt Ir Code Readback Report command
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES1_PULSE_TIME_UNIT_MSB_MASK = 0x0F
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES1_DUTY_CYCLE_MASK = 0x30
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES1_DUTY_CYCLE_SHIFT = 0x04
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_DUTY_CYCLE_1_2_DUTY_CYCLE = 0x00
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_DUTY_CYCLE_1_3_DUTY_CYCLE = 0x01
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_DUTY_CYCLE_1_4_DUTY_CYCLE = 0x02
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_DUTY_CYCLE_RESERVED = 0x03
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES1_RESERVED1_MASK = 0xC0
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x06
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES2_REPORT_NUMBER_MSB_MASK = 0x7F
IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_PROPERTIES2_LAST_BIT_MASK = 0x80
# Values used for Ir Repeater Configuration Set command
IR_REPEATER_CONFIGURATION_SET_PROPERTIES1_PERIOD_LSB_MASK = 0x0F
IR_REPEATER_CONFIGURATION_SET_PROPERTIES1_RESERVED1_MASK = 0xF0
IR_REPEATER_CONFIGURATION_SET_PROPERTIES1_RESERVED1_SHIFT = 0x04
# Values used for Ir Repeater Configuration Report command
IR_REPEATER_CONFIGURATION_REPORT_PROPERTIES1_PERIOD_LSB_MASK = 0x0F
IR_REPEATER_CONFIGURATION_REPORT_PROPERTIES1_RESERVED1_MASK = 0xF0
IR_REPEATER_CONFIGURATION_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x04
# Values used for Ir Repeater Repeat command
IR_REPEATER_REPEAT_PROPERTIES1_PULSE_TIME_UNIT_MSB_MASK = 0x0F
IR_REPEATER_REPEAT_PROPERTIES1_DUTY_CYCLE_MASK = 0x30
IR_REPEATER_REPEAT_PROPERTIES1_DUTY_CYCLE_SHIFT = 0x04
IR_REPEATER_REPEAT_DUTY_CYCLE_1_2_DUTY_CYCLE = 0x00
IR_REPEATER_REPEAT_DUTY_CYCLE_1_3_DUTY_CYCLE = 0x01
IR_REPEATER_REPEAT_DUTY_CYCLE_1_4_DUTY_CYCLE = 0x02
IR_REPEATER_REPEAT_DUTY_CYCLE_RESERVED = 0x03
IR_REPEATER_REPEAT_PROPERTIES1_RESERVED1_MASK = 0xC0
IR_REPEATER_REPEAT_PROPERTIES1_RESERVED1_SHIFT = 0x06
IR_REPEATER_REPEAT_PROPERTIES2_REPORT_NUMBER_MSB_MASK = 0x7F
IR_REPEATER_REPEAT_PROPERTIES2_LAST_BIT_MASK = 0x80

class ZW_IR_REPEATER_CAPABILITIES_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IR_REPEATER_CAPABILITIES_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfIrCodeIdentifiersForLearning', uint8_t),
        ('properties1', uint8_t),
        ('carrier', uint8_t),
        ('minimumSubCarrier', uint8_t),
        ('maxiumSubCarrier', uint8_t),
        ('minimumPulseTimeUnitMsb', uint8_t),
        ('properties2', uint8_t),
        ('maximumPulseTimeUnitLsb', uint8_t),
    ]


class ZW_IR_REPEATER_IR_CODE_LEARNING_START_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('irCodeIdentifier', uint8_t),
        ('timeout', uint8_t),
        ('properties1', uint8_t),
        ('pulseTimeUnitLsb', uint8_t),
    ]


class ZW_IR_REPEATER_IR_CODE_LEARNING_STOP_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IR_REPEATER_IR_CODE_LEARNING_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('irCodeIdentifier', uint8_t),
        ('status', uint8_t),
    ]


class ZW_IR_REPEATER_LEARNT_IR_CODE_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('irCodeIdentifier', uint8_t)]


class ZW_IR_REPEATER_LEARNT_IR_CODE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IR_REPEATER_LEARNT_IR_CODE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('irCodeIdentifierStatusBitmask1', uint8_t),
    ]


class ZW_IR_REPEATER_LEARNT_IR_CODE_READBACK_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('irCodeIdentifier', uint8_t),
        ('properties1', uint8_t),
        ('reportNumberLsb', uint8_t),
    ]


class VG_IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties3', uint8_t),
        ('dataBlockValue1', uint8_t),
    ]


class ZW_IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('irCodeIdentifier', uint8_t),
        ('subCarrier', uint8_t),
        ('properties1', uint8_t),
        ('pulseTimeUnitLsb', uint8_t),
        ('properties2', uint8_t),
        ('reportNumberLsb', uint8_t),
        ('variantgroup1', VG_IR_REPEATER_LEARNT_IR_CODE_READBACK_REPORT_VG),
    ]


class VG_IR_REPEATER_CONFIGURATION_SET_VG(ctypes.Structure):
    _fields_ = [
        ('dataBitEncodingLength1', uint8_t),
        ('dataBitEncodingLength2', uint8_t),
        ('dataBitEncoding1', uint8_t),
    ]


class ZW_IR_REPEATER_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('periodMsb', uint8_t),
        ('properties1', uint8_t),
        ('variantgroup1', VG_IR_REPEATER_CONFIGURATION_SET_VG),
    ]


class ZW_IR_REPEATER_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class VG_IR_REPEATER_CONFIGURATION_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('dataBitEncodingLength1', uint8_t),
        ('dataBitEncodingLength2', uint8_t),
        ('dataBitEncoding1', uint8_t),
    ]


class ZW_IR_REPEATER_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('periodMsb', uint8_t),
        ('properties1', uint8_t),
        ('variantgroup1', VG_IR_REPEATER_CONFIGURATION_REPORT_VG),
    ]


class ZW_IR_REPEATER_REPEAT_LEARNT_CODE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('irCodeIdentifier', uint8_t)]


class VG_IR_REPEATER_REPEAT_VG(ctypes.Structure):
    _fields_ = [
        ('properties3', uint8_t),
        ('dataBlockValue1', uint8_t),
    ]


class ZW_IR_REPEATER_REPEAT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('subCarrier', uint8_t),
        ('properties1', uint8_t),
        ('pulseTimeUnitLsb', uint8_t),
        ('properties2', uint8_t),
        ('reportNumberLsb', uint8_t),
        ('variantgroup1', VG_IR_REPEATER_REPEAT_VG),
    ]
