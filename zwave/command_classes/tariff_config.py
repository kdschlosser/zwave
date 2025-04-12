# Tariff Table Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_TARIFF_CONFIG = 0x4A

TARIFF_CONFIG_VERSION = 0x01
# Tariff Table Supplier Set
TARIFF_TBL_SUPPLIER_SET = 0x01
# Tariff Table Set
TARIFF_TBL_SET = 0x02
# Tariff Table Remove
TARIFF_TBL_REMOVE = 0x03

# Values used for Tariff Tbl Remove command
TARIFF_TBL_REMOVE_PROPERTIES1_RATE_PARAMETER_SET_IDS_MASK = 0x3F
TARIFF_TBL_REMOVE_PROPERTIES1_RESERVED_MASK = 0xC0
TARIFF_TBL_REMOVE_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Tariff Tbl Set command
TARIFF_TBL_SET_PROPERTIES1_RESERVED_MASK = 0x1F
TARIFF_TBL_SET_PROPERTIES1_TARIFF_PRECISION_MASK = 0xE0
TARIFF_TBL_SET_PROPERTIES1_TARIFF_PRECISION_SHIFT = 0x05
# Values used for Tariff Tbl Supplier Set command
TARIFF_TBL_SUPPLIER_SET_PROPERTIES1_STANDING_CHARGE_PERIOD_MASK = 0x1F
TARIFF_TBL_SUPPLIER_SET_PROPERTIES1_STANDING_CHARGE_PRECISION_MASK = 0xE0
TARIFF_TBL_SUPPLIER_SET_PROPERTIES1_STANDING_CHARGE_PRECISION_SHIFT = 0x05
TARIFF_TBL_SUPPLIER_SET_PROPERTIES2_NUMBER_OF_SUPPLIER_CHARACTERS_MASK = 0x1F
TARIFF_TBL_SUPPLIER_SET_PROPERTIES2_RESERVED_MASK = 0xE0
TARIFF_TBL_SUPPLIER_SET_PROPERTIES2_RESERVED_SHIFT = 0x05


class ZW_TARIFF_TBL_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('rateParameterSetId1', uint8_t),
    ]


class ZW_TARIFF_TBL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('rateParameterSetId', uint8_t),
        ('properties1', uint8_t),
        ('tariffValue1', uint8_t),
        ('tariffValue2', uint8_t),
        ('tariffValue3', uint8_t),
        ('tariffValue4', uint8_t),
    ]


class ZW_TARIFF_TBL_SUPPLIER_SET_FRAME(ZW_COMMON_FRAME):
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
