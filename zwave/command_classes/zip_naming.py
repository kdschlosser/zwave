# Z/IP Naming and Location Command Class
# Management
# ==============================
COMMAND_CLASS_ZIP_NAMING = 0x68

ZIP_NAMING_VERSION = 0x01
# Z/IP Name Set
ZIP_NAMING_NAME_SET = 0x01
# Z/IP Name Get
ZIP_NAMING_NAME_GET = 0x02
# Z/IP Name Report
ZIP_NAMING_NAME_REPORT = 0x03
# Z/IP Location Set
ZIP_NAMING_LOCATION_SET = 0x04
# Z/IP Location Get
ZIP_NAMING_LOCATION_GET = 0x05
# Z/IP Location Report
ZIP_NAMING_LOCATION_REPORT = 0x06


class ZW_ZIP_NAMING_NAME_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('name1', uint8_t)]


class ZW_ZIP_NAMING_NAME_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ZIP_NAMING_NAME_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('name1', uint8_t)]


class ZW_ZIP_NAMING_LOCATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('location1', uint8_t)]


class ZW_ZIP_NAMING_LOCATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ZIP_NAMING_LOCATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('location1', uint8_t)]


