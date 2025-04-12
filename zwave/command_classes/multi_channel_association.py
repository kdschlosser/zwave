# Multi Channel Association Command Class
# Management
# ==============================
COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION = 0x8E
# Multi Channel Association Set
MULTI_CHANNEL_ASSOCIATION_SET = 0x01
# Multi Channel Association Get
MULTI_CHANNEL_ASSOCIATION_GET = 0x02
# Multi Channel Association Report
MULTI_CHANNEL_ASSOCIATION_REPORT = 0x03
# Multi Channel Association Remove
MULTI_CHANNEL_ASSOCIATION_REMOVE = 0x04
# Multi Channel Association Groupings Get
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET = 0x05
# Multi Channel Association Groupings Report
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT = 0x06

MULTI_CHANNEL_ASSOCIATION_VERSION_V2 = 0x02
MULTI_CHANNEL_ASSOCIATION_GET_V2 = 0x02
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V2 = 0x05
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V2 = 0x06
MULTI_CHANNEL_ASSOCIATION_REMOVE_V2 = 0x04
MULTI_CHANNEL_ASSOCIATION_REPORT_V2 = 0x03
MULTI_CHANNEL_ASSOCIATION_SET_V2 = 0x01
# Values used for Multi Channel Association Remove command
MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER_V2 = 0x00
# Values used for Multi Channel Association Report command
MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER_V2 = 0x00
# Values used for Multi Channel Association Set command
MULTI_CHANNEL_ASSOCIATION_SET_MARKER_V2 = 0x00

MULTI_CHANNEL_ASSOCIATION_VERSION_V3 = 0x03
MULTI_CHANNEL_ASSOCIATION_GET_V3 = 0x02
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V3 = 0x05
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V3 = 0x06
MULTI_CHANNEL_ASSOCIATION_REMOVE_V3 = 0x04
MULTI_CHANNEL_ASSOCIATION_REPORT_V3 = 0x03
MULTI_CHANNEL_ASSOCIATION_SET_V3 = 0x01
# Values used for Multi Channel Association Remove command
MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER_V3 = 0x00
# Values used for Multi Channel Association Report command
MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER_V3 = 0x00
# Values used for Multi Channel Association Set command
MULTI_CHANNEL_ASSOCIATION_SET_MARKER_V3 = 0x00

MULTI_CHANNEL_ASSOCIATION_VERSION_V4 = 0x04
MULTI_CHANNEL_ASSOCIATION_GET_V4 = 0x02
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V4 = 0x05
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V4 = 0x06
MULTI_CHANNEL_ASSOCIATION_REMOVE_V4 = 0x04
MULTI_CHANNEL_ASSOCIATION_REPORT_V4 = 0x03
MULTI_CHANNEL_ASSOCIATION_SET_V4 = 0x01
# Values used for Multi Channel Association Remove command
MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER_V4 = 0x00
# Values used for Multi Channel Association Report command
MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER_V4 = 0x00
# Values used for Multi Channel Association Set command
MULTI_CHANNEL_ASSOCIATION_SET_MARKER_V4 = 0x00

MULTI_CHANNEL_ASSOCIATION_VERSION_V5 = 0x05
MULTI_CHANNEL_ASSOCIATION_GET_V5 = 0x02
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V5 = 0x05
MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V5 = 0x06
MULTI_CHANNEL_ASSOCIATION_REMOVE_V5 = 0x04
MULTI_CHANNEL_ASSOCIATION_REPORT_V5 = 0x03
MULTI_CHANNEL_ASSOCIATION_SET_V5 = 0x01
# Values used for Multi Channel Association Remove command
MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER_V5 = 0x00
# Values used for Multi Channel Association Report command
MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER_V5 = 0x00
# Values used for Multi Channel Association Set command
MULTI_CHANNEL_ASSOCIATION_SET_MARKER_V5 = 0x00


class ZW_MULTI_CHANNEL_ASSOCIATION_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('groupingIdentifier', uint8_t)]


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedGroupings', uint8_t)]


class VG_MULTI_CHANNEL_ASSOCIATION_REMOVE_V2_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_CHANNEL_ASSOCIATION_REMOVE_V2_VG),
    ]


class VG_MULTI_CHANNEL_ASSOCIATION_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('maxNodesSupported', uint8_t),
        ('reportsToFollow', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_CHANNEL_ASSOCIATION_REPORT_V2_VG),
    ]


class VG_MULTI_CHANNEL_ASSOCIATION_SET_V2_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('nodeId1', uint8_t),
        ('marker', uint8_t),
        ('variantgroup1', VG_MULTI_CHANNEL_ASSOCIATION_SET_V2_VG),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_GET_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V2_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REMOVE_V3_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V2_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V2_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_SET_V3_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_SET_V3_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_SET_V2_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GET_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V3_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REMOVE_V4_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V3_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V3_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_SET_V4_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_SET_V4_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_SET_V3_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GET_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GET_V4_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET_V4_FRAME):
    _fields_ = []


class ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_GROUPINGS_REPORT_V4_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REMOVE_V5_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REMOVE_V4_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_REPORT_V5_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_REPORT_V4_FRAME):
    _fields_ = []


class VG_MULTI_CHANNEL_ASSOCIATION_SET_V5_VG(ctypes.Structure):
    _fields_ = [
        ('multiChannelNodeId', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_MULTI_CHANNEL_ASSOCIATION_SET_V5_FRAME(ZW_MULTI_CHANNEL_ASSOCIATION_SET_V4_FRAME):
    _fields_ = []




