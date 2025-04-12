# Inclusion Controller Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_INCLUSION_CONTROLLER = 0x74

INCLUSION_CONTROLLER_VERSION = 0x01
# Inclusion Controller Initiate
INITIATE = 0x01
# Inclusion Controller Complete
COMPLETE = 0x02

# Values used for Initiate command
INITIATE_PROXY_INCLUSION = 0x01
INITIATE_S0_INCLUSION = 0x02
INITIATE_PROXY_INCLUSION_REPLACE = 0x03
# Values used for Complete command
COMPLETE_PROXY_INCLUSION = 0x01
COMPLETE_S0_INCLUSION = 0x02
COMPLETE_PROXY_INCLUSION_REPLACE = 0x03
COMPLETE_STEP_OK = 0x01
COMPLETE_STEP_USER_REJECTED = 0x02
COMPLETE_STEP_FAILED = 0x03
COMPLETE_STEP_NOT_SUPPORTED = 0x04

class ZW_INITIATE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('nodeId', uint8_t),
        ('stepId', uint8_t),
    ]


class ZW_COMPLETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('stepId', uint8_t),
        ('status', uint8_t),
    ]

