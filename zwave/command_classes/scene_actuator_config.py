# Scene Actuator Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_SCENE_ACTUATOR_CONF = 0x2C

SCENE_ACTUATOR_CONF_VERSION = 0x01
# Scene Actuator Configuration Set
SCENE_ACTUATOR_CONF_SET = 0x01
# Scene Actuator Configuration Get
SCENE_ACTUATOR_CONF_GET = 0x02
# Scene Actuator Configuration Report
SCENE_ACTUATOR_CONF_REPORT = 0x03

# Values used for Scene Actuator Conf Set command
SCENE_ACTUATOR_CONF_SET_LEVEL2_RESERVED_MASK = 0x7F
SCENE_ACTUATOR_CONF_SET_LEVEL2_OVERRIDE_BIT_MASK = 0x80


class ZW_SCENE_ACTUATOR_CONF_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('sceneId', uint8_t)]


class ZW_SCENE_ACTUATOR_CONF_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sceneId', uint8_t),
        ('level', uint8_t),
        ('dimmingDuration', uint8_t),
    ]


class ZW_SCENE_ACTUATOR_CONF_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sceneId', uint8_t),
        ('dimmingDuration', uint8_t),
        ('level2', uint8_t),
        ('level', uint8_t),
    ]
