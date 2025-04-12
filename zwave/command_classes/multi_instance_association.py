COMMAND_CLASS_MULTI_INSTANCE_ASSOCIATION = 0x8E  # [OBSOLETED]

MULTI_INSTANCE_ASSOCIATION_VERSION = 0x01
MULTI_INSTANCE_ASSOCIATION_GET = 0x02
MULTI_INSTANCE_ASSOCIATION_GROUPINGS_GET = 0x05
MULTI_INSTANCE_ASSOCIATION_GROUPINGS_REPORT = 0x06
MULTI_INSTANCE_ASSOCIATION_REMOVE = 0x04
MULTI_INSTANCE_ASSOCIATION_REPORT = 0x03
MULTI_INSTANCE_ASSOCIATION_SET = 0x01
# Values used for Multi Instance Association Remove command
MULTI_INSTANCE_ASSOCIATION_REMOVE_MARKER = 0x00
# Values used for Multi Instance Association Report command
MULTI_INSTANCE_ASSOCIATION_REPORT_MARKER = 0x00
# Values used for Multi Instance Association Set command
MULTI_INSTANCE_ASSOCIATION_SET_MARKER = 0x00


class ZW_MULTI_INSTANCE_ASSOCIATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('groupingIdentifier', uint8_t)]


class ZW_MULTI_INSTANCE_ASSOCIATION_GROUPINGS_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_MULTI_INSTANCE_ASSOCIATION_GROUPINGS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedGroupings', uint8_t)]


class VG_MULTI_INSTANCE_ASSOCIATION_REMOVE_VG(ctypes.Structure):
    _fields_ = [
        ('multiInstanceNodeId', uint8_t),
        ('instance', uint8_t),
    ]


class ZW_MULTI_INSTANCE_ASSOCIATION_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_INSTANCE_ASSOCIATION_REMOVE_VG),
    ]


class VG_MULTI_INSTANCE_ASSOCIATION_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('multiInstanceNodeId', uint8_t),
        ('instance', uint8_t),
    ]


class ZW_MULTI_INSTANCE_ASSOCIATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('maxNodesSupported', uint8_t),
        ('reportsToFollow', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_INSTANCE_ASSOCIATION_REPORT_VG),
    ]


class VG_MULTI_INSTANCE_ASSOCIATION_SET_VG(ctypes.Structure):
    _fields_ = [
        ('multiInstanceNodeId', uint8_t),
        ('instance', uint8_t),
    ]


class ZW_MULTI_INSTANCE_ASSOCIATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_INSTANCE_ASSOCIATION_SET_VG),
    ]

