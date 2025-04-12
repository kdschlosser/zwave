# Controller Replication Command Class
# Application
# ==============================
COMMAND_CLASS_CONTROLLER_REPLICATION = 0x21

CONTROLLER_REPLICATION_VERSION = 0x01
# Transfer Group
CTRL_REPLICATION_TRANSFER_GROUP = 0x31
# Transfer Group Name
CTRL_REPLICATION_TRANSFER_GROUP_NAME = 0x32
# Transfer Scene
CTRL_REPLICATION_TRANSFER_SCENE = 0x33
# Transfer Scene Name
CTRL_REPLICATION_TRANSFER_SCENE_NAME = 0x34





class ZW_CTRL_REPLICATION_TRANSFER_GROUP_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('groupId', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_CTRL_REPLICATION_TRANSFER_GROUP_NAME_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('groupId', uint8_t),
        ('groupName1', uint8_t),
    ]


class ZW_CTRL_REPLICATION_TRANSFER_SCENE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('sceneId', uint8_t),
        ('nodeId', uint8_t),
        ('level', uint8_t),
    ]


class ZW_CTRL_REPLICATION_TRANSFER_SCENE_NAME_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('sceneId', uint8_t),
        ('sceneName1', uint8_t),
    ]



