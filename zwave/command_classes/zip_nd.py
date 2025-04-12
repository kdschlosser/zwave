# Z/IP ND Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_ZIP_ND = 0x58

ZIP_ND_VERSION = 0x01
# Z/IP Node Advertisement
ZIP_NODE_ADVERTISEMENT = 0x01
# Z/IP Node Solicitation
ZIP_NODE_SOLICITATION = 0x03
# Z/IP Inverse Node Solicitation
ZIP_INV_NODE_SOLICITATION = 0x04

# Values used for Zip Inv Node Solicitation command
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED1_MASK = 0x03
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_LOCAL_BIT_MASK = 0x04
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED2_MASK = 0xF8
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED2_SHIFT = 0x03
# Values used for Zip Node Advertisement command
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_VALIDITY_MASK = 0x03
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_OK = 0x00
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_OBSOLETE = 0x01
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_NOT_FOUND = 0x02
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_LOCAL_BIT_MASK = 0x04
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_RESERVED_MASK = 0xF8
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_RESERVED_SHIFT = 0x03

ZIP_ND_VERSION_V2 = 0x02
ZIP_NODE_SOLICITATION_V2 = 0x03
ZIP_INV_NODE_SOLICITATION_V2 = 0x04
ZIP_NODE_ADVERTISEMENT_V2 = 0x01
# Values used for Zip Inv Node Solicitation command
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED1_MASK_V2 = 0x03
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_LOCAL_BIT_MASK_V2 = 0x04
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED2_MASK_V2 = 0xF8
ZIP_INV_NODE_SOLICITATION_PROPERTIES1_RESERVED2_SHIFT_V2 = 0x03
# Values used for Zip Node Advertisement command
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_VALIDITY_MASK_V2 = 0x03
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_OK_V2 = 0x00
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_OBSOLETE_V2 = 0x01
ZIP_NODE_ADVERTISEMENT_VALIDITY_INFORMATION_NOT_FOUND_V2 = 0x02
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_LOCAL_BIT_MASK_V2 = 0x04
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_RESERVED_MASK_V2 = 0xF8
ZIP_NODE_ADVERTISEMENT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x03


class ZW_ZIP_NODE_SOLICITATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reserved', uint8_t),
        ('nodeId', uint8_t),
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
    ]


class ZW_ZIP_INV_NODE_SOLICITATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_ZIP_NODE_ADVERTISEMENT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('nodeId', uint8_t),
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
        ('homeId1', uint8_t),
        ('homeId2', uint8_t),
        ('homeId3', uint8_t),
        ('homeId4', uint8_t),
    ]


class ZW_ZIP_NODE_SOLICITATION_V2_FRAME(ZW_ZIP_NODE_SOLICITATION_FRAME):
    _fields_ = []


class ZW_ZIP_INV_NODE_SOLICITATION_V2_FRAME(ZW_ZIP_INV_NODE_SOLICITATION_FRAME):
    _fields_ = [
        ('extendedNodeid1', uint8_t),
        ('extendedNodeid2', uint8_t),
    ]


class ZW_ZIP_NODE_ADVERTISEMENT_V2_FRAME(ZW_ZIP_NODE_ADVERTISEMENT_FRAME):
    _fields_ = [
        ('extendedNodeid1', uint8_t),
        ('extendedNodeid2', uint8_t),
    ]

