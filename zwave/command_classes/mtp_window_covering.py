# Move To Position Window Covering Command Class
# Application
# ==============================
COMMAND_CLASS_MTP_WINDOW_COVERING = 0x51

MTP_WINDOW_COVERING_VERSION = 0x01
# Move To Position Set
MOVE_TO_POSITION_SET = 0x01
# Move To Position Get
MOVE_TO_POSITION_GET = 0x02
# Move To Position Report
MOVE_TO_POSITION_REPORT = 0x03





class ZW_MOVE_TO_POSITION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_MOVE_TO_POSITION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


class ZW_MOVE_TO_POSITION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('value', uint8_t)]


