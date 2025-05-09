# Window Covering Command Class
# Application
# ==============================
COMMAND_CLASS_WINDOW_COVERING = 0x6A

WINDOW_COVERING_VERSION = 0x01
# Window Covering Supported Get
WINDOW_COVERING_SUPPORTED_GET = 0x01
# Window Covering Supported Report
WINDOW_COVERING_SUPPORTED_REPORT = 0x02
# Window Covering Get
WINDOW_COVERING_GET = 0x03
# Window Covering Report
WINDOW_COVERING_REPORT = 0x04
# Window Covering Set
WINDOW_COVERING_SET = 0x05
# Window Covering Start Level Change
WINDOW_COVERING_START_LEVEL_CHANGE = 0x06
# Window Covering Stop Level Change
WINDOW_COVERING_STOP_LEVEL_CHANGE = 0x07

# Values used for Window Covering Supported Report command
WINDOW_COVERING_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_PARAMETER_MASK_BYTES_MASK = 0x0F
WINDOW_COVERING_SUPPORTED_REPORT_PROPERTIES1_RESERVED_MASK = 0xF0
WINDOW_COVERING_SUPPORTED_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x04
# Values used for Window Covering Get command
WINDOW_COVERING_GET_OUT_LEFT_1 = 0x00
WINDOW_COVERING_GET_OUT_LEFT_2 = 0x01
WINDOW_COVERING_GET_OUT_RIGHT_1 = 0x02
WINDOW_COVERING_GET_OUT_RIGHT_2 = 0x03
WINDOW_COVERING_GET_IN_LEFT_1 = 0x04
WINDOW_COVERING_GET_IN_LEFT_2 = 0x05
WINDOW_COVERING_GET_IN_RIGHT_1 = 0x06
WINDOW_COVERING_GET_IN_RIGHT_2 = 0x07
WINDOW_COVERING_GET_IN_RIGHT_LEFT_1 = 0x08
WINDOW_COVERING_GET_IN_RIGHT_LEFT_2 = 0x09
WINDOW_COVERING_GET_VERTICAL_SLATS_ANGLE_1 = 0x0A
WINDOW_COVERING_GET_VERTICAL_SLATS_ANGLE_2 = 0x0B
WINDOW_COVERING_GET_OUT_BOTTOM_1 = 0x0C
WINDOW_COVERING_GET_OUT_BOTTOM_2 = 0x0D
WINDOW_COVERING_GET_OUT_TOP_1 = 0x0E
WINDOW_COVERING_GET_OUT_TOP_2 = 0x0F
WINDOW_COVERING_GET_IN_BOTTOM_1 = 0x10
WINDOW_COVERING_GET_IN_BOTTOM_2 = 0x11
WINDOW_COVERING_GET_IN_TOP_1 = 0x12
WINDOW_COVERING_GET_IN_TOP_2 = 0x13
WINDOW_COVERING_GET_IN_TOP_BOTTOM_1 = 0x14
WINDOW_COVERING_GET_IN_TOP_BOTTOM_2 = 0x15
WINDOW_COVERING_GET_HORIZONTAL_SLATS_ANGLE_1 = 0x16
WINDOW_COVERING_GET_HORIZONTAL_SLATS_ANGLE_2 = 0x17
# Values used for Window Covering Report command
WINDOW_COVERING_REPORT_OUT_LEFT_1 = 0x00
WINDOW_COVERING_REPORT_OUT_LEFT_2 = 0x01
WINDOW_COVERING_REPORT_OUT_RIGHT_1 = 0x02
WINDOW_COVERING_REPORT_OUT_RIGHT_2 = 0x03
WINDOW_COVERING_REPORT_IN_LEFT_1 = 0x04
WINDOW_COVERING_REPORT_IN_LEFT_2 = 0x05
WINDOW_COVERING_REPORT_IN_RIGHT_1 = 0x06
WINDOW_COVERING_REPORT_IN_RIGHT_2 = 0x07
WINDOW_COVERING_REPORT_IN_RIGHT_LEFT_1 = 0x08
WINDOW_COVERING_REPORT_IN_RIGHT_LEFT_2 = 0x09
WINDOW_COVERING_REPORT_VERTICAL_SLATS_ANGLE_1 = 0x0A
WINDOW_COVERING_REPORT_VERTICAL_SLATS_ANGLE_2 = 0x0B
WINDOW_COVERING_REPORT_OUT_BOTTOM_1 = 0x0C
WINDOW_COVERING_REPORT_OUT_BOTTOM_2 = 0x0D
WINDOW_COVERING_REPORT_OUT_TOP_1 = 0x0E
WINDOW_COVERING_REPORT_OUT_TOP_2 = 0x0F
WINDOW_COVERING_REPORT_IN_BOTTOM_1 = 0x10
WINDOW_COVERING_REPORT_IN_BOTTOM_2 = 0x11
WINDOW_COVERING_REPORT_IN_TOP_1 = 0x12
WINDOW_COVERING_REPORT_IN_TOP_2 = 0x13
WINDOW_COVERING_REPORT_IN_TOP_BOTTOM_1 = 0x14
WINDOW_COVERING_REPORT_IN_TOP_BOTTOM_2 = 0x15
WINDOW_COVERING_REPORT_HORIZONTAL_SLATS_ANGLE_1 = 0x16
WINDOW_COVERING_REPORT_HORIZONTAL_SLATS_ANGLE_2 = 0x17
# Values used for Window Covering Set command
WINDOW_COVERING_SET_PROPERTIES1_PARAMETER_COUNT_MASK = 0x1F
WINDOW_COVERING_SET_PROPERTIES1_RESERVED_MASK = 0xE0
WINDOW_COVERING_SET_PROPERTIES1_RESERVED_SHIFT = 0x05
WINDOW_COVERING_SET_OUT_LEFT_1 = 0x00
WINDOW_COVERING_SET_OUT_LEFT_2 = 0x01
WINDOW_COVERING_SET_OUT_RIGHT_1 = 0x02
WINDOW_COVERING_SET_OUT_RIGHT_2 = 0x03
WINDOW_COVERING_SET_IN_LEFT_1 = 0x04
WINDOW_COVERING_SET_IN_LEFT_2 = 0x05
WINDOW_COVERING_SET_IN_RIGHT_1 = 0x06
WINDOW_COVERING_SET_IN_RIGHT_2 = 0x07
WINDOW_COVERING_SET_IN_RIGHT_LEFT_1 = 0x08
WINDOW_COVERING_SET_IN_RIGHT_LEFT_2 = 0x09
WINDOW_COVERING_SET_VERTICAL_SLATS_ANGLE_1 = 0x0A
WINDOW_COVERING_SET_VERTICAL_SLATS_ANGLE_2 = 0x0B
WINDOW_COVERING_SET_OUT_BOTTOM_1 = 0x0C
WINDOW_COVERING_SET_OUT_BOTTOM_2 = 0x0D
WINDOW_COVERING_SET_OUT_TOP_1 = 0x0E
WINDOW_COVERING_SET_OUT_TOP_2 = 0x0F
WINDOW_COVERING_SET_IN_BOTTOM_1 = 0x10
WINDOW_COVERING_SET_IN_BOTTOM_2 = 0x11
WINDOW_COVERING_SET_IN_TOP_1 = 0x12
WINDOW_COVERING_SET_IN_TOP_2 = 0x13
WINDOW_COVERING_SET_IN_TOP_BOTTOM_1 = 0x14
WINDOW_COVERING_SET_IN_TOP_BOTTOM_2 = 0x15
WINDOW_COVERING_SET_HORIZONTAL_SLATS_ANGLE_1 = 0x16
WINDOW_COVERING_SET_HORIZONTAL_SLATS_ANGLE_2 = 0x17
# Values used for Window Covering Start Level Change command
WINDOW_COVERING_START_LEVEL_CHANGE_PROPERTIES1_RES1_MASK = 0x3F
WINDOW_COVERING_START_LEVEL_CHANGE_PROPERTIES1_UP_DOWN_BIT_MASK = 0x40
WINDOW_COVERING_START_LEVEL_CHANGE_PROPERTIES1_RES2_BIT_MASK = 0x80
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_LEFT_1 = 0x00
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_LEFT_2 = 0x01
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_RIGHT_1 = 0x02
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_RIGHT_2 = 0x03
WINDOW_COVERING_START_LEVEL_CHANGE_IN_LEFT_1 = 0x04
WINDOW_COVERING_START_LEVEL_CHANGE_IN_LEFT_2 = 0x05
WINDOW_COVERING_START_LEVEL_CHANGE_IN_RIGHT_1 = 0x06
WINDOW_COVERING_START_LEVEL_CHANGE_IN_RIGHT_2 = 0x07
WINDOW_COVERING_START_LEVEL_CHANGE_IN_RIGHT_LEFT_1 = 0x08
WINDOW_COVERING_START_LEVEL_CHANGE_IN_RIGHT_LEFT_2 = 0x09
WINDOW_COVERING_START_LEVEL_CHANGE_VERTICAL_SLATS_ANGLE_1 = 0x0A
WINDOW_COVERING_START_LEVEL_CHANGE_VERTICAL_SLATS_ANGLE_2 = 0x0B
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_BOTTOM_1 = 0x0C
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_BOTTOM_2 = 0x0D
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_TOP_1 = 0x0E
WINDOW_COVERING_START_LEVEL_CHANGE_OUT_TOP_2 = 0x0F
WINDOW_COVERING_START_LEVEL_CHANGE_IN_BOTTOM_1 = 0x10
WINDOW_COVERING_START_LEVEL_CHANGE_IN_BOTTOM_2 = 0x11
WINDOW_COVERING_START_LEVEL_CHANGE_IN_TOP_1 = 0x12
WINDOW_COVERING_START_LEVEL_CHANGE_IN_TOP_2 = 0x13
WINDOW_COVERING_START_LEVEL_CHANGE_IN_TOP_BOTTOM_1 = 0x14
WINDOW_COVERING_START_LEVEL_CHANGE_IN_TOP_BOTTOM_2 = 0x15
WINDOW_COVERING_START_LEVEL_CHANGE_HORIZONTAL_SLATS_ANGLE_1 = 0x16
WINDOW_COVERING_START_LEVEL_CHANGE_HORIZONTAL_SLATS_ANGLE_2 = 0x17
# Values used for Window Covering Stop Level Change command
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_LEFT_1 = 0x00
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_LEFT_2 = 0x01
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_RIGHT_1 = 0x02
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_RIGHT_2 = 0x03
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_LEFT_1 = 0x04
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_LEFT_2 = 0x05
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_RIGHT_1 = 0x06
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_RIGHT_2 = 0x07
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_RIGHT_LEFT_1 = 0x08
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_RIGHT_LEFT_2 = 0x09
WINDOW_COVERING_STOP_LEVEL_CHANGE_VERTICAL_SLATS_ANGLE_1 = 0x0A
WINDOW_COVERING_STOP_LEVEL_CHANGE_VERTICAL_SLATS_ANGLE_2 = 0x0B
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_BOTTOM_1 = 0x0C
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_BOTTOM_2 = 0x0D
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_TOP_1 = 0x0E
WINDOW_COVERING_STOP_LEVEL_CHANGE_OUT_TOP_2 = 0x0F
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_BOTTOM_1 = 0x10
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_BOTTOM_2 = 0x11
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_TOP_1 = 0x12
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_TOP_2 = 0x13
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_TOP_BOTTOM_1 = 0x14
WINDOW_COVERING_STOP_LEVEL_CHANGE_IN_TOP_BOTTOM_2 = 0x15
WINDOW_COVERING_STOP_LEVEL_CHANGE_HORIZONTAL_SLATS_ANGLE_1 = 0x16
WINDOW_COVERING_STOP_LEVEL_CHANGE_HORIZONTAL_SLATS_ANGLE_2 = 0x17

class ZW_WINDOW_COVERING_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_WINDOW_COVERING_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('parameterMask1', uint8_t),
    ]


class ZW_WINDOW_COVERING_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('parameterId', uint8_t)]


class ZW_WINDOW_COVERING_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('parameterId', uint8_t),
        ('currentValue', uint8_t),
        ('targetValue', uint8_t),
        ('duration', uint8_t),
    ]


class VG_WINDOW_COVERING_SET_VG(ctypes.Structure):
    _fields_ = [
        ('parameterId', uint8_t),
        ('value', uint8_t),
    ]


class ZW_WINDOW_COVERING_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('variantgroup1', VG_WINDOW_COVERING_SET_VG),
        ('duration', uint8_t),
    ]


class ZW_WINDOW_COVERING_START_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('parameterId', uint8_t),
        ('duration', uint8_t),
    ]


class ZW_WINDOW_COVERING_STOP_LEVEL_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('parameterId', uint8_t)]

