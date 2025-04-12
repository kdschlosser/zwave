# Proprietary Command Class
# Application
# ==============================
COMMAND_CLASS_PROPRIETARY = 0x88

PROPRIETARY_VERSION = 0x01
# Proprietary Set
PROPRIETARY_SET = 0x01
# Proprietary Get
PROPRIETARY_GET = 0x02
# Proprietary Report
PROPRIETARY_REPORT = 0x03

class ZW_PROPRIETARY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('data1', uint8_t)]


class ZW_PROPRIETARY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('data1', uint8_t)]


class ZW_PROPRIETARY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('data1', uint8_t)]
