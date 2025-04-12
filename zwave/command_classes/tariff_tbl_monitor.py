# Tariff Table Monitor Command Class
# Application
# ==============================
COMMAND_CLASS_TARIFF_TBL_MONITOR = 0x4B

TARIFF_TBL_MONITOR_VERSION = 0x01
# Tariff Table Supplier Get
TARIFF_TBL_SUPPLIER_GET = 0x01
# Tariff Table Supplier Report
TARIFF_TBL_SUPPLIER_REPORT = 0x02
# Tariff Table Get
TARIFF_TBL_GET = 0x03
# Tariff Table Report
TARIFF_TBL_REPORT = 0x04
# Tariff Table Cost Get
TARIFF_TBL_COST_GET = 0x05
# Tariff Table Cost Report
TARIFF_TBL_COST_REPORT = 0x06

# Values used for Tariff Tbl Cost Report command
TARIFF_TBL_COST_REPORT_PROPERTIES1_RATE_TYPE_MASK = 0x03
TARIFF_TBL_COST_REPORT_PROPERTIES1_RESERVED1_MASK = 0xFC
TARIFF_TBL_COST_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x02
TARIFF_TBL_COST_REPORT_PROPERTIES2_RESERVED2_MASK = 0x1F
TARIFF_TBL_COST_REPORT_PROPERTIES2_COST_PRECISION_MASK = 0xE0
TARIFF_TBL_COST_REPORT_PROPERTIES2_COST_PRECISION_SHIFT = 0x05
# Values used for Tariff Tbl Report command
TARIFF_TBL_REPORT_PROPERTIES1_RESERVED_MASK = 0x1F
TARIFF_TBL_REPORT_PROPERTIES1_TARIFF_PRECISION_MASK = 0xE0
TARIFF_TBL_REPORT_PROPERTIES1_TARIFF_PRECISION_SHIFT = 0x05
# Values used for Tariff Tbl Supplier Report command
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES1_STANDING_CHARGE_PERIOD_MASK = 0x1F
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES1_STANDING_CHARGE_PRECISION_MASK = 0xE0
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES1_STANDING_CHARGE_PRECISION_SHIFT = 0x05
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES2_NUMBER_OF_SUPPLIER_CHARACTERS_MASK = 0x1F
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES2_RESERVED_MASK = 0xE0
TARIFF_TBL_SUPPLIER_REPORT_PROPERTIES2_RESERVED_SHIFT = 0x05

class ZW_TARIFF_TBL_COST_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('startYear1', uint8_t),
        ('startYear2', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHourLocalTime', uint8_t),
        ('startMinuteLocalTime', uint8_t),
        ('stopYear1', uint8_t),
        ('stopYear2', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHourLocalTime', uint8_t),
        ('stopMinuteLocalTime', uint8_t),
    ]


class ZW_TARIFF_TBL_COST_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('properties1', uint8_t),
        ('startYear1', uint8_t),
        ('startYear2', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHourLocalTime', uint8_t),
        ('startMinuteLocalTime', uint8_t),
        ('stopYear1', uint8_t),
        ('stopYear2', uint8_t),
        ('stopMonth', uint8_t),
        ('stopDay', uint8_t),
        ('stopHourLocalTime', uint8_t),
        ('stopMinuteLocalTime', uint8_t),
        ('currency1', uint8_t),
        ('currency2', uint8_t),
        ('currency3', uint8_t),
        ('properties2', uint8_t),
        ('costValue1', uint8_t),
        ('costValue2', uint8_t),
        ('costValue3', uint8_t),
        ('costValue4', uint8_t),
    ]


class ZW_TARIFF_TBL_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('rateParameterSetId', uint8_t)]


class ZW_TARIFF_TBL_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('properties1', uint8_t),
        ('tariffValue1', uint8_t),
        ('tariffValue2', uint8_t),
        ('tariffValue3', uint8_t),
        ('tariffValue4', uint8_t),
    ]


class ZW_TARIFF_TBL_SUPPLIER_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_TARIFF_TBL_SUPPLIER_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
        ('currency1', uint8_t),
        ('currency2', uint8_t),
        ('currency3', uint8_t),
        ('properties1', uint8_t),
        ('standingChargeValue1', uint8_t),
        ('standingChargeValue2', uint8_t),
        ('standingChargeValue3', uint8_t),
        ('standingChargeValue4', uint8_t),
        ('properties2', uint8_t),
        ('supplierCharacter1', uint8_t),
    ]
