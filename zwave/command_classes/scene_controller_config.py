# Scene Controller Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_SCENE_CONTROLLER_CONF = 0x2D

SCENE_CONTROLLER_CONF_VERSION = 0x01
# Scene Controller Configuration Set
SCENE_CONTROLLER_CONF_SET = 0x01
# Scene Controller Configuration Get
SCENE_CONTROLLER_CONF_GET = 0x02
# Scene Controller Configuration Report
SCENE_CONTROLLER_CONF_REPORT = 0x03


class ZW_SCENE_CONTROLLER_CONF_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('groupId', uint8_t)]


class ZW_SCENE_CONTROLLER_CONF_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupId', uint8_t),
        ('sceneId', uint8_t),
        ('dimmingDuration', uint8_t),
    ]


class ZW_SCENE_CONTROLLER_CONF_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupId', uint8_t),
        ('sceneId', uint8_t),
        ('dimmingDuration', uint8_t),
    ]
