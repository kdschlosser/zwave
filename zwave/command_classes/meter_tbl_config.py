# Meter Table Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_METER_TBL_CONFIG = 0x3C

METER_TBL_CONFIG_VERSION = 0x01
# Meter Table Point Adm Number Set
METER_TBL_TABLE_POINT_ADM_NO_SET = 0x01

# Values used for Meter Tbl Table Point Adm No Set command
METER_TBL_TABLE_POINT_ADM_NO_SET_PROPERTIES1_NUMBER_OF_CHARACTERS_MASK = 0x1F
METER_TBL_TABLE_POINT_ADM_NO_SET_PROPERTIES1_RESERVED_MASK = 0xE0
METER_TBL_TABLE_POINT_ADM_NO_SET_PROPERTIES1_RESERVED_SHIFT = 0x05



class ZW_METER_TBL_TABLE_POINT_ADM_NO_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('meterPointAdmNumberCharacter1', uint8_t),
    ]
