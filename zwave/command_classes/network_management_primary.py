# Network Management Primary Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY = 0x54

NETWORK_MANAGEMENT_PRIMARY_VERSION = 0x01
# Controller Change
COMMAND_CONTROLLER_CHANGE = 0x01
# Controller Change Status
COMMAND_CONTROLLER_CHANGE_STATUS = 0x02

# Values used for Controller Change Status command
CONTROLLER_CHANGE_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK = 0x7F
CONTROLLER_CHANGE_STATUS_PROPERTIES1_LISTENING_BIT_MASK = 0x80
CONTROLLER_CHANGE_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK = 0x7F
CONTROLLER_CHANGE_STATUS_PROPERTIES2_OPT_BIT_MASK = 0x80

class ZW_CONTROLLER_CHANGE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('reserved', uint8_t),
        ('mode', uint8_t),
        ('txOptions', uint8_t),
    ]


class ZW_CONTROLLER_CHANGE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('reserved', uint8_t),
        ('newNodeId', uint8_t),
        ('nodeInfoLength', uint8_t),
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('basicDeviceClass', uint8_t),
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
        ('commandClass1', uint8_t),
    ]
