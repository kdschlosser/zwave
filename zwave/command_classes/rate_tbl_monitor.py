# Rate Table Monitor Command Class
# Application
# ==============================
COMMAND_CLASS_RATE_TBL_MONITOR = 0x49

RATE_TBL_MONITOR_VERSION = 0x01
# Rate Table Supported Get
RATE_TBL_SUPPORTED_GET = 0x01
# Rate Table Supported Report
RATE_TBL_SUPPORTED_REPORT = 0x02
# Rate Table Get
RATE_TBL_GET = 0x03
# Rate Table Report
RATE_TBL_REPORT = 0x04
# Rate Table Active Rate Get
RATE_TBL_ACTIVE_RATE_GET = 0x05
# Rate Table Active Rate Report
RATE_TBL_ACTIVE_RATE_REPORT = 0x06
# Rate Table Current Data Get
RATE_TBL_CURRENT_DATA_GET = 0x07
# Rate Table Current Data Report
RATE_TBL_CURRENT_DATA_REPORT = 0x08
# Rate Table Historical Data Get
RATE_TBL_HISTORICAL_DATA_GET = 0x09
# Rate Table Historical Data Report
RATE_TBL_HISTORICAL_DATA_REPORT = 0x0A

# Values used for Rate Tbl Report command
RATE_TBL_REPORT_PROPERTIES1_NUMBER_OF_RATE_CHAR_MASK = 0x1F
RATE_TBL_REPORT_PROPERTIES1_RATE_TYPE_MASK = 0x60
RATE_TBL_REPORT_PROPERTIES1_RATE_TYPE_SHIFT = 0x05
RATE_TBL_REPORT_PROPERTIES1_RESERVED_BIT_MASK = 0x80
RATE_TBL_REPORT_PROPERTIES2_CONSUMPTION_SCALE_MASK = 0x1F
RATE_TBL_REPORT_PROPERTIES2_CONSUMPTION_PRECISION_MASK = 0xE0
RATE_TBL_REPORT_PROPERTIES2_CONSUMPTION_PRECISION_SHIFT = 0x05
RATE_TBL_REPORT_PROPERTIES3_MAX_DEMAND_SCALE_MASK = 0x1F
RATE_TBL_REPORT_PROPERTIES3_MAX_DEMAND_PRECISION_MASK = 0xE0
RATE_TBL_REPORT_PROPERTIES3_MAX_DEMAND_PRECISION_SHIFT = 0x05


class ZW_RATE_TBL_ACTIVE_RATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_RATE_TBL_ACTIVE_RATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('rateParameterSetId', uint8_t)]


class ZW_RATE_TBL_CURRENT_DATA_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('datasetRequested1', uint8_t),
        ('datasetRequested2', uint8_t),
        ('datasetRequested3', uint8_t),
    ]


class VG_RATE_TBL_CURRENT_DATA_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('currentValue1', uint8_t),
        ('currentValue2', uint8_t),
        ('currentValue3', uint8_t),
        ('currentValue4', uint8_t),
    ]


class ZW_RATE_TBL_CURRENT_DATA_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('rateParameterSetId', uint8_t),
        ('dataset1', uint8_t),
        ('dataset2', uint8_t),
        ('dataset3', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
        ('variantgroup1', VG_RATE_TBL_CURRENT_DATA_REPORT_VG),
    ]


class ZW_RATE_TBL_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('rateParameterSetId', uint8_t)]


class ZW_RATE_TBL_HISTORICAL_DATA_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('maximumReports', uint8_t),
        ('rateParameterSetId', uint8_t),
        ('datasetRequested1', uint8_t),
        ('datasetRequested2', uint8_t),
        ('datasetRequested3', uint8_t),
        ('startYear1', uint8_t),
        ('startYear2', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHourLocalTime', uint8_t),
        ('startMinuteLocalTime', uint8_t),
        ('startSecondLocalTime', uint8_t),
        ('stopYear1', uint8_t),
        ('stopYear2', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHourLocalTime', uint8_t),
        ('stopMinuteLocalTime', uint8_t),
        ('stopSecondLocalTime', uint8_t),
    ]


class VG_RATE_TBL_HISTORICAL_DATA_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('historicalValue1', uint8_t),
        ('historicalValue2', uint8_t),
        ('historicalValue3', uint8_t),
        ('historicalValue4', uint8_t),
    ]


class ZW_RATE_TBL_HISTORICAL_DATA_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('rateParameterSetId', uint8_t),
        ('dataset1', uint8_t),
        ('dataset2', uint8_t),
        ('dataset3', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
        ('variantgroup1', VG_RATE_TBL_HISTORICAL_DATA_REPORT_VG),
    ]


class ZW_RATE_TBL_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('properties1', uint8_t),
        ('rateCharacter1', uint8_t),
        ('startHourLocalTime', uint8_t),
        ('startMinuteLocalTime', uint8_t),
        ('durationMinute1', uint8_t),
        ('durationMinute2', uint8_t),
        ('properties2', uint8_t),
        ('minConsumptionValue1', uint8_t),
        ('minConsumptionValue2', uint8_t),
        ('minConsumptionValue3', uint8_t),
        ('minConsumptionValue4', uint8_t),
        ('maxConsumptionValue1', uint8_t),
        ('maxConsumptionValue2', uint8_t),
        ('maxConsumptionValue3', uint8_t),
        ('maxConsumptionValue4', uint8_t),
        ('properties3', uint8_t),
        ('maxDemandValue1', uint8_t),
        ('maxDemandValue2', uint8_t),
        ('maxDemandValue3', uint8_t),
        ('maxDemandValue4', uint8_t),
        ('dcpRateId', uint8_t),
    ]


class ZW_RATE_TBL_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_RATE_TBL_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('ratesSupported', uint8_t),
        ('parameterSetSupportedBitMask1', uint8_t),
        ('parameterSetSupportedBitMask2', uint8_t),
    ]

