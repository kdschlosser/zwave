# Supervision Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_SUPERVISION = 0x6C

SUPERVISION_VERSION = 0x01
# Supervision Get
SUPERVISION_GET = 0x01
# Supervision Report
SUPERVISION_REPORT = 0x02

# Values used for Supervision Get command
SUPERVISION_GET_PROPERTIES1_SESSION_ID_MASK = 0x3F
SUPERVISION_GET_PROPERTIES1_RESERVED_BIT_MASK = 0x40
SUPERVISION_GET_PROPERTIES1_STATUS_UPDATES_BIT_MASK = 0x80
# Values used for Supervision Report command
SUPERVISION_REPORT_PROPERTIES1_SESSION_ID_MASK = 0x3F
SUPERVISION_REPORT_PROPERTIES1_RESERVED_BIT_MASK = 0x40
SUPERVISION_REPORT_PROPERTIES1_MORE_STATUS_UPDATES_BIT_MASK = 0x80
SUPERVISION_REPORT_NO_SUPPORT = 0x00
SUPERVISION_REPORT_WORKING = 0x01
SUPERVISION_REPORT_FAIL = 0x02
SUPERVISION_REPORT_BUSY = 0x03
SUPERVISION_REPORT_SUCCESS = 0xFF

SUPERVISION_VERSION_V2 = 0x02
SUPERVISION_GET_V2 = 0x01
SUPERVISION_REPORT_V2 = 0x02
# Values used for Supervision Get command
SUPERVISION_GET_PROPERTIES1_SESSION_ID_MASK_V2 = 0x3F
SUPERVISION_GET_PROPERTIES1_RESERVED_BIT_MASK_V2 = 0x40
SUPERVISION_GET_PROPERTIES1_STATUS_UPDATES_BIT_MASK_V2 = 0x80
# Values used for Supervision Report command
SUPERVISION_REPORT_PROPERTIES1_SESSION_ID_MASK_V2 = 0x3F
SUPERVISION_REPORT_PROPERTIES1_WAKE_UP_REQUEST_BIT_MASK_V2 = 0x40
SUPERVISION_REPORT_PROPERTIES1_MORE_STATUS_UPDATES_BIT_MASK_V2 = 0x80
SUPERVISION_REPORT_NO_SUPPORT_V2 = 0x00
SUPERVISION_REPORT_WORKING_V2 = 0x01
SUPERVISION_REPORT_FAIL_V2 = 0x02
SUPERVISION_REPORT_BUSY_V2 = 0x03
SUPERVISION_REPORT_SUCCESS_V2 = 0xFF

class ZW_SUPERVISION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('encapsulatedCommandLength', uint8_t),
    ]


class ZW_SUPERVISION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('status', uint8_t),
        ('duration', uint8_t),
    ]


class ZW_SUPERVISION_GET_V2_FRAME(ZW_SUPERVISION_GET_FRAME):
    _fields_ = []


class ZW_SUPERVISION_REPORT_V2_FRAME(ZW_SUPERVISION_REPORT_FRAME):
    _fields_ = []

