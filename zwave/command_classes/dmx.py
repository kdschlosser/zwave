COMMAND_CLASS_DMX = 0x65

DMX_VERSION = 0x01
DMX_ADDRESS_SET = 0x01
DMX_ADDRESS_GET = 0x02
DMX_ADDRESS_REPORT = 0x03
DMX_CAPABILITY_GET = 0x04
DMX_CAPABILITY_REPORT = 0x05
DMX_DATA = 0x06
# Values used for Dmx Address Set command
DMX_ADDRESS_SET_PROPERTIES1_PAGE_ID_MASK = 0x0F
DMX_ADDRESS_SET_PROPERTIES1_RESERVED_MASK = 0xF0
DMX_ADDRESS_SET_PROPERTIES1_RESERVED_SHIFT = 0x04
# Values used for Dmx Address Report command
DMX_ADDRESS_REPORT_PROPERTIES1_PAGE_ID_MASK = 0x0F
DMX_ADDRESS_REPORT_PROPERTIES1_RESERVED_MASK = 0xF0
DMX_ADDRESS_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x04
# Values used for Dmx Data command
DMX_DATA_PROPERTIES1_PAGE_MASK = 0x0F
DMX_DATA_PROPERTIES1_SEQUENCE_NO_MASK = 0x30
DMX_DATA_PROPERTIES1_SEQUENCE_NO_SHIFT = 0x04
DMX_DATA_PROPERTIES1_RESERVED_MASK = 0xC0
DMX_DATA_PROPERTIES1_RESERVED_SHIFT = 0x06

class ZW_DMX_ADDRESS_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('channelId', uint8_t),
    ]


class ZW_DMX_ADDRESS_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_DMX_ADDRESS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('channelId', uint8_t),
    ]


class ZW_DMX_CAPABILITY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('channelId', uint8_t)]


class ZW_DMX_CAPABILITY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('channelId', uint8_t),
        ('propertyId1', uint8_t),
        ('propertyId2', uint8_t),
        ('deviceChannels', uint8_t),
        ('maxChannels', uint8_t),
    ]


class ZW_DMX_DATA_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('source', uint8_t),
        ('properties1', uint8_t),
        ('dmxChannel1', uint8_t),
    ]
