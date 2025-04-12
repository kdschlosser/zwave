from . import CommandClass, CommandClassCommands


class ANTITHEFT_UNLOCK_V1_COMMANDS(CommandClassCommands):
    version = 0x01
    GET = 0x01
    REPORT = 0x02
    SET = 0x03
    SET_VALUES = []
    GET_VALUES = []
    REPORT_VALUES = []


class COMMAND_CLASS_ANTITHEFT_UNLOCK(CommandClass):
    id = 0x7E
    versions = [
        ANTITHEFT_UNLOCK_V1_COMMANDS
    ]


# Values used for Antitheft Unlock State Report command
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_STATE_BIT_MASK = 0x01
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_RESTRICTED_BIT_MASK = 0x02
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_ANTI_THEFT_HINT_LENGTH_MASK = 0x3C
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_ANTI_THEFT_HINT_LENGTH_SHIFT = 0x02
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_RESERVED_MASK = 0xC0
ANTITHEFT_UNLOCK_STATE_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Antitheft Unlock Set command
ANTITHEFT_UNLOCK_SET_PROPERTIES1_MAGIC_CODE_LENGTH_MASK = 0x0F
ANTITHEFT_UNLOCK_SET_PROPERTIES1_RESERVED_MASK = 0xF0
ANTITHEFT_UNLOCK_SET_PROPERTIES1_RESERVED_SHIFT = 0x04


class ZW_ANTITHEFT_UNLOCK_STATE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_UNLOCK_STATE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('antiTheftHint1', uint8_t),
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('zWaveAllianceLockingEntityId1', uint8_t),
        ('zWaveAllianceLockingEntityId2', uint8_t),
    ]


class ZW_ANTITHEFT_UNLOCK_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('magicCode1', uint8_t),
    ]

