# Network Management Basic Node Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC = 0x4D


NETWORK_MANAGEMENT_BASIC_VERSION = 0x01
# Learn Mode Set
COMMAND_LEARN_MODE_SET = 0x01
# Learn Mode Set Status
COMMAND_LEARN_MODE_SET_STATUS = 0x02
# Network Update Request
COMMAND_NETWORK_UPDATE_REQUEST = 0x03
# Network Update Request Status
COMMAND_NETWORK_UPDATE_REQUEST_STATUS = 0x04
# Node Information Send
COMMAND_NODE_INFORMATION_SEND = 0x05
# Default Set
COMMAND_DEFAULT_SET = 0x06
# Default Set Complete
COMMAND_DEFAULT_SET_COMPLETE = 0x07



NETWORK_MANAGEMENT_BASIC_VERSION_V2 = 0x02
COMMAND_LEARN_MODE_SET_V2 = 0x01
COMMAND_LEARN_MODE_SET_STATUS_V2 = 0x02
COMMAND_NODE_INFORMATION_SEND_V2 = 0x05
COMMAND_NETWORK_UPDATE_REQUEST_V2 = 0x03
COMMAND_NETWORK_UPDATE_REQUEST_STATUS_V2 = 0x04
COMMAND_DEFAULT_SET_V2 = 0x06
COMMAND_DEFAULT_SET_COMPLETE_V2 = 0x07
# DSK Get
COMMAND_DSK_GET_V2 = 0x08
# DSK Report
COMMAND_DSK_REPORT_V2 = 0x09

# Values used for Learn Mode Set command
LEARN_MODE_SET_PROPERTIES1_RETURN_INTERVIEW_STATUS_BIT_MASK_V2 = 0x01
LEARN_MODE_SET_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
LEARN_MODE_SET_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01
# Values used for Dsk Get command
DSK_GET_PROPERTIES1_ADD_MODE_BIT_MASK_V2 = 0x01
DSK_GET_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
DSK_GET_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01
# Values used for Dsk Report command
DSK_REPORT_PROPERTIES1_ADD_MODE_BIT_MASK_V2 = 0x01
DSK_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
DSK_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01



class ZW_LEARN_MODE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('reserved', uint8_t),
        ('mode', uint8_t),
    ]


class ZW_LEARN_MODE_SET_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('reserved', uint8_t),
        ('newNodeId', uint8_t),
    ]


class ZW_NODE_INFORMATION_SEND_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('reserved', uint8_t),
        ('destinationNodeId', uint8_t),
        ('txOptions', uint8_t),
    ]






class ZW_NETWORK_UPDATE_REQUEST_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('seqNo', uint8_t)]


class ZW_NETWORK_UPDATE_REQUEST_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
    ]





class ZW_DEFAULT_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('seqNo', uint8_t)]


class ZW_DEFAULT_SET_COMPLETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
    ]





class ZW_LEARN_MODE_SET_V2_FRAME(ZW_LEARN_MODE_SET_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_LEARN_MODE_SET_STATUS_V2_FRAME(ZW_LEARN_MODE_SET_STATUS_FRAME):
    _fields_ = [
        ('grantedKeys', uint8_t),
        ('kexFailType', uint8_t),
        ('dsk1', uint8_t),
        ('dsk2', uint8_t),
        ('dsk3', uint8_t),
        ('dsk4', uint8_t),
        ('dsk5', uint8_t),
        ('dsk6', uint8_t),
        ('dsk7', uint8_t),
        ('dsk8', uint8_t),
        ('dsk9', uint8_t),
        ('dsk10', uint8_t),
        ('dsk11', uint8_t),
        ('dsk12', uint8_t),
        ('dsk13', uint8_t),
        ('dsk14', uint8_t),
        ('dsk15', uint8_t),
        ('dsk16', uint8_t),
    ]


class ZW_NODE_INFORMATION_SEND_V2_FRAME(ZW_NODE_INFORMATION_SEND_FRAME):
    _fields_ = []


class ZW_NETWORK_UPDATE_REQUEST_V2_FRAME(ZW_NETWORK_UPDATE_REQUEST_FRAME):
    _fields_ = []


class ZW_NETWORK_UPDATE_REQUEST_STATUS_V2_FRAME(ZW_NETWORK_UPDATE_REQUEST_STATUS_FRAME):
    _fields_ = []


class ZW_DEFAULT_SET_V2_FRAME(ZW_DEFAULT_SET_FRAME):
    _fields_ = []


class ZW_DEFAULT_SET_COMPLETE_V2_FRAME(ZW_DEFAULT_SET_COMPLETE_FRAME):
    _fields_ = []





class ZW_DSK_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
    ]


class ZW_DSK_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
        ('dsk2', uint8_t),
        ('dsk3', uint8_t),
        ('dsk4', uint8_t),
        ('dsk5', uint8_t),
        ('dsk6', uint8_t),
        ('dsk7', uint8_t),
        ('dsk8', uint8_t),
        ('dsk9', uint8_t),
        ('dsk10', uint8_t),
        ('dsk11', uint8_t),
        ('dsk12', uint8_t),
        ('dsk13', uint8_t),
        ('dsk14', uint8_t),
        ('dsk15', uint8_t),
        ('dsk16', uint8_t),
    ]

