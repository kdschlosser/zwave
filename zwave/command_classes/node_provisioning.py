# Node Provisioning Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_NODE_PROVISIONING = 0x78

NODE_PROVISIONING_VERSION = 0x01
# Node Provisioning Set
COMMAND_NODE_PROVISIONING_SET = 0x01
# Node Provisioning Delete
COMMAND_NODE_PROVISIONING_DELETE = 0x02
# Node Provisioning Get
COMMAND_NODE_PROVISIONING_GET = 0x05
# Node Provisioning Report
COMMAND_NODE_PROVISIONING_REPORT = 0x06
# Node Provisioning List Iteration Get
COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET = 0x03
# Node Provisioning List Iteration Report
COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT = 0x04

# Values used for Node Provisioning Set command
NODE_PROVISIONING_SET_PROPERTIES1_DSK_LENGTH_MASK = 0x1F
NODE_PROVISIONING_SET_PROPERTIES1_RESERVED1_MASK = 0xE0
NODE_PROVISIONING_SET_PROPERTIES1_RESERVED1_SHIFT = 0x05
# Values used for Node Provisioning Delete command
NODE_PROVISIONING_DELETE_PROPERTIES1_DSK_LENGTH_MASK = 0x1F
NODE_PROVISIONING_DELETE_PROPERTIES1_RESERVED1_MASK = 0xE0
NODE_PROVISIONING_DELETE_PROPERTIES1_RESERVED1_SHIFT = 0x05
# Values used for Node Provisioning List Iteration Report command
NODE_PROVISIONING_LIST_ITERATION_REPORT_PROPERTIES1_DSK_LENGTH_MASK = 0x1F
NODE_PROVISIONING_LIST_ITERATION_REPORT_PROPERTIES1_RESERVED1_MASK = 0xE0
NODE_PROVISIONING_LIST_ITERATION_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x05
# Values used for Node Provisioning Get command
NODE_PROVISIONING_GET_PROPERTIES1_DSK_LENGTH_MASK = 0x1F
NODE_PROVISIONING_GET_PROPERTIES1_RESERVED1_MASK = 0xE0
NODE_PROVISIONING_GET_PROPERTIES1_RESERVED1_SHIFT = 0x05
# Values used for Node Provisioning Report command
NODE_PROVISIONING_REPORT_PROPERTIES1_DSK_LENGTH_MASK = 0x1F
NODE_PROVISIONING_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
NODE_PROVISIONING_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05

class ZW_NODE_PROVISIONING_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
        ('variantgroup1', VG_NODE_PROVISIONING_SET_VG),
    ]


class ZW_NODE_PROVISIONING_DELETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
    ]


class ZW_NODE_PROVISIONING_LIST_ITERATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('remainingCounter', uint8_t),
    ]


class ZW_NODE_PROVISIONING_LIST_ITERATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('remainingCount', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
        ('variantgroup1', VG_NODE_PROVISIONING_LIST_ITERATION_REPORT_VG),
    ]


class ZW_NODE_PROVISIONING_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
    ]


class ZW_NODE_PROVISIONING_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
        ('variantgroup1', VG_NODE_PROVISIONING_REPORT_VG),
    ]

