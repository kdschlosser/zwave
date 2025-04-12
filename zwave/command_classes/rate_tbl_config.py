# Rate Table Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_RATE_TBL_CONFIG = 0x48

RATE_TBL_CONFIG_VERSION = 0x01
# Rate Table Set
RATE_TBL_SET = 0x01
# Rate Table Remove
RATE_TBL_REMOVE = 0x02

# Values used for Rate Tbl Remove command
RATE_TBL_REMOVE_PROPERTIES1_RATE_PARAMETER_SET_IDS_MASK = 0x3F
RATE_TBL_REMOVE_PROPERTIES1_RESERVED_MASK = 0xC0
RATE_TBL_REMOVE_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Rate Tbl Set command
RATE_TBL_SET_PROPERTIES1_NUMBER_OF_RATE_CHAR_MASK = 0x1F
RATE_TBL_SET_PROPERTIES1_RATE_TYPE_MASK = 0x60
RATE_TBL_SET_PROPERTIES1_RATE_TYPE_SHIFT = 0x05
RATE_TBL_SET_PROPERTIES1_RESERVED_BIT_MASK = 0x80
RATE_TBL_SET_PROPERTIES2_CONSUMPTION_SCALE_MASK = 0x1F
RATE_TBL_SET_PROPERTIES2_CONSUMPTION_PRECISION_MASK = 0xE0
RATE_TBL_SET_PROPERTIES2_CONSUMPTION_PRECISION_SHIFT = 0x05
RATE_TBL_SET_PROPERTIES3_MAX_DEMAND_SCALE_MASK = 0x1F
RATE_TBL_SET_PROPERTIES3_MAX_DEMAND_PRECISION_MASK = 0xE0
RATE_TBL_SET_PROPERTIES3_MAX_DEMAND_PRECISION_SHIFT = 0x05



class ZW_RATE_TBL_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('rateParameterSetId1', uint8_t),
    ]


class ZW_RATE_TBL_SET_FRAME(ZW_COMMON_FRAME):
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

