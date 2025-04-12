# Language Command Class
# Application
# ==============================
COMMAND_CLASS_LANGUAGE = 0x89

LANGUAGE_VERSION = 0x01
# Language Set
LANGUAGE_SET = 0x01
# Language Get
LANGUAGE_GET = 0x02
# Language Report
LANGUAGE_REPORT = 0x03





class ZW_LANGUAGE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_LANGUAGE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('language1', uint8_t),
        ('language2', uint8_t),
        ('language3', uint8_t),
        ('country1', uint8_t),
        ('country2', uint8_t),
    ]


class ZW_LANGUAGE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('language1', uint8_t),
        ('language2', uint8_t),
        ('language3', uint8_t),
        ('country1', uint8_t),
        ('country2', uint8_t),
    ]



