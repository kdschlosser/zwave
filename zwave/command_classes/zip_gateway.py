# Z/IP Gateway Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_ZIP_GATEWAY = 0x5F

ZIP_GATEWAY_VERSION = 0x01
# Gateway Mode Set
GATEWAY_MODE_SET = 0x01
# Gateway Mode Get
GATEWAY_MODE_GET = 0x02
# Gateway Mode Report
GATEWAY_MODE_REPORT = 0x03
# Gateway Peer Set
GATEWAY_PEER_SET = 0x04
# Gateway Peer Get
GATEWAY_PEER_GET = 0x05
# Gateway Peer Report
GATEWAY_PEER_REPORT = 0x06
# Gateway Lock Set
GATEWAY_LOCK_SET = 0x07
# Unsolicited Destination Set
UNSOLICITED_DESTINATION_SET = 0x08
# Unsolicited Destination Get
UNSOLICITED_DESTINATION_GET = 0x09
# Unsolicited Destination Report
UNSOLICITED_DESTINATION_REPORT = 0x0A
# Application Node Info Set
COMMAND_APPLICATION_NODE_INFO_SET = 0x0B
# Application Node Info Get
COMMAND_APPLICATION_NODE_INFO_GET = 0x0C
# Application Node Info Report
COMMAND_APPLICATION_NODE_INFO_REPORT = 0x0D

# Values used for Gateway Mode Set command
GATEWAY_MODE_SET_STAND_ALONE = 0x01
GATEWAY_MODE_SET_PORTAL = 0x02
# Values used for Gateway Mode Report command
GATEWAY_MODE_REPORT_STAND_ALONE = 0x01
GATEWAY_MODE_REPORT_PORTAL = 0x02
# Values used for Gateway Peer Set command
GATEWAY_PEER_SET_PROPERTIES1_PEER_NAME_LENGTH_MASK = 0x3F
GATEWAY_PEER_SET_PROPERTIES1_RESERVED_MASK = 0xC0
GATEWAY_PEER_SET_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Gateway Peer Report command
GATEWAY_PEER_REPORT_PROPERTIES1_PEER_NAME_LENGTH_MASK = 0x3F
GATEWAY_PEER_REPORT_PROPERTIES1_RESERVED_MASK = 0xC0
GATEWAY_PEER_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Gateway Lock Set command
GATEWAY_LOCK_SET_PROPERTIES1_LOCK_BIT_MASK = 0x01
GATEWAY_LOCK_SET_PROPERTIES1_SHOW_BIT_MASK = 0x02
GATEWAY_LOCK_SET_PROPERTIES1_RESERVED_MASK = 0xFC
GATEWAY_LOCK_SET_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Command Application Node Info Set command
COMMAND_APPLICATION_NODE_INFO_SET_SECURITY_SCHEME_0_MARK = 0xF100
# Values used for Command Application Node Info Report command
COMMAND_APPLICATION_NODE_INFO_REPORT_SECURITY_SCHEME_0_MARK = 0xF100

class ZW_GATEWAY_MODE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('mode', uint8_t)]


class ZW_GATEWAY_MODE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_GATEWAY_MODE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('mode', uint8_t)]


class ZW_GATEWAY_PEER_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('peerProfile', uint8_t),
        ('ipv6Address1', uint8_t),
        ('ipv6Address2', uint8_t),
        ('ipv6Address3', uint8_t),
        ('ipv6Address4', uint8_t),
        ('ipv6Address5', uint8_t),
        ('ipv6Address6', uint8_t),
        ('ipv6Address7', uint8_t),
        ('ipv6Address8', uint8_t),
        ('ipv6Address9', uint8_t),
        ('ipv6Address10', uint8_t),
        ('ipv6Address11', uint8_t),
        ('ipv6Address12', uint8_t),
        ('ipv6Address13', uint8_t),
        ('ipv6Address14', uint8_t),
        ('ipv6Address15', uint8_t),
        ('ipv6Address16', uint8_t),
        ('port1', uint8_t),
        ('port2', uint8_t),
        ('properties1', uint8_t),
        ('peerName1', uint8_t),
    ]


class ZW_GATEWAY_PEER_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('peerProfile', uint8_t)]


class ZW_GATEWAY_PEER_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('peerProfile', uint8_t),
        ('peerCount', uint8_t),
        ('ipv6Address1', uint8_t),
        ('ipv6Address2', uint8_t),
        ('ipv6Address3', uint8_t),
        ('ipv6Address4', uint8_t),
        ('ipv6Address5', uint8_t),
        ('ipv6Address6', uint8_t),
        ('ipv6Address7', uint8_t),
        ('ipv6Address8', uint8_t),
        ('ipv6Address9', uint8_t),
        ('ipv6Address10', uint8_t),
        ('ipv6Address11', uint8_t),
        ('ipv6Address12', uint8_t),
        ('ipv6Address13', uint8_t),
        ('ipv6Address14', uint8_t),
        ('ipv6Address15', uint8_t),
        ('ipv6Address16', uint8_t),
        ('port1', uint8_t),
        ('port2', uint8_t),
        ('properties1', uint8_t),
        ('peerName1', uint8_t),
    ]


class ZW_GATEWAY_LOCK_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_UNSOLICITED_DESTINATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('unsolicitedIpv6Destination1', uint8_t),
        ('unsolicitedIpv6Destination2', uint8_t),
        ('unsolicitedIpv6Destination3', uint8_t),
        ('unsolicitedIpv6Destination4', uint8_t),
        ('unsolicitedIpv6Destination5', uint8_t),
        ('unsolicitedIpv6Destination6', uint8_t),
        ('unsolicitedIpv6Destination7', uint8_t),
        ('unsolicitedIpv6Destination8', uint8_t),
        ('unsolicitedIpv6Destination9', uint8_t),
        ('unsolicitedIpv6Destination10', uint8_t),
        ('unsolicitedIpv6Destination11', uint8_t),
        ('unsolicitedIpv6Destination12', uint8_t),
        ('unsolicitedIpv6Destination13', uint8_t),
        ('unsolicitedIpv6Destination14', uint8_t),
        ('unsolicitedIpv6Destination15', uint8_t),
        ('unsolicitedIpv6Destination16', uint8_t),
        ('unsolicitedDestinationPort1', uint8_t),
        ('unsolicitedDestinationPort2', uint8_t),
    ]


class ZW_UNSOLICITED_DESTINATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_UNSOLICITED_DESTINATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('unsolicitedIpv6Destination1', uint8_t),
        ('unsolicitedIpv6Destination2', uint8_t),
        ('unsolicitedIpv6Destination3', uint8_t),
        ('unsolicitedIpv6Destination4', uint8_t),
        ('unsolicitedIpv6Destination5', uint8_t),
        ('unsolicitedIpv6Destination6', uint8_t),
        ('unsolicitedIpv6Destination7', uint8_t),
        ('unsolicitedIpv6Destination8', uint8_t),
        ('unsolicitedIpv6Destination9', uint8_t),
        ('unsolicitedIpv6Destination10', uint8_t),
        ('unsolicitedIpv6Destination11', uint8_t),
        ('unsolicitedIpv6Destination12', uint8_t),
        ('unsolicitedIpv6Destination13', uint8_t),
        ('unsolicitedIpv6Destination14', uint8_t),
        ('unsolicitedIpv6Destination15', uint8_t),
        ('unsolicitedIpv6Destination16', uint8_t),
        ('unsolicitedDestinationPort1', uint8_t),
        ('unsolicitedDestinationPort2', uint8_t),
    ]


class ZW_COMMAND_APPLICATION_NODE_INFO_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('nonSecureCommandClass1', uint8_t),
        ('securityScheme0Mark1', uint8_t),
        ('securityScheme0Mark2', uint8_t),
        ('securityScheme0CommandClass1', uint8_t),
    ]


class ZW_COMMAND_APPLICATION_NODE_INFO_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_COMMAND_APPLICATION_NODE_INFO_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('nonSecureCommandClass1', uint8_t),
        ('securityScheme0Mark1', uint8_t),
        ('securityScheme0Mark2', uint8_t),
        ('securityScheme0CommandClass1', uint8_t),
    ]

