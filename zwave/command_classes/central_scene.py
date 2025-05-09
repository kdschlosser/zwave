# Central Scene Command Class
# Application
# ==============================
COMMAND_CLASS_CENTRAL_SCENE = 0x5B

CENTRAL_SCENE_VERSION = 0x01
# Central Scene Supported Get
CENTRAL_SCENE_SUPPORTED_GET = 0x01
# Central Scene Supported Report
CENTRAL_SCENE_SUPPORTED_REPORT = 0x02
# Central Scene Notification
CENTRAL_SCENE_NOTIFICATION = 0x03


# Values used for Central Scene Notification command
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_KEY_ATTRIBUTES_MASK = 0x07
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_MASK = 0xF8
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_SHIFT = 0x03

CENTRAL_SCENE_VERSION_V2 = 0x02
CENTRAL_SCENE_SUPPORTED_GET_V2 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_V2 = 0x02
CENTRAL_SCENE_NOTIFICATION_V2 = 0x03
# Values used for Central Scene Supported Report command
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_IDENTICAL_BIT_MASK_V2 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_BIT_MASK_BYTES_MASK_V2 = 0x06
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_BIT_MASK_BYTES_SHIFT_V2 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xF8
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x03
# Values used for Central Scene Notification command
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_KEY_ATTRIBUTES_MASK_V2 = 0x07
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_1_TIME_V2 = 0x00
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_RELEASED_V2 = 0x01
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_HELD_DOWN_V2 = 0x02
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_2_TIMES_V2 = 0x03
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_3_TIMES_V2 = 0x04
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_4_TIMES_V2 = 0x05
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_5_TIMES_V2 = 0x06
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_MASK_V2 = 0xF8
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_SHIFT_V2 = 0x03

CENTRAL_SCENE_VERSION_V3 = 0x03
CENTRAL_SCENE_SUPPORTED_GET_V3 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_V3 = 0x02
CENTRAL_SCENE_NOTIFICATION_V3 = 0x03
# Central Scene Configuration Set
CENTRAL_SCENE_CONFIGURATION_SET_V3 = 0x04
# Central Scene Configuration Get
CENTRAL_SCENE_CONFIGURATION_GET_V3 = 0x05
# Central Scene Configuration Report
CENTRAL_SCENE_CONFIGURATION_REPORT_V3 = 0x06

# Values used for Central Scene Supported Report command
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_IDENTICAL_BIT_MASK_V3 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_BIT_MASK_BYTES_MASK_V3 = 0x06
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_NUMBER_OF_BIT_MASK_BYTES_SHIFT_V3 = 0x01
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0x78
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x03
CENTRAL_SCENE_SUPPORTED_REPORT_PROPERTIES1_SLOW_REFRESH_SUPPORT_BIT_MASK_V3 = 0x80
# Values used for Central Scene Notification command
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_KEY_ATTRIBUTES_MASK_V3 = 0x07
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_1_TIME_V3 = 0x00
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_RELEASED_V3 = 0x01
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_HELD_DOWN_V3 = 0x02
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_2_TIMES_V3 = 0x03
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_3_TIMES_V3 = 0x04
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_4_TIMES_V3 = 0x05
CENTRAL_SCENE_NOTIFICATION_KEY_ATTRIBUTES_KEY_PRESSED_5_TIMES_V3 = 0x06
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_MASK_V3 = 0x78
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_RESERVED_SHIFT_V3 = 0x03
CENTRAL_SCENE_NOTIFICATION_PROPERTIES1_SLOW_REFRESH_BIT_MASK_V3 = 0x80
# Values used for Central Scene Configuration Set command
CENTRAL_SCENE_CONFIGURATION_SET_PROPERTIES1_RESERVED_MASK_V3 = 0x7F
CENTRAL_SCENE_CONFIGURATION_SET_PROPERTIES1_SLOW_REFRESH_BIT_MASK_V3 = 0x80
# Values used for Central Scene Configuration Report command
CENTRAL_SCENE_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0x7F
CENTRAL_SCENE_CONFIGURATION_REPORT_PROPERTIES1_SLOW_REFRESH_BIT_MASK_V3 = 0x80

class ZW_CENTRAL_SCENE_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedScenes', uint8_t)]


class ZW_CENTRAL_SCENE_NOTIFICATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('properties1', uint8_t),
        ('sceneNumber', uint8_t),
    ]


class ZW_CENTRAL_SCENE_SUPPORTED_GET_V2_FRAME(ZW_CENTRAL_SCENE_SUPPORTED_GET_FRAME):
    _fields_ = []


class VG_CENTRAL_SCENE_SUPPORTED_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [('supportedKeyAttributesForScene1', uint8_t)]


class ZW_CENTRAL_SCENE_SUPPORTED_REPORT_V2_FRAME(ZW_CENTRAL_SCENE_SUPPORTED_REPORT_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('variantgroup1', VG_CENTRAL_SCENE_SUPPORTED_REPORT_V2_VG),
    ]


class ZW_CENTRAL_SCENE_NOTIFICATION_V2_FRAME(ZW_CENTRAL_SCENE_NOTIFICATION_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_SUPPORTED_GET_V3_FRAME(ZW_CENTRAL_SCENE_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_SUPPORTED_REPORT_V3_FRAME(ZW_CENTRAL_SCENE_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_NOTIFICATION_V3_FRAME(ZW_CENTRAL_SCENE_NOTIFICATION_V2_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_CONFIGURATION_SET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_CENTRAL_SCENE_CONFIGURATION_GET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_CENTRAL_SCENE_CONFIGURATION_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]

