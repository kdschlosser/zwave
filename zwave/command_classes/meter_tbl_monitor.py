# Meter Table Monitor Command Class
# Application
# ==============================
COMMAND_CLASS_METER_TBL_MONITOR = 0x3D

METER_TBL_MONITOR_VERSION = 0x01
# Meter Table Point Adm Number Get
METER_TBL_TABLE_POINT_ADM_NO_GET = 0x01
# Meter Table Point Adm Number Report
METER_TBL_TABLE_POINT_ADM_NO_REPORT = 0x02
# Meter Table ID Get
METER_TBL_TABLE_ID_GET = 0x03
# Meter Table ID Report
METER_TBL_TABLE_ID_REPORT = 0x04
# Meter Table Capability Get
METER_TBL_TABLE_CAPABILITY_GET = 0x05
# Meter Table Capability Report
METER_TBL_TABLE_CAPABILITY_REPORT = 0x06
# Meter Table Status Supported Get
METER_TBL_STATUS_SUPPORTED_GET = 0x07
# Meter Table Status Supported Report
METER_TBL_STATUS_SUPPORTED_REPORT = 0x08
# Meter Table Status Depth Get
METER_TBL_STATUS_DEPTH_GET = 0x09
# Meter Table Status Date Get
METER_TBL_STATUS_DATE_GET = 0x0A
# Meter Table Status Report
METER_TBL_STATUS_REPORT = 0x0B
# Meter Table Current Data Get
METER_TBL_CURRENT_DATA_GET = 0x0C
# Meter Table Current Data Report
METER_TBL_CURRENT_DATA_REPORT = 0x0D
# Meter Table Historical Data Get
METER_TBL_HISTORICAL_DATA_GET = 0x0E
# Meter Table Historical Data Report
METER_TBL_HISTORICAL_DATA_REPORT = 0x0F

# Values used for Meter Tbl Current Data Report command
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK = 0x03
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Meter Tbl Historical Data Report command
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK = 0x03
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Meter Tbl Table Capability Report command
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_METER_TYPE_MASK = 0x3F
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_MASK = 0xC0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_SHIFT = 0x06
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_PAY_METER_MASK = 0x0F
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_RESERVED = 0x00
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_CREDITMETER = 0x01
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER = 0x02
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER_DEBT = 0x03
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_MASK = 0xF0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_SHIFT = 0x04
# Values used for Meter Tbl Table Id Report command
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK = 0x1F
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05
# Values used for Meter Tbl Table Point Adm No Report command
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK = 0x1F
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_MASK = 0xE0
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x05

METER_TBL_MONITOR_VERSION_V2 = 0x02
METER_TBL_STATUS_REPORT_V2 = 0x0B
METER_TBL_STATUS_DATE_GET_V2 = 0x0A
METER_TBL_STATUS_DEPTH_GET_V2 = 0x09
METER_TBL_STATUS_SUPPORTED_GET_V2 = 0x07
METER_TBL_STATUS_SUPPORTED_REPORT_V2 = 0x08
METER_TBL_CURRENT_DATA_GET_V2 = 0x0C
METER_TBL_CURRENT_DATA_REPORT_V2 = 0x0D
METER_TBL_HISTORICAL_DATA_GET_V2 = 0x0E
METER_TBL_HISTORICAL_DATA_REPORT_V2 = 0x0F
METER_TBL_TABLE_CAPABILITY_REPORT_V2 = 0x06
METER_TBL_TABLE_CAPABILITY_GET_V2 = 0x05
METER_TBL_TABLE_ID_GET_V2 = 0x03
METER_TBL_TABLE_ID_REPORT_V2 = 0x04
METER_TBL_TABLE_POINT_ADM_NO_GET_V2 = 0x01
METER_TBL_TABLE_POINT_ADM_NO_REPORT_V2 = 0x02
# Values used for Meter Tbl Current Data Report command
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK_V2 = 0x03
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0x7C
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_OPERATING_STATUS_INDICATION_BIT_MASK_V2 = 0x80
# Values used for Meter Tbl Historical Data Report command
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK_V2 = 0x03
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0x7C
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_OPERATING_STATUS_INDICATION_BIT_MASK_V2 = 0x80
# Values used for Meter Tbl Table Capability Report command
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_METER_TYPE_MASK_V2 = 0x3F
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_MASK_V2 = 0xC0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_SHIFT_V2 = 0x06
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_PAY_METER_MASK_V2 = 0x0F
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_RESERVED_V2 = 0x00
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_CREDITMETER_V2 = 0x01
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER_V2 = 0x02
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER_DEBT_V2 = 0x03
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_MASK_V2 = 0xF0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_SHIFT_V2 = 0x04
# Values used for Meter Tbl Table Id Report command
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK_V2 = 0x1F
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xE0
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x05
# Values used for Meter Tbl Table Point Adm No Report command
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK_V2 = 0x1F
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xE0
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x05

METER_TBL_MONITOR_VERSION_V3 = 0x03
METER_TBL_STATUS_REPORT_V3 = 0x0B
METER_TBL_STATUS_DATE_GET_V3 = 0x0A
METER_TBL_STATUS_DEPTH_GET_V3 = 0x09
METER_TBL_STATUS_SUPPORTED_GET_V3 = 0x07
METER_TBL_STATUS_SUPPORTED_REPORT_V3 = 0x08
METER_TBL_CURRENT_DATA_GET_V3 = 0x0C
METER_TBL_CURRENT_DATA_REPORT_V3 = 0x0D
METER_TBL_HISTORICAL_DATA_GET_V3 = 0x0E
METER_TBL_HISTORICAL_DATA_REPORT_V3 = 0x0F
METER_TBL_TABLE_CAPABILITY_REPORT_V3 = 0x06
METER_TBL_TABLE_CAPABILITY_GET_V3 = 0x05
METER_TBL_TABLE_ID_GET_V3 = 0x03
METER_TBL_TABLE_ID_REPORT_V3 = 0x04
METER_TBL_TABLE_POINT_ADM_NO_GET_V3 = 0x01
METER_TBL_TABLE_POINT_ADM_NO_REPORT_V3 = 0x02
# Values used for Meter Tbl Current Data Report command
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK_V3 = 0x03
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0x7C
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x02
METER_TBL_CURRENT_DATA_REPORT_PROPERTIES1_OPERATING_STATUS_INDICATION_BIT_MASK_V3 = 0x80
# Values used for Meter Tbl Historical Data Report command
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RATE_TYPE_MASK_V3 = 0x03
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0x7C
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x02
METER_TBL_HISTORICAL_DATA_REPORT_PROPERTIES1_OPERATING_STATUS_INDICATION_BIT_MASK_V3 = 0x80
# Values used for Meter Tbl Table Capability Report command
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_METER_TYPE_MASK_V3 = 0x3F
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_MASK_V3 = 0xC0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES1_RATE_TYPE_SHIFT_V3 = 0x06
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_PAY_METER_MASK_V3 = 0x0F
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_RESERVED_V3 = 0x00
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_CREDITMETER_V3 = 0x01
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER_V3 = 0x02
METER_TBL_TABLE_CAPABILITY_REPORT_PAY_METER_PREPAYMENT_METER_DEBT_V3 = 0x03
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_MASK_V3 = 0xF0
METER_TBL_TABLE_CAPABILITY_REPORT_PROPERTIES2_RESERVED_SHIFT_V3 = 0x04
# Values used for Meter Tbl Table Id Report command
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK_V3 = 0x1F
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0xE0
METER_TBL_TABLE_ID_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x05
# Values used for Meter Tbl Table Point Adm No Report command
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK_V3 = 0x1F
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_MASK_V3 = 0xE0
METER_TBL_TABLE_POINT_ADM_NO_REPORT_PROPERTIES1_RESERVED_SHIFT_V3 = 0x05


class VG_METER_TBL_STATUS_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
    ]


class ZW_METER_TBL_STATUS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('currentOperatingStatus1', uint8_t),
        ('currentOperatingStatus2', uint8_t),
        ('currentOperatingStatus3', uint8_t),
        ('variantgroup1', VG_METER_TBL_STATUS_REPORT_VG),
    ]


class ZW_METER_TBL_STATUS_DATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('maximumReports', uint8_t),
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


class ZW_METER_TBL_STATUS_DEPTH_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('statusEventLogDepth', uint8_t)]


class ZW_METER_TBL_STATUS_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('supportedOperatingStatus1', uint8_t),
        ('supportedOperatingStatus2', uint8_t),
        ('supportedOperatingStatus3', uint8_t),
        ('statusEventLogDepth', uint8_t),
    ]


class ZW_METER_TBL_CURRENT_DATA_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('datasetRequested1', uint8_t),
        ('datasetRequested2', uint8_t),
        ('datasetRequested3', uint8_t),
    ]


class VG_METER_TBL_CURRENT_DATA_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('currentValue1', uint8_t),
        ('currentValue2', uint8_t),
        ('currentValue3', uint8_t),
        ('currentValue4', uint8_t),
    ]


class ZW_METER_TBL_CURRENT_DATA_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('properties1', uint8_t),
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
        ('variantgroup1', VG_METER_TBL_CURRENT_DATA_REPORT_VG),
    ]


class ZW_METER_TBL_HISTORICAL_DATA_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('maximumReports', uint8_t),
        ('historicalDatasetRequested1', uint8_t),
        ('historicalDatasetRequested2', uint8_t),
        ('historicalDatasetRequested3', uint8_t),
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


class VG_METER_TBL_HISTORICAL_DATA_REPORT_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('historicalValue1', uint8_t),
        ('historicalValue2', uint8_t),
        ('historicalValue3', uint8_t),
        ('historicalValue4', uint8_t),
    ]


class ZW_METER_TBL_HISTORICAL_DATA_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('properties1', uint8_t),
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
        ('variantgroup1', VG_METER_TBL_HISTORICAL_DATA_REPORT_VG),
    ]


class ZW_METER_TBL_TABLE_CAPABILITY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('datasetSupported1', uint8_t),
        ('datasetSupported2', uint8_t),
        ('datasetSupported3', uint8_t),
        ('datasetHistorySupported1', uint8_t),
        ('datasetHistorySupported2', uint8_t),
        ('datasetHistorySupported3', uint8_t),
        ('dataHistorySupported1', uint8_t),
        ('dataHistorySupported2', uint8_t),
        ('dataHistorySupported3', uint8_t),
    ]


class ZW_METER_TBL_TABLE_CAPABILITY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('meterIdCharacter1', uint8_t),
    ]


class ZW_METER_TBL_TABLE_POINT_ADM_NO_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_POINT_ADM_NO_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('meterPointAdmNumberCharacter1', uint8_t),
    ]


class VG_METER_TBL_STATUS_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
    ]


class ZW_METER_TBL_STATUS_REPORT_V2_FRAME(ZW_METER_TBL_STATUS_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_DATE_GET_V2_FRAME(ZW_METER_TBL_STATUS_DATE_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_DEPTH_GET_V2_FRAME(ZW_METER_TBL_STATUS_DEPTH_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_SUPPORTED_GET_V2_FRAME(ZW_METER_TBL_STATUS_SUPPORTED_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_SUPPORTED_REPORT_V2_FRAME(ZW_METER_TBL_STATUS_SUPPORTED_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_CURRENT_DATA_GET_V2_FRAME(ZW_METER_TBL_CURRENT_DATA_GET_FRAME):
    _fields_ = []


class VG_METER_TBL_CURRENT_DATA_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('currentValue1', uint8_t),
        ('currentValue2', uint8_t),
        ('currentValue3', uint8_t),
        ('currentValue4', uint8_t),
    ]


class ZW_METER_TBL_CURRENT_DATA_REPORT_V2_FRAME(ZW_METER_TBL_CURRENT_DATA_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_HISTORICAL_DATA_GET_V2_FRAME(ZW_METER_TBL_HISTORICAL_DATA_GET_FRAME):
    _fields_ = []


class VG_METER_TBL_HISTORICAL_DATA_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('historicalValue1', uint8_t),
        ('historicalValue2', uint8_t),
        ('historicalValue3', uint8_t),
        ('historicalValue4', uint8_t),
    ]


class ZW_METER_TBL_HISTORICAL_DATA_REPORT_V2_FRAME(ZW_METER_TBL_HISTORICAL_DATA_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_CAPABILITY_REPORT_V2_FRAME(ZW_METER_TBL_TABLE_CAPABILITY_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_CAPABILITY_GET_V2_FRAME(ZW_METER_TBL_TABLE_CAPABILITY_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_GET_V2_FRAME(ZW_METER_TBL_TABLE_ID_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_REPORT_V2_FRAME(ZW_METER_TBL_TABLE_ID_REPORT_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_POINT_ADM_NO_GET_V2_FRAME(ZW_METER_TBL_TABLE_POINT_ADM_NO_GET_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_POINT_ADM_NO_REPORT_V2_FRAME(ZW_METER_TBL_TABLE_POINT_ADM_NO_REPORT_FRAME):
    _fields_ = []


class VG_METER_TBL_STATUS_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
    ]


class ZW_METER_TBL_STATUS_REPORT_V3_FRAME(ZW_METER_TBL_STATUS_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_DATE_GET_V3_FRAME(ZW_METER_TBL_STATUS_DATE_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_DEPTH_GET_V3_FRAME(ZW_METER_TBL_STATUS_DEPTH_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_SUPPORTED_GET_V3_FRAME(ZW_METER_TBL_STATUS_SUPPORTED_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_STATUS_SUPPORTED_REPORT_V3_FRAME(ZW_METER_TBL_STATUS_SUPPORTED_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_CURRENT_DATA_GET_V3_FRAME(ZW_METER_TBL_CURRENT_DATA_GET_V2_FRAME):
    _fields_ = []


class VG_METER_TBL_CURRENT_DATA_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('currentValue1', uint8_t),
        ('currentValue2', uint8_t),
        ('currentValue3', uint8_t),
        ('currentValue4', uint8_t),
    ]


class ZW_METER_TBL_CURRENT_DATA_REPORT_V3_FRAME(ZW_METER_TBL_CURRENT_DATA_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_HISTORICAL_DATA_GET_V3_FRAME(ZW_METER_TBL_HISTORICAL_DATA_GET_V2_FRAME):
    _fields_ = []


class VG_METER_TBL_HISTORICAL_DATA_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('properties1', uint8_t),
        ('historicalValue1', uint8_t),
        ('historicalValue2', uint8_t),
        ('historicalValue3', uint8_t),
        ('historicalValue4', uint8_t),
    ]


class ZW_METER_TBL_HISTORICAL_DATA_REPORT_V3_FRAME(ZW_METER_TBL_HISTORICAL_DATA_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_CAPABILITY_REPORT_V3_FRAME(ZW_METER_TBL_TABLE_CAPABILITY_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_CAPABILITY_GET_V3_FRAME(ZW_METER_TBL_TABLE_CAPABILITY_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_GET_V3_FRAME(ZW_METER_TBL_TABLE_ID_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_ID_REPORT_V3_FRAME(ZW_METER_TBL_TABLE_ID_REPORT_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_POINT_ADM_NO_GET_V3_FRAME(ZW_METER_TBL_TABLE_POINT_ADM_NO_GET_V2_FRAME):
    _fields_ = []


class ZW_METER_TBL_TABLE_POINT_ADM_NO_REPORT_V3_FRAME(ZW_METER_TBL_TABLE_POINT_ADM_NO_REPORT_V2_FRAME):
    _fields_ = []
