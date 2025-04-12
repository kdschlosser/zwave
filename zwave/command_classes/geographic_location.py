# Geographic Location Command Class
# Application
# ==============================
COMMAND_CLASS_GEOGRAPHIC_LOCATION = 0x8C

GEOGRAPHIC_LOCATION_VERSION = 0x01
# Geographic Location Set
GEOGRAPHIC_LOCATION_SET = 0x01
# Geographic Location Get
GEOGRAPHIC_LOCATION_GET = 0x02
# Geographic Location Report
GEOGRAPHIC_LOCATION_REPORT = 0x03

# Values used for Geographic Location Report command
GEOGRAPHIC_LOCATION_REPORT_LEVEL_LONGITUDE_MINUTES_MASK = 0x7F
GEOGRAPHIC_LOCATION_REPORT_LEVEL_LONG_SIGN_BIT_MASK = 0x80
GEOGRAPHIC_LOCATION_REPORT_LEVEL2_LATITUDE_MINUTES_MASK = 0x7F
GEOGRAPHIC_LOCATION_REPORT_LEVEL2_LAT_SIGN_BIT_MASK = 0x80
# Values used for Geographic Location Set command
GEOGRAPHIC_LOCATION_SET_LEVEL_LONGITUDE_MINUTES_MASK = 0x7F
GEOGRAPHIC_LOCATION_SET_LEVEL_LONG_SIGN_BIT_MASK = 0x80
GEOGRAPHIC_LOCATION_SET_LEVEL2_LATITUDE_MINUTES_MASK = 0x7F
GEOGRAPHIC_LOCATION_SET_LEVEL2_LAT_SIGN_BIT_MASK = 0x80



class ZW_GEOGRAPHIC_LOCATION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_GEOGRAPHIC_LOCATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('longitudeDegrees', uint8_t),
        ('level', uint8_t),
        ('latitudeDegrees', uint8_t),
        ('level2', uint8_t),
    ]


class ZW_GEOGRAPHIC_LOCATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('longitudeDegrees', uint8_t),
        ('level', uint8_t),
        ('latitudeDegrees', uint8_t),
        ('level2', uint8_t),
    ]




