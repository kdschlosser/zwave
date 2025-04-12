# Remote Association Configuration Command Class
# Management
# ==============================
COMMAND_CLASS_REMOTE_ASSOCIATION = 0x7D

REMOTE_ASSOCIATION_VERSION = 0x01
# Remote Association Configuration Set
REMOTE_ASSOCIATION_CONFIGURATION_SET = 0x01
# Remote Association Configuration Get
REMOTE_ASSOCIATION_CONFIGURATION_GET = 0x02
# Remote Association Configuration Report
REMOTE_ASSOCIATION_CONFIGURATION_REPORT = 0x03



class ZW_REMOTE_ASSOCIATION_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('localGroupingIdentifier', uint8_t)]


class ZW_REMOTE_ASSOCIATION_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('localGroupingIdentifier', uint8_t),
        ('remoteNodeid', uint8_t),
        ('remoteGroupingIdentifier', uint8_t),
    ]


class ZW_REMOTE_ASSOCIATION_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('localGroupingIdentifier', uint8_t),
        ('remoteNodeid', uint8_t),
        ('remoteGroupingIdentifier', uint8_t),
    ]

