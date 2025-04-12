# Remote Association Activation Command Class
# Management
# ==============================
COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE = 0x7C

REMOTE_ASSOCIATION_ACTIVATE_VERSION = 0x01
# Remote Association Activate
REMOTE_ASSOCIATION_ACTIVATE = 0x01


class ZW_REMOTE_ASSOCIATION_ACTIVATE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('groupingIdentifier', uint8_t)]

