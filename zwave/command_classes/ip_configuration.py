# IP Configuration Command Class
# Management
# ==============================
COMMAND_CLASS_IP_CONFIGURATION = 0x9A

IP_CONFIGURATION_VERSION = 0x01
# IP Configuration Set
IP_CONFIGURATION_SET = 0x01
# IP Configuration Get
IP_CONFIGURATION_GET = 0x02
# IP Configuration Report
IP_CONFIGURATION_REPORT = 0x03
# IP Configuration DHCP Release
IP_CONFIGURATION_RELEASE = 0x04
# IP Configuration DHCP Renew
IP_CONFIGURATION_RENEW = 0x05

# Values used for Ip Configuration Report command
IP_CONFIGURATION_REPORT_PROPERTIES1_AUTO_DNS_BIT_MASK = 0x01
IP_CONFIGURATION_REPORT_PROPERTIES1_AUTO_IP_BIT_MASK = 0x02
IP_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
IP_CONFIGURATION_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Ip Configuration Set command
IP_CONFIGURATION_SET_PROPERTIES1_AUTO_DNS_BIT_MASK = 0x01
IP_CONFIGURATION_SET_PROPERTIES1_AUTO_IP_BIT_MASK = 0x02
IP_CONFIGURATION_SET_PROPERTIES1_RESERVED_MASK = 0xFC
IP_CONFIGURATION_SET_PROPERTIES1_RESERVED_SHIFT = 0x02


class ZW_IP_CONFIGURATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IP_CONFIGURATION_RELEASE_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IP_CONFIGURATION_RENEW_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_IP_CONFIGURATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('ipAddress1', uint8_t),
        ('ipAddress2', uint8_t),
        ('ipAddress3', uint8_t),
        ('ipAddress4', uint8_t),
        ('subnetMask1', uint8_t),
        ('subnetMask2', uint8_t),
        ('subnetMask3', uint8_t),
        ('subnetMask4', uint8_t),
        ('gateway1', uint8_t),
        ('gateway2', uint8_t),
        ('gateway3', uint8_t),
        ('gateway4', uint8_t),
        ('dns11', uint8_t),
        ('dns12', uint8_t),
        ('dns13', uint8_t),
        ('dns14', uint8_t),
        ('dns21', uint8_t),
        ('dns22', uint8_t),
        ('dns23', uint8_t),
        ('dns24', uint8_t),
        ('leasetime1', uint8_t),
        ('leasetime2', uint8_t),
        ('leasetime3', uint8_t),
        ('leasetime4', uint8_t),
    ]


class ZW_IP_CONFIGURATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('ipAddress1', uint8_t),
        ('ipAddress2', uint8_t),
        ('ipAddress3', uint8_t),
        ('ipAddress4', uint8_t),
        ('subnetMask1', uint8_t),
        ('subnetMask2', uint8_t),
        ('subnetMask3', uint8_t),
        ('subnetMask4', uint8_t),
        ('gateway1', uint8_t),
        ('gateway2', uint8_t),
        ('gateway3', uint8_t),
        ('gateway4', uint8_t),
        ('dns11', uint8_t),
        ('dns12', uint8_t),
        ('dns13', uint8_t),
        ('dns14', uint8_t),
        ('dns21', uint8_t),
        ('dns22', uint8_t),
        ('dns23', uint8_t),
        ('dns24', uint8_t),
    ]


