# IP Association Command Class
# Management
COMMAND_CLASS_IP_ASSOCIATION = 0x5C

IP_ASSOCIATION_VERSION = 0x01
IP_ASSOCIATION_SET = 0x01
IP_ASSOCIATION_GET = 0x02
IP_ASSOCIATION_REPORT = 0x03
IP_ASSOCIATION_REMOVE = 0x04

class ZW_IP_ASSOCIATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
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
        ('endPoint', uint8_t),
    ]


class ZW_IP_ASSOCIATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('index', uint8_t),
    ]


class ZW_IP_ASSOCIATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
        ('index', uint8_t),
        ('actualNodes', uint8_t),
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
        ('endPoint', uint8_t),
    ]


class ZW_IP_ASSOCIATION_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('groupingIdentifier', uint8_t),
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
        ('endPoint', uint8_t),
    ]

