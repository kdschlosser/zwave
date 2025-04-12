# Transport Service Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_TRANSPORT_SERVICE = 0x55
# First Segment
COMMAND_FIRST_FRAGMENT = 0xC0
# Segment Complete
COMMAND_FRAGMENT_COMPLETE = 0xE8
# Segment Request
COMMAND_FRAGMENT_REQUEST = 0xC8
# Segment Wait
COMMAND_FRAGMENT_WAIT = 0xF0
# Subsequent segment
COMMAND_SUBSEQUENT_FRAGMENT = 0xE0


TRANSPORT_SERVICE_VERSION_V2 = 0x02
COMMAND_FIRST_SEGMENT_V2 = 0xC0
COMMAND_SEGMENT_COMPLETE_V2 = 0xE8
COMMAND_SEGMENT_REQUEST_V2 = 0xC8
COMMAND_SEGMENT_WAIT_V2 = 0xF0
COMMAND_SUBSEQUENT_SEGMENT_V2 = 0xE0
# Values used for Command First Segment command
COMMAND_FIRST_SEGMENT_MASK_V2 = 0xF8
COMMAND_FIRST_SEGMENT_DATAGRAM_SIZE_1_MASK_V2 = 0x07
COMMAND_FIRST_SEGMENT_PROPERTIES2_RESERVED_MASK_V2 = 0x07
COMMAND_FIRST_SEGMENT_PROPERTIES2_EXT_BIT_MASK_V2 = 0x08
COMMAND_FIRST_SEGMENT_PROPERTIES2_SESSION_ID_MASK_V2 = 0xF0
COMMAND_FIRST_SEGMENT_PROPERTIES2_SESSION_ID_SHIFT_V2 = 0x04
# Values used for Command Segment Complete command
COMMAND_SEGMENT_COMPLETE_MASK_V2 = 0xF8
COMMAND_SEGMENT_COMPLETE_RESERVED_MASK_V2 = 0x07
COMMAND_SEGMENT_COMPLETE_PROPERTIES2_RESERVED2_MASK_V2 = 0x0F
COMMAND_SEGMENT_COMPLETE_PROPERTIES2_SESSION_ID_MASK_V2 = 0xF0
COMMAND_SEGMENT_COMPLETE_PROPERTIES2_SESSION_ID_SHIFT_V2 = 0x04
# Values used for Command Segment Request command
COMMAND_SEGMENT_REQUEST_MASK_V2 = 0xF8
COMMAND_SEGMENT_REQUEST_RESERVED_MASK_V2 = 0x07
COMMAND_SEGMENT_REQUEST_PROPERTIES2_DATAGRAM_OFFSET_1_MASK_V2 = 0x07
COMMAND_SEGMENT_REQUEST_PROPERTIES2_RESERVED2_BIT_MASK_V2 = 0x08
COMMAND_SEGMENT_REQUEST_PROPERTIES2_SESSION_ID_MASK_V2 = 0xF0
COMMAND_SEGMENT_REQUEST_PROPERTIES2_SESSION_ID_SHIFT_V2 = 0x04
# Values used for Command Segment Wait command
COMMAND_SEGMENT_WAIT_MASK_V2 = 0xF8
COMMAND_SEGMENT_WAIT_RESERVED_MASK_V2 = 0x07
# Values used for Command Subsequent Segment command
COMMAND_SUBSEQUENT_SEGMENT_MASK_V2 = 0xF8
COMMAND_SUBSEQUENT_SEGMENT_DATAGRAM_SIZE_1_MASK_V2 = 0x07
COMMAND_SUBSEQUENT_SEGMENT_PROPERTIES2_DATAGRAM_OFFSET_1_MASK_V2 = 0x07
COMMAND_SUBSEQUENT_SEGMENT_PROPERTIES2_EXT_BIT_MASK_V2 = 0x08
COMMAND_SUBSEQUENT_SEGMENT_PROPERTIES2_SESSION_ID_MASK_V2 = 0xF0
COMMAND_SUBSEQUENT_SEGMENT_PROPERTIES2_SESSION_ID_SHIFT_V2 = 0x04

TRANSPORT_SERVICE_VERSION = 0x01
COMMAND_FIRST_FRAGMENT = 0xC0
COMMAND_SUBSEQUENT_FRAGMENT = 0xE0
# Values used for Command First Fragment command
COMMAND_FIRST_FRAGMENT_MASK = 0xF8
COMMAND_FIRST_FRAGMENT_DATAGRAM_SIZE_1_MASK = 0x07
COMMAND_FIRST_FRAGMENT_PROPERTIES2_SEQUENCE_NO_MASK = 0x0F
COMMAND_FIRST_FRAGMENT_PROPERTIES2_RESERVED_MASK = 0xF0
COMMAND_FIRST_FRAGMENT_PROPERTIES2_RESERVED_SHIFT = 0x04
# Values used for Command Subsequent Fragment command
COMMAND_SUBSEQUENT_FRAGMENT_MASK = 0xF8
COMMAND_SUBSEQUENT_FRAGMENT_DATAGRAM_SIZE_1_MASK = 0x07
COMMAND_SUBSEQUENT_FRAGMENT_PROPERTIES2_DATAGRAM_OFFSET_1_MASK = 0x07
COMMAND_SUBSEQUENT_FRAGMENT_PROPERTIES2_SEQUENCE_NO_MASK = 0x78
COMMAND_SUBSEQUENT_FRAGMENT_PROPERTIES2_SEQUENCE_NO_SHIFT = 0x03
COMMAND_SUBSEQUENT_FRAGMENT_PROPERTIES2_RESERVED_BIT_MASK = 0x80


class ZW_COMMAND_FIRST_SEGMENT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('properties2', uint8_t),
        ('headerExtensionLength', uint8_t),
        ('headerExtension1', uint8_t),
        ('payload1', uint8_t),
        ('frameCheckSequence1', uint8_t),
        ('frameCheckSequence2', uint8_t),
    ]


class ZW_COMMAND_SEGMENT_COMPLETE_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_reserved', uint8_t),
        ('properties2', uint8_t),
    ]


class ZW_COMMAND_SEGMENT_REQUEST_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_reserved', uint8_t),
        ('properties2', uint8_t),
        ('datagramOffset2', uint8_t),
    ]


class ZW_COMMAND_SEGMENT_WAIT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_reserved', uint8_t),
        ('pendingFragments', uint8_t),
    ]


class ZW_COMMAND_SUBSEQUENT_SEGMENT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('properties2', uint8_t),
        ('datagramOffset2', uint8_t),
        ('headerExtensionLength', uint8_t),
        ('headerExtension1', uint8_t),
        ('payload1', uint8_t),
        ('frameCheckSequence1', uint8_t),
        ('frameCheckSequence2', uint8_t),
    ]


class ZW_COMMAND_FIRST_FRAGMENT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('properties2', uint8_t),
        ('payload1', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]


class ZW_COMMAND_SUBSEQUENT_FRAGMENT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('cmd_datagramSize1', uint8_t),
        ('datagramSize2', uint8_t),
        ('properties2', uint8_t),
        ('datagramOffset2', uint8_t),
        ('payload1', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]

