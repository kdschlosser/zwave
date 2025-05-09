# Multi Channel Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_MULTI_CHANNEL = 0x60
# Multi Channel End Point Get
MULTI_CHANNEL_END_POINT_GET = 0x07
# Multi Channel End Point Report
MULTI_CHANNEL_END_POINT_REPORT = 0x08
# Multi Channel Capability Get
MULTI_CHANNEL_CAPABILITY_GET = 0x09
# Multi Channel Capability Report
MULTI_CHANNEL_CAPABILITY_REPORT = 0x0A
# Multi Channel End Point Find
MULTI_CHANNEL_END_POINT_FIND = 0x0B
# Multi Channel End Point Find Report
MULTI_CHANNEL_END_POINT_FIND_REPORT = 0x0C
# Multi Channel Command Encapsulation
MULTI_CHANNEL_CMD_ENCAP = 0x0D
# Multi Channel Aggregated Members Get
MULTI_CHANNEL_AGGREGATED_MEMBERS_GET = 0x0E
# Multi Channel Aggregated Members Report
MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT = 0x0F

MULTI_CHANNEL_VERSION_V2 = 0x02
MULTI_CHANNEL_CAPABILITY_GET_V2 = 0x09
MULTI_CHANNEL_CAPABILITY_REPORT_V2 = 0x0A
MULTI_CHANNEL_CMD_ENCAP_V2 = 0x0D
MULTI_CHANNEL_END_POINT_FIND_V2 = 0x0B
MULTI_CHANNEL_END_POINT_FIND_REPORT_V2 = 0x0C
MULTI_CHANNEL_END_POINT_GET_V2 = 0x07
MULTI_CHANNEL_END_POINT_REPORT_V2 = 0x08
MULTI_INSTANCE_CMD_ENCAP_V2 = 0x06
MULTI_INSTANCE_GET_V2 = 0x04
MULTI_INSTANCE_REPORT_V2 = 0x05
# Values used for Multi Channel Capability Get command
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_END_POINT_MASK_V2 = 0x7F
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_RES_BIT_MASK_V2 = 0x80
# Values used for Multi Channel Capability Report command
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_END_POINT_MASK_V2 = 0x7F
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V2 = 0x80
# Values used for Multi Channel Cmd Encap command
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_SOURCE_END_POINT_MASK_V2 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V2 = 0x80
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_DESTINATION_END_POINT_MASK_V2 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_BIT_ADDRESS_BIT_MASK_V2 = 0x80
# Values used for Multi Channel End Point Report command
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_RES1_MASK_V2 = 0x3F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_IDENTICAL_BIT_MASK_V2 = 0x40
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V2 = 0x80
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_END_POINTS_MASK_V2 = 0x7F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_RES2_BIT_MASK_V2 = 0x80
# Values used for Multi Instance Cmd Encap command
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_INSTANCE_MASK_V2 = 0x7F
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V2 = 0x80
# Values used for Multi Instance Report command
MULTI_INSTANCE_REPORT_PROPERTIES1_INSTANCES_MASK_V2 = 0x7F
MULTI_INSTANCE_REPORT_PROPERTIES1_RES_BIT_MASK_V2 = 0x80

MULTI_CHANNEL_VERSION_V3 = 0x03
MULTI_CHANNEL_CAPABILITY_GET_V3 = 0x09
MULTI_CHANNEL_CAPABILITY_REPORT_V3 = 0x0A
MULTI_CHANNEL_CMD_ENCAP_V3 = 0x0D
MULTI_CHANNEL_END_POINT_FIND_V3 = 0x0B
MULTI_CHANNEL_END_POINT_FIND_REPORT_V3 = 0x0C
MULTI_CHANNEL_END_POINT_GET_V3 = 0x07
MULTI_CHANNEL_END_POINT_REPORT_V3 = 0x08
MULTI_INSTANCE_CMD_ENCAP_V3 = 0x06
MULTI_INSTANCE_GET_V3 = 0x04
MULTI_INSTANCE_REPORT_V3 = 0x05
# Values used for Multi Channel Capability Get command
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_END_POINT_MASK_V3 = 0x7F
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_RES_BIT_MASK_V3 = 0x80
# Values used for Multi Channel Capability Report command
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_END_POINT_MASK_V3 = 0x7F
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V3 = 0x80
# Values used for Multi Channel Cmd Encap command
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_SOURCE_END_POINT_MASK_V3 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V3 = 0x80
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_DESTINATION_END_POINT_MASK_V3 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_BIT_ADDRESS_BIT_MASK_V3 = 0x80
# Values used for Multi Channel End Point Report command
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_RES1_MASK_V3 = 0x3F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_IDENTICAL_BIT_MASK_V3 = 0x40
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V3 = 0x80
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_END_POINTS_MASK_V3 = 0x7F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_RES2_BIT_MASK_V3 = 0x80
# Values used for Multi Instance Cmd Encap command
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_INSTANCE_MASK_V3 = 0x7F
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V3 = 0x80
# Values used for Multi Instance Report command
MULTI_INSTANCE_REPORT_PROPERTIES1_INSTANCES_MASK_V3 = 0x7F
MULTI_INSTANCE_REPORT_PROPERTIES1_RES_BIT_MASK_V3 = 0x80

MULTI_CHANNEL_VERSION_V4 = 0x04
MULTI_CHANNEL_CAPABILITY_GET_V4 = 0x09
MULTI_CHANNEL_CAPABILITY_REPORT_V4 = 0x0A
MULTI_CHANNEL_CMD_ENCAP_V4 = 0x0D
MULTI_CHANNEL_END_POINT_FIND_V4 = 0x0B
MULTI_CHANNEL_END_POINT_FIND_REPORT_V4 = 0x0C
MULTI_CHANNEL_END_POINT_GET_V4 = 0x07
MULTI_CHANNEL_END_POINT_REPORT_V4 = 0x08
MULTI_INSTANCE_CMD_ENCAP_V4 = 0x06
MULTI_INSTANCE_GET_V4 = 0x04
MULTI_INSTANCE_REPORT_V4 = 0x05
MULTI_CHANNEL_AGGREGATED_MEMBERS_GET_V4 = 0x0E
MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT_V4 = 0x0F
# Values used for Multi Channel Capability Get command
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_CAPABILITY_GET_PROPERTIES1_RES_BIT_MASK_V4 = 0x80
# Values used for Multi Channel Capability Report command
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_CAPABILITY_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V4 = 0x80
# Values used for Multi Channel Cmd Encap command
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_SOURCE_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V4 = 0x80
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_DESTINATION_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_CMD_ENCAP_PROPERTIES2_BIT_ADDRESS_BIT_MASK_V4 = 0x80
# Values used for Multi Channel End Point Report command
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_RES1_MASK_V4 = 0x3F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_IDENTICAL_BIT_MASK_V4 = 0x40
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES1_DYNAMIC_BIT_MASK_V4 = 0x80
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_INDIVIDUAL_END_POINTS_MASK_V4 = 0x7F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES2_RES2_BIT_MASK_V4 = 0x80
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES3_AGGREGATED_END_POINTS_MASK_V4 = 0x7F
MULTI_CHANNEL_END_POINT_REPORT_PROPERTIES3_RES3_BIT_MASK_V4 = 0x80
# Values used for Multi Instance Cmd Encap command
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_INSTANCE_MASK_V4 = 0x7F
MULTI_INSTANCE_CMD_ENCAP_PROPERTIES1_RES_BIT_MASK_V4 = 0x80
# Values used for Multi Instance Report command
MULTI_INSTANCE_REPORT_PROPERTIES1_INSTANCES_MASK_V4 = 0x7F
MULTI_INSTANCE_REPORT_PROPERTIES1_RES_BIT_MASK_V4 = 0x80
# Values used for Multi Channel Aggregated Members Get command
MULTI_CHANNEL_AGGREGATED_MEMBERS_GET_PROPERTIES1_AGGREGATED_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_AGGREGATED_MEMBERS_GET_PROPERTIES1_RES_BIT_MASK_V4 = 0x80
# Values used for Multi Channel Aggregated Members Report command
MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT_PROPERTIES1_AGGREGATED_END_POINT_MASK_V4 = 0x7F
MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT_PROPERTIES1_RES_BIT_MASK_V4 = 0x80






class ZW_MULTI_CHANNEL_CMD_ENCAP_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('encapFrame', ALL_EXCEPT_ENCAP),
    ]


class ZW_MULTI_CHANNEL_CAPABILITY_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_MULTI_CHANNEL_CAPABILITY_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
        ('commandClass1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_END_POINT_FIND_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
    ]


class VG_MULTI_CHANNEL_END_POINT_FIND_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [('properties1', uint8_t)]


class ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
        ('variantgroup1', VG_MULTI_CHANNEL_END_POINT_FIND_REPORT_V2_VG),
    ]


class ZW_MULTI_CHANNEL_END_POINT_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_MULTI_INSTANCE_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('commandClass', uint8_t)]


class ZW_MULTI_INSTANCE_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('commandClass', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_CAPABILITY_GET_V3_FRAME(ZW_MULTI_CHANNEL_CAPABILITY_GET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_CAPABILITY_REPORT_V3_FRAME(ZW_MULTI_CHANNEL_CAPABILITY_REPORT_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_FIND_V3_FRAME(ZW_MULTI_CHANNEL_END_POINT_FIND_V2_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_END_POINT_FIND_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [('properties1', uint8_t)]


class ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT_V3_FRAME(ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_GET_V3_FRAME(ZW_MULTI_CHANNEL_END_POINT_GET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_REPORT_V3_FRAME(ZW_MULTI_CHANNEL_END_POINT_REPORT_V2_FRAME):
    _fields_ = []


class ZW_MULTI_INSTANCE_GET_V3_FRAME(ZW_MULTI_INSTANCE_GET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_INSTANCE_REPORT_V3_FRAME(ZW_MULTI_INSTANCE_REPORT_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_CAPABILITY_GET_V4_FRAME(ZW_MULTI_CHANNEL_CAPABILITY_GET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_CAPABILITY_REPORT_V4_FRAME(ZW_MULTI_CHANNEL_CAPABILITY_REPORT_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_FIND_V4_FRAME(ZW_MULTI_CHANNEL_END_POINT_FIND_V3_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_END_POINT_FIND_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [('properties1', uint8_t)]


class ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT_V4_FRAME(ZW_MULTI_CHANNEL_END_POINT_FIND_REPORT_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_GET_V4_FRAME(ZW_MULTI_CHANNEL_END_POINT_GET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_END_POINT_REPORT_V4_FRAME(ZW_MULTI_CHANNEL_END_POINT_REPORT_V3_FRAME):
    _fields_ = [('properties3', uint8_t)]


class ZW_MULTI_INSTANCE_GET_V4_FRAME(ZW_MULTI_INSTANCE_GET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_INSTANCE_REPORT_V4_FRAME(ZW_MULTI_INSTANCE_REPORT_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('numberOfBitMasks', uint8_t),
        ('aggregatedMembersBitMask1', uint8_t),
    ]
