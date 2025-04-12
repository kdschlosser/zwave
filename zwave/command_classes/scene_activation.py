# Scene Activation Command Class
# Application
# ==============================
COMMAND_CLASS_SCENE_ACTIVATION = 0x2B

SCENE_ACTIVATION_VERSION = 0x01
# Scene Activation Set
SCENE_ACTIVATION_SET = 0x01

class ZW_SCENE_ACTIVATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sceneId', uint8_t),
        ('dimmingDuration', uint8_t),
    ]
