# Network Management Inclusion Command Class
# Network-Protocol
# ==============================
COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION = 0x34

NETWORK_MANAGEMENT_INCLUSION_VERSION = 0x01
# Node Add
COMMAND_NODE_ADD = 0x01
# Node Add Status
COMMAND_NODE_ADD_STATUS = 0x02
# Node Remove
COMMAND_NODE_REMOVE = 0x03
# Node Remove Status
COMMAND_NODE_REMOVE_STATUS = 0x04
# Failed Node Remove
COMMAND_FAILED_NODE_REMOVE = 0x07
# Failed Node Remove Status
COMMAND_FAILED_NODE_REMOVE_STATUS = 0x08
# Failed Node Replace
COMMAND_FAILED_NODE_REPLACE = 0x09
# Failed Node Replace Status
COMMAND_FAILED_NODE_REPLACE_STATUS = 0x0A
# Node Neighbor Update Request
COMMAND_NODE_NEIGHBOR_UPDATE_REQUEST = 0x0B
# Node Neighbor Update Status
COMMAND_NODE_NEIGHBOR_UPDATE_STATUS = 0x0C
# Return Route Assign
COMMAND_RETURN_ROUTE_ASSIGN = 0x0D
# Return Route Assign Complete
COMMAND_RETURN_ROUTE_ASSIGN_COMPLETE = 0x0E
# Return Route Delete
COMMAND_RETURN_ROUTE_DELETE = 0x0F
# Return Route Delete Complete
COMMAND_RETURN_ROUTE_DELETE_COMPLETE = 0x10

# Values used for Node Add Status command
NODE_ADD_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK = 0x7F
NODE_ADD_STATUS_PROPERTIES1_LISTENING_BIT_MASK = 0x80
NODE_ADD_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK = 0x7F
NODE_ADD_STATUS_PROPERTIES2_OPT_BIT_MASK = 0x80

NETWORK_MANAGEMENT_INCLUSION_VERSION_V2 = 0x02
COMMAND_FAILED_NODE_REMOVE_V2 = 0x07
COMMAND_FAILED_NODE_REMOVE_STATUS_V2 = 0x08
COMMAND_NODE_ADD_V2 = 0x01
COMMAND_NODE_ADD_STATUS_V2 = 0x02
COMMAND_NODE_REMOVE_V2 = 0x03
COMMAND_NODE_REMOVE_STATUS_V2 = 0x04
COMMAND_FAILED_NODE_REPLACE_V2 = 0x09
COMMAND_FAILED_NODE_REPLACE_STATUS_V2 = 0x0A
COMMAND_NODE_NEIGHBOR_UPDATE_REQUEST_V2 = 0x0B
COMMAND_NODE_NEIGHBOR_UPDATE_STATUS_V2 = 0x0C
COMMAND_RETURN_ROUTE_ASSIGN_V2 = 0x0D
COMMAND_RETURN_ROUTE_ASSIGN_COMPLETE_V2 = 0x0E
COMMAND_RETURN_ROUTE_DELETE_V2 = 0x0F
COMMAND_RETURN_ROUTE_DELETE_COMPLETE_V2 = 0x10
# Node Add Keys Report
COMMAND_NODE_ADD_KEYS_REPORT_V2 = 0x11
# Node Add Keys Set
COMMAND_NODE_ADD_KEYS_SET_V2 = 0x12
# Node Add DSK Report
COMMAND_NODE_ADD_DSK_REPORT_V2 = 0x13
# Node Add DSK Set
COMMAND_NODE_ADD_DSK_SET_V2 = 0x14

# Values used for Node Add Status command
NODE_ADD_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK_V2 = 0x7F
NODE_ADD_STATUS_PROPERTIES1_LISTENING_BIT_MASK_V2 = 0x80
NODE_ADD_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK_V2 = 0x7F
NODE_ADD_STATUS_PROPERTIES2_OPT_BIT_MASK_V2 = 0x80
# Values used for Node Add Keys Report command
NODE_ADD_KEYS_REPORT_PROPERTIES1_REQUEST_CSA_BIT_MASK_V2 = 0x01
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01
# Values used for Node Add Keys Set command
NODE_ADD_KEYS_SET_PROPERTIES1_ACCEPT_BIT_MASK_V2 = 0x01
NODE_ADD_KEYS_SET_PROPERTIES1_GRANT_CSA_BIT_MASK_V2 = 0x02
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
# Values used for Node Add Dsk Report command
NODE_ADD_DSK_REPORT_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V2 = 0x0F
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xF0
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x04
# Values used for Node Add Dsk Set command
NODE_ADD_DSK_SET_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V2 = 0x0F
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_MASK_V2 = 0x70
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_SHIFT_V2 = 0x04
NODE_ADD_DSK_SET_PROPERTIES1_ACCEPT_BIT_MASK_V2 = 0x80

NETWORK_MANAGEMENT_INCLUSION_VERSION_V3 = 0x03
COMMAND_FAILED_NODE_REMOVE_V3 = 0x07
COMMAND_FAILED_NODE_REMOVE_STATUS_V3 = 0x08
COMMAND_NODE_ADD_V3 = 0x01
COMMAND_NODE_ADD_STATUS_V3 = 0x02
COMMAND_NODE_REMOVE_V3 = 0x03
COMMAND_NODE_REMOVE_STATUS_V3 = 0x04
COMMAND_FAILED_NODE_REPLACE_V3 = 0x09
COMMAND_FAILED_NODE_REPLACE_STATUS_V3 = 0x0A
COMMAND_NODE_NEIGHBOR_UPDATE_REQUEST_V3 = 0x0B
COMMAND_NODE_NEIGHBOR_UPDATE_STATUS_V3 = 0x0C
COMMAND_RETURN_ROUTE_ASSIGN_V3 = 0x0D
COMMAND_RETURN_ROUTE_ASSIGN_COMPLETE_V3 = 0x0E
COMMAND_RETURN_ROUTE_DELETE_V3 = 0x0F
COMMAND_RETURN_ROUTE_DELETE_COMPLETE_V3 = 0x10
COMMAND_NODE_ADD_KEYS_REPORT_V3 = 0x11
COMMAND_NODE_ADD_KEYS_SET_V3 = 0x12
COMMAND_NODE_ADD_DSK_REPORT_V3 = 0x13
COMMAND_NODE_ADD_DSK_SET_V3 = 0x14
# Included Node Information Frame Report
COMMAND_INCLUDED_NIF_REPORT_V3 = 0x19
# Smart Start Join Started
COMMAND_SMART_START_JOIN_STARTED_REPORT_V3 = 0x15

# Values used for Node Add Status command
NODE_ADD_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK_V3 = 0x7F
NODE_ADD_STATUS_PROPERTIES1_LISTENING_BIT_MASK_V3 = 0x80
NODE_ADD_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK_V3 = 0x7F
NODE_ADD_STATUS_PROPERTIES2_OPT_BIT_MASK_V3 = 0x80
NODE_ADD_STATUS_PROPERTIES3_DSK_LENGTH_MASK_V3 = 0x1F
NODE_ADD_STATUS_PROPERTIES3_RESERVED2_MASK_V3 = 0xE0
NODE_ADD_STATUS_PROPERTIES3_RESERVED2_SHIFT_V3 = 0x05
# Values used for Node Add Keys Report command
NODE_ADD_KEYS_REPORT_PROPERTIES1_REQUEST_CSA_BIT_MASK_V3 = 0x01
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0xFE
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x01
# Values used for Node Add Keys Set command
NODE_ADD_KEYS_SET_PROPERTIES1_ACCEPT_BIT_MASK_V3 = 0x01
NODE_ADD_KEYS_SET_PROPERTIES1_GRANT_CSA_BIT_MASK_V3 = 0x02
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_MASK_V3 = 0xFC
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_SHIFT_V3 = 0x02
# Values used for Node Add Dsk Report command
NODE_ADD_DSK_REPORT_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V3 = 0x0F
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0xF0
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x04
# Values used for Node Add Dsk Set command
NODE_ADD_DSK_SET_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V3 = 0x0F
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_MASK_V3 = 0x70
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_SHIFT_V3 = 0x04
NODE_ADD_DSK_SET_PROPERTIES1_ACCEPT_BIT_MASK_V3 = 0x80
# Values used for Smart Start Join Started Report command
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_DSK_LENGTH_MASK_V3 = 0x1F
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_RESERVED1_MASK_V3 = 0xE0
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_RESERVED1_SHIFT_V3 = 0x05
# Values used for Included Nif Report command
INCLUDED_NIF_REPORT_PROPERTIES1_DSK_LENGTH_MASK_V3 = 0x1F
INCLUDED_NIF_REPORT_PROPERTIES1_RESERVED1_MASK_V3 = 0xE0
INCLUDED_NIF_REPORT_PROPERTIES1_RESERVED1_SHIFT_V3 = 0x05

NETWORK_MANAGEMENT_INCLUSION_VERSION_V4 = 0x04
COMMAND_FAILED_NODE_REMOVE_V4 = 0x07
COMMAND_FAILED_NODE_REMOVE_STATUS_V4 = 0x08
COMMAND_NODE_ADD_V4 = 0x01
COMMAND_NODE_ADD_STATUS_V4 = 0x02
COMMAND_NODE_REMOVE_V4 = 0x03
COMMAND_NODE_REMOVE_STATUS_V4 = 0x04
COMMAND_FAILED_NODE_REPLACE_V4 = 0x09
COMMAND_FAILED_NODE_REPLACE_STATUS_V4 = 0x0A
COMMAND_NODE_NEIGHBOR_UPDATE_REQUEST_V4 = 0x0B
COMMAND_NODE_NEIGHBOR_UPDATE_STATUS_V4 = 0x0C
COMMAND_RETURN_ROUTE_ASSIGN_V4 = 0x0D
COMMAND_RETURN_ROUTE_ASSIGN_COMPLETE_V4 = 0x0E
COMMAND_RETURN_ROUTE_DELETE_V4 = 0x0F
COMMAND_RETURN_ROUTE_DELETE_COMPLETE_V4 = 0x10
COMMAND_NODE_ADD_KEYS_REPORT_V4 = 0x11
COMMAND_NODE_ADD_KEYS_SET_V4 = 0x12
COMMAND_NODE_ADD_DSK_REPORT_V4 = 0x13
COMMAND_NODE_ADD_DSK_SET_V4 = 0x14
COMMAND_SMART_START_JOIN_STARTED_REPORT_V4 = 0x15
COMMAND_INCLUDED_NIF_REPORT_V4 = 0x19
# Extended Node Add Status
COMMAND_EXTENDED_NODE_ADD_STATUS_V4 = 0x16

# Values used for Node Add Status command
NODE_ADD_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK_V4 = 0x7F
NODE_ADD_STATUS_PROPERTIES1_LISTENING_BIT_MASK_V4 = 0x80
NODE_ADD_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK_V4 = 0x7F
NODE_ADD_STATUS_PROPERTIES2_OPT_BIT_MASK_V4 = 0x80
NODE_ADD_STATUS_PROPERTIES3_DSK_LENGTH_MASK_V4 = 0x1F
NODE_ADD_STATUS_PROPERTIES3_RESERVED2_MASK_V4 = 0xE0
NODE_ADD_STATUS_PROPERTIES3_RESERVED2_SHIFT_V4 = 0x05
# Values used for Node Add Keys Report command
NODE_ADD_KEYS_REPORT_PROPERTIES1_REQUEST_CSA_BIT_MASK_V4 = 0x01
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_MASK_V4 = 0xFE
NODE_ADD_KEYS_REPORT_PROPERTIES1_RESERVED_SHIFT_V4 = 0x01
# Values used for Node Add Keys Set command
NODE_ADD_KEYS_SET_PROPERTIES1_ACCEPT_BIT_MASK_V4 = 0x01
NODE_ADD_KEYS_SET_PROPERTIES1_GRANT_CSA_BIT_MASK_V4 = 0x02
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_MASK_V4 = 0xFC
NODE_ADD_KEYS_SET_PROPERTIES1_RESERVED_SHIFT_V4 = 0x02
# Values used for Node Add Dsk Report command
NODE_ADD_DSK_REPORT_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V4 = 0x0F
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_MASK_V4 = 0xF0
NODE_ADD_DSK_REPORT_PROPERTIES1_RESERVED_SHIFT_V4 = 0x04
# Values used for Node Add Dsk Set command
NODE_ADD_DSK_SET_PROPERTIES1_INPUT_DSK_LENGTH_MASK_V4 = 0x0F
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_MASK_V4 = 0x70
NODE_ADD_DSK_SET_PROPERTIES1_RESERVED_SHIFT_V4 = 0x04
NODE_ADD_DSK_SET_PROPERTIES1_ACCEPT_BIT_MASK_V4 = 0x80
# Values used for Smart Start Join Started Report command
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_DSK_LENGTH_MASK_V4 = 0x1F
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_RESERVED1_MASK_V4 = 0xE0
SMART_START_JOIN_STARTED_REPORT_PROPERTIES1_RESERVED1_SHIFT_V4 = 0x05
# Values used for Included Nif Report command
INCLUDED_NIF_REPORT_PROPERTIES1_DSK_LENGTH_MASK_V4 = 0x1F
INCLUDED_NIF_REPORT_PROPERTIES1_RESERVED1_MASK_V4 = 0xE0
INCLUDED_NIF_REPORT_PROPERTIES1_RESERVED1_SHIFT_V4 = 0x05
# Values used for Extended Node Add Status command
EXTENDED_NODE_ADD_STATUS_PROPERTIES1_Z_WAVE_PROTOCOL_SPECIFIC_PART_1_MASK_V4 = 0x7F
EXTENDED_NODE_ADD_STATUS_PROPERTIES1_LISTENING_BIT_MASK_V4 = 0x80
EXTENDED_NODE_ADD_STATUS_PROPERTIES2_Z_WAVE_PROTOCOL_SPECIFIC_PART_2_MASK_V4 = 0x7F
EXTENDED_NODE_ADD_STATUS_PROPERTIES2_OPT_FUNC_BIT_MASK_V4 = 0x80


class ZW_FAILED_NODE_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_FAILED_NODE_REMOVE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_NODE_ADD_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('reserved', uint8_t),
        ('mode', uint8_t),
        ('txOptions', uint8_t),
    ]


class ZW_NODE_ADD_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('reserved', uint8_t),
        ('newNodeId', uint8_t),
        ('nodeInfoLength', uint8_t),
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('basicDeviceClass', uint8_t),
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
        ('commandClass1', uint8_t),
    ]


class ZW_NODE_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('reserved', uint8_t),
        ('mode', uint8_t),
    ]


class ZW_NODE_REMOVE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('nodeid', uint8_t),
    ]


class ZW_FAILED_NODE_REPLACE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('nodeId', uint8_t),
        ('txOptions', uint8_t),
        ('mode', uint8_t),
    ]


class ZW_FAILED_NODE_REPLACE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_NODE_NEIGHBOR_UPDATE_REQUEST_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_NODE_NEIGHBOR_UPDATE_STATUS_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
    ]


class ZW_RETURN_ROUTE_ASSIGN_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('sourceNodeId', uint8_t),
        ('destinationNodeId', uint8_t),
    ]


class ZW_RETURN_ROUTE_ASSIGN_COMPLETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
    ]


class ZW_RETURN_ROUTE_DELETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('nodeId', uint8_t),
    ]


class ZW_RETURN_ROUTE_DELETE_COMPLETE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
    ]


class ZW_FAILED_NODE_REMOVE_V2_FRAME(ZW_FAILED_NODE_REMOVE_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REMOVE_STATUS_V2_FRAME(ZW_FAILED_NODE_REMOVE_STATUS_FRAME):
    _fields_ = []


class ZW_NODE_ADD_V2_FRAME(ZW_NODE_ADD_FRAME):
    _fields_ = []


class ZW_NODE_ADD_STATUS_V2_FRAME(ZW_NODE_ADD_STATUS_FRAME):
    _fields_ = [
        ('grantedKeys', uint8_t),
        ('kexFailType', uint8_t),
    ]


class ZW_NODE_REMOVE_V2_FRAME(ZW_NODE_REMOVE_FRAME):
    _fields_ = []


class ZW_NODE_REMOVE_STATUS_V2_FRAME(ZW_NODE_REMOVE_STATUS_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REPLACE_V2_FRAME(ZW_FAILED_NODE_REPLACE_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REPLACE_STATUS_V2_FRAME(ZW_FAILED_NODE_REPLACE_STATUS_FRAME):
    _fields_ = [
        ('grantedKeys', uint8_t),
        ('kexFailType', uint8_t),
    ]


class ZW_NODE_NEIGHBOR_UPDATE_REQUEST_V2_FRAME(ZW_NODE_NEIGHBOR_UPDATE_REQUEST_FRAME):
    _fields_ = []


class ZW_NODE_NEIGHBOR_UPDATE_STATUS_V2_FRAME(ZW_NODE_NEIGHBOR_UPDATE_STATUS_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_V2_FRAME(ZW_RETURN_ROUTE_ASSIGN_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_COMPLETE_V2_FRAME(ZW_RETURN_ROUTE_ASSIGN_COMPLETE_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_V2_FRAME(ZW_RETURN_ROUTE_DELETE_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_COMPLETE_V2_FRAME(ZW_RETURN_ROUTE_DELETE_COMPLETE_FRAME):
    _fields_ = []


class ZW_NODE_ADD_KEYS_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('requestedKeys', uint8_t),
    ]


class ZW_NODE_ADD_KEYS_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('grantedKeys', uint8_t),
    ]


class ZW_NODE_ADD_DSK_REPORT_V2_FRAME(ZW_COMMON_FRAME):
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


class ZW_NODE_ADD_DSK_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('inputDsk1', uint8_t),
    ]


class ZW_FAILED_NODE_REMOVE_V3_FRAME(ZW_FAILED_NODE_REMOVE_V2_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REMOVE_STATUS_V3_FRAME(ZW_FAILED_NODE_REMOVE_STATUS_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_V3_FRAME(ZW_NODE_ADD_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_STATUS_V3_FRAME(ZW_NODE_ADD_STATUS_V2_FRAME):
    _fields_ = [
        ('reserved1', uint8_t),
        ('properties3', uint8_t),
        ('dsk1', uint8_t),
    ]


class ZW_NODE_REMOVE_V3_FRAME(ZW_NODE_REMOVE_V2_FRAME):
    _fields_ = []


class ZW_NODE_REMOVE_STATUS_V3_FRAME(ZW_NODE_REMOVE_STATUS_V2_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REPLACE_V3_FRAME(ZW_FAILED_NODE_REPLACE_V2_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REPLACE_STATUS_V3_FRAME(ZW_FAILED_NODE_REPLACE_STATUS_V2_FRAME):
    _fields_ = []


class ZW_NODE_NEIGHBOR_UPDATE_REQUEST_V3_FRAME(ZW_NODE_NEIGHBOR_UPDATE_REQUEST_V2_FRAME):
    _fields_ = []


class ZW_NODE_NEIGHBOR_UPDATE_STATUS_V3_FRAME(ZW_NODE_NEIGHBOR_UPDATE_STATUS_V2_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_V3_FRAME(ZW_RETURN_ROUTE_ASSIGN_V2_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_COMPLETE_V3_FRAME(ZW_RETURN_ROUTE_ASSIGN_COMPLETE_V2_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_V3_FRAME(ZW_RETURN_ROUTE_DELETE_V2_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_COMPLETE_V3_FRAME(ZW_RETURN_ROUTE_DELETE_COMPLETE_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_KEYS_REPORT_V3_FRAME(ZW_NODE_ADD_KEYS_REPORT_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_KEYS_SET_V3_FRAME(ZW_NODE_ADD_KEYS_SET_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_DSK_REPORT_V3_FRAME(ZW_NODE_ADD_DSK_REPORT_V2_FRAME):
    _fields_ = []


class ZW_NODE_ADD_DSK_SET_V3_FRAME(ZW_NODE_ADD_DSK_SET_V2_FRAME):
    _fields_ = []


class ZW_SMART_START_JOIN_STARTED_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
    ]


class ZW_INCLUDED_NIF_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('properties1', uint8_t),
        ('dsk1', uint8_t),
    ]


class ZW_FAILED_NODE_REMOVE_V4_FRAME(ZW_FAILED_NODE_REMOVE_V3_FRAME):
    _fields_ = [
        ('extendedNodeid1', uint8_t),
        ('extendedNodeid2', uint8_t),
    ]


class ZW_FAILED_NODE_REMOVE_STATUS_V4_FRAME(ZW_FAILED_NODE_REMOVE_STATUS_V3_FRAME):
    _fields_ = [
        ('extendedNodeid1', uint8_t),
        ('extendedNodeid2', uint8_t),
    ]


class ZW_NODE_ADD_V4_FRAME(ZW_NODE_ADD_V3_FRAME):
    _fields_ = []


class ZW_NODE_ADD_STATUS_V4_FRAME(ZW_NODE_ADD_STATUS_V3_FRAME):
    _fields_ = []


class ZW_NODE_REMOVE_V4_FRAME(ZW_NODE_REMOVE_V3_FRAME):
    _fields_ = []


class ZW_NODE_REMOVE_STATUS_V4_FRAME(ZW_NODE_REMOVE_STATUS_V3_FRAME):
    _fields_ = [
        ('extendedNodeid1', uint8_t),
        ('extendedNodeid2', uint8_t),
    ]


class ZW_FAILED_NODE_REPLACE_V4_FRAME(ZW_FAILED_NODE_REPLACE_V3_FRAME):
    _fields_ = []


class ZW_FAILED_NODE_REPLACE_STATUS_V4_FRAME(ZW_FAILED_NODE_REPLACE_STATUS_V3_FRAME):
    _fields_ = []


class ZW_NODE_NEIGHBOR_UPDATE_REQUEST_V4_FRAME(ZW_NODE_NEIGHBOR_UPDATE_REQUEST_V3_FRAME):
    _fields_ = []


class ZW_NODE_NEIGHBOR_UPDATE_STATUS_V4_FRAME(ZW_NODE_NEIGHBOR_UPDATE_STATUS_V3_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_V4_FRAME(ZW_RETURN_ROUTE_ASSIGN_V3_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_ASSIGN_COMPLETE_V4_FRAME(ZW_RETURN_ROUTE_ASSIGN_COMPLETE_V3_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_V4_FRAME(ZW_RETURN_ROUTE_DELETE_V3_FRAME):
    _fields_ = []


class ZW_RETURN_ROUTE_DELETE_COMPLETE_V4_FRAME(ZW_RETURN_ROUTE_DELETE_COMPLETE_V3_FRAME):
    _fields_ = []


class ZW_NODE_ADD_KEYS_REPORT_V4_FRAME(ZW_NODE_ADD_KEYS_REPORT_V3_FRAME):
    _fields_ = []


class ZW_NODE_ADD_KEYS_SET_V4_FRAME(ZW_NODE_ADD_KEYS_SET_V3_FRAME):
    _fields_ = []


class ZW_NODE_ADD_DSK_REPORT_V4_FRAME(ZW_NODE_ADD_DSK_REPORT_V3_FRAME):
    _fields_ = []


class ZW_NODE_ADD_DSK_SET_V4_FRAME(ZW_NODE_ADD_DSK_SET_V3_FRAME):
    _fields_ = []


class ZW_SMART_START_JOIN_STARTED_REPORT_V4_FRAME(ZW_SMART_START_JOIN_STARTED_REPORT_V3_FRAME):
    _fields_ = []


class ZW_INCLUDED_NIF_REPORT_V4_FRAME(ZW_INCLUDED_NIF_REPORT_V3_FRAME):
    _fields_ = []


class ZW_EXTENDED_NODE_ADD_STATUS_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('seqNo', uint8_t),
        ('status', uint8_t),
        ('assignedNodeid1', uint8_t),
        ('assignedNodeid2', uint8_t),
        ('nodeInfoLength', uint8_t),
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('basicDeviceClass', uint8_t),
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
        ('commandClass1', uint8_t),
        ('grantedKeys', uint8_t),
        ('kexFailType', uint8_t),
    ]

