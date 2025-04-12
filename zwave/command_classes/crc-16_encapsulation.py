# CRC-16 Encapsulation Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_CRC_16_ENCAP = 0x56

CRC_16_ENCAP_VERSION = 0x01
# CRC-16 Encapsulated
CRC_16_ENCAP = 0x01



class ZW_CRC_16_ENCAP_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('commandClass', uint8_t),
        ('command', uint8_t),
        ('data1', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]


