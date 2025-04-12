# Z/IP Portal Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_ZIP_PORTAL = 0x61

ZIP_PORTAL_VERSION = 0x01
# Gateway Configuration Set
GATEWAY_CONFIGURATION_SET = 0x01
# Gateway Configuration Status
GATEWAY_CONFIGURATION_STATUS = 0x02
# Gateway Configuration Get
GATEWAY_CONFIGURATION_GET = 0x03
# Gateway Configuration Report
GATEWAY_CONFIGURATION_REPORT = 0x04

GATEWAY_UNREGISTER = 0x05

class ZW_GATEWAY_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('lanIpv6Address1', uint8_t),
        ('lanIpv6Address2', uint8_t),
        ('lanIpv6Address3', uint8_t),
        ('lanIpv6Address4', uint8_t),
        ('lanIpv6Address5', uint8_t),
        ('lanIpv6Address6', uint8_t),
        ('lanIpv6Address7', uint8_t),
        ('lanIpv6Address8', uint8_t),
        ('lanIpv6Address9', uint8_t),
        ('lanIpv6Address10', uint8_t),
        ('lanIpv6Address11', uint8_t),
        ('lanIpv6Address12', uint8_t),
        ('lanIpv6Address13', uint8_t),
        ('lanIpv6Address14', uint8_t),
        ('lanIpv6Address15', uint8_t),
        ('lanIpv6Address16', uint8_t),
        ('lanIpv6PrefixLength', uint8_t),
        ('portalIpv6Prefix1', uint8_t),
        ('portalIpv6Prefix2', uint8_t),
        ('portalIpv6Prefix3', uint8_t),
        ('portalIpv6Prefix4', uint8_t),
        ('portalIpv6Prefix5', uint8_t),
        ('portalIpv6Prefix6', uint8_t),
        ('portalIpv6Prefix7', uint8_t),
        ('portalIpv6Prefix8', uint8_t),
        ('portalIpv6Prefix9', uint8_t),
        ('portalIpv6Prefix10', uint8_t),
        ('portalIpv6Prefix11', uint8_t),
        ('portalIpv6Prefix12', uint8_t),
        ('portalIpv6Prefix13', uint8_t),
        ('portalIpv6Prefix14', uint8_t),
        ('portalIpv6Prefix15', uint8_t),
        ('portalIpv6Prefix16', uint8_t),
        ('portalIpv6PrefixLength', uint8_t),
        ('defaultGatewayIpv6Address1', uint8_t),
        ('defaultGatewayIpv6Address2', uint8_t),
        ('defaultGatewayIpv6Address3', uint8_t),
        ('defaultGatewayIpv6Address4', uint8_t),
        ('defaultGatewayIpv6Address5', uint8_t),
        ('defaultGatewayIpv6Address6', uint8_t),
        ('defaultGatewayIpv6Address7', uint8_t),
        ('defaultGatewayIpv6Address8', uint8_t),
        ('defaultGatewayIpv6Address9', uint8_t),
        ('defaultGatewayIpv6Address10', uint8_t),
        ('defaultGatewayIpv6Address11', uint8_t),
        ('defaultGatewayIpv6Address12', uint8_t),
        ('defaultGatewayIpv6Address13', uint8_t),
        ('defaultGatewayIpv6Address14', uint8_t),
        ('defaultGatewayIpv6Address15', uint8_t),
        ('defaultGatewayIpv6Address16', uint8_t),
        ('panIpv6Prefix1', uint8_t),
        ('panIpv6Prefix2', uint8_t),
        ('panIpv6Prefix3', uint8_t),
        ('panIpv6Prefix4', uint8_t),
        ('panIpv6Prefix5', uint8_t),
        ('panIpv6Prefix6', uint8_t),
        ('panIpv6Prefix7', uint8_t),
        ('panIpv6Prefix8', uint8_t),
        ('panIpv6Prefix9', uint8_t),
        ('panIpv6Prefix10', uint8_t),
        ('panIpv6Prefix11', uint8_t),
        ('panIpv6Prefix12', uint8_t),
        ('panIpv6Prefix13', uint8_t),
        ('panIpv6Prefix14', uint8_t),
        ('panIpv6Prefix15', uint8_t),
        ('panIpv6Prefix16', uint8_t),
    ]


class ZW_GATEWAY_CONFIGURATION_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('status', uint8_t)]


class ZW_GATEWAY_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_GATEWAY_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('lanIpv6Address1', uint8_t),
        ('lanIpv6Address2', uint8_t),
        ('lanIpv6Address3', uint8_t),
        ('lanIpv6Address4', uint8_t),
        ('lanIpv6Address5', uint8_t),
        ('lanIpv6Address6', uint8_t),
        ('lanIpv6Address7', uint8_t),
        ('lanIpv6Address8', uint8_t),
        ('lanIpv6Address9', uint8_t),
        ('lanIpv6Address10', uint8_t),
        ('lanIpv6Address11', uint8_t),
        ('lanIpv6Address12', uint8_t),
        ('lanIpv6Address13', uint8_t),
        ('lanIpv6Address14', uint8_t),
        ('lanIpv6Address15', uint8_t),
        ('lanIpv6Address16', uint8_t),
        ('lanIpv6PrefixLength', uint8_t),
        ('portalIpv6Prefix1', uint8_t),
        ('portalIpv6Prefix2', uint8_t),
        ('portalIpv6Prefix3', uint8_t),
        ('portalIpv6Prefix4', uint8_t),
        ('portalIpv6Prefix5', uint8_t),
        ('portalIpv6Prefix6', uint8_t),
        ('portalIpv6Prefix7', uint8_t),
        ('portalIpv6Prefix8', uint8_t),
        ('portalIpv6Prefix9', uint8_t),
        ('portalIpv6Prefix10', uint8_t),
        ('portalIpv6Prefix11', uint8_t),
        ('portalIpv6Prefix12', uint8_t),
        ('portalIpv6Prefix13', uint8_t),
        ('portalIpv6Prefix14', uint8_t),
        ('portalIpv6Prefix15', uint8_t),
        ('portalIpv6Prefix16', uint8_t),
        ('portalIpv6PrefixLength', uint8_t),
        ('defaultGatewayIpv6Address1', uint8_t),
        ('defaultGatewayIpv6Address2', uint8_t),
        ('defaultGatewayIpv6Address3', uint8_t),
        ('defaultGatewayIpv6Address4', uint8_t),
        ('defaultGatewayIpv6Address5', uint8_t),
        ('defaultGatewayIpv6Address6', uint8_t),
        ('defaultGatewayIpv6Address7', uint8_t),
        ('defaultGatewayIpv6Address8', uint8_t),
        ('defaultGatewayIpv6Address9', uint8_t),
        ('defaultGatewayIpv6Address10', uint8_t),
        ('defaultGatewayIpv6Address11', uint8_t),
        ('defaultGatewayIpv6Address12', uint8_t),
        ('defaultGatewayIpv6Address13', uint8_t),
        ('defaultGatewayIpv6Address14', uint8_t),
        ('defaultGatewayIpv6Address15', uint8_t),
        ('defaultGatewayIpv6Address16', uint8_t),
        ('panIpv6Prefix1', uint8_t),
        ('panIpv6Prefix2', uint8_t),
        ('panIpv6Prefix3', uint8_t),
        ('panIpv6Prefix4', uint8_t),
        ('panIpv6Prefix5', uint8_t),
        ('panIpv6Prefix6', uint8_t),
        ('panIpv6Prefix7', uint8_t),
        ('panIpv6Prefix8', uint8_t),
        ('panIpv6Prefix9', uint8_t),
        ('panIpv6Prefix10', uint8_t),
        ('panIpv6Prefix11', uint8_t),
        ('panIpv6Prefix12', uint8_t),
        ('panIpv6Prefix13', uint8_t),
        ('panIpv6Prefix14', uint8_t),
        ('panIpv6Prefix15', uint8_t),
        ('panIpv6Prefix16', uint8_t),
    ]


class ZW_GATEWAY_UNREGISTER_FRAME(ZW_COMMON_FRAME):
    _fields_ = []

