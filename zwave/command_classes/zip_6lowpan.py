# Z/IP 6LoWPAN Command Class
# Network-Protocol
COMMAND_CLASS_ZIP_6LOWPAN = 0x4F

ZIP_6LOWPAN_VERSION = 0x01
LOWPAN_FIRST_FRAGMENT = 0xC0
LOWPAN_SUBSEQUENT_FRAGMENT = 0xE0
# Values used for Lowpan First Fragment command
LOWPAN_FIRST_FRAGMENT_MASK = 0xF8
LOWPAN_FIRST_FRAGMENT_DATAGRAM_SIZE_1_MASK = 0x07
# Values used for Lowpan Subsequent Fragment command
LOWPAN_SUBSEQUENT_FRAGMENT_MASK = 0xF8
LOWPAN_SUBSEQUENT_FRAGMENT_DATAGRAM_SIZE_1_MASK = 0x07

class ZW_LOWPAN_FIRST_FRAGMENT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('datagramTag', uint8_t),
        ('payload1', uint8_t),
    ]


class ZW_LOWPAN_SUBSEQUENT_FRAGMENT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('datagramTag', uint8_t),
        ('datagramOffset', uint8_t),
        ('payload1', uint8_t),
    ]

