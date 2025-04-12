from . import CommandClass, CommandClassCommands


# Anti-theft Command Class
# Application
# ==============================


class ANTITHEFT_V1_COMMANDS(CommandClassCommands):
    version = 0x01
    SET = 0x01
    GET = 0x02
    REPORT = 0x03
    SET_VALUES = []
    GET_VALUES = []
    REPORT_VALUES = []


class ANTITHEFT_V2_COMMANDS(ANTITHEFT_V1_COMMANDS):
    version = 0x02
    REPORT_VALUES = [
        'Reserved',
        'Disabled',
        'Enabled',
        'Not Fully Enabled'
    ]


class ANTITHEFT_V3_COMMANDS(ANTITHEFT_V2_COMMANDS):
    version = 0x03
    SET_VALUES = []
    GET_VALUES = []


class COMMAND_CLASS_ANTITHEFT(CommandClass):
    id = 0x5D
    versions = [
        ANTITHEFT_V1_COMMANDS,
        ANTITHEFT_V2_COMMANDS,
        ANTITHEFT_V3_COMMANDS
    ]


# Anti-theft Set
# Values used for Antitheft Set command
ANTITHEFT_SET_PROPERTIES1_NUMBER_OF_MAGIC_CODE_BYTES_MASK_V1 = 0x7F
ANTITHEFT_SET_PROPERTIES1_ENABLE_BIT_MASK_V1 = 0x80

# Values used for Antitheft Set command
ANTITHEFT_SET_PROPERTIES1_NUMBER_OF_MAGIC_CODE_BYTES_MASK_V2 = 0x7F
ANTITHEFT_SET_PROPERTIES1_ENABLE_BIT_MASK_V2 = 0x80

# Values used for Antitheft Set command
ANTITHEFT_SET_PROPERTIES1_NUMBER_OF_MAGIC_CODE_BYTES_MASK_V3 = 0x7F
ANTITHEFT_SET_PROPERTIES1_ENABLE_BIT_MASK_V3 = 0x80


class ZW_ANTITHEFT_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('magicCode1', uint8_t),
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('antiTheftHintNumberBytes', uint8_t),
        ('antiTheftHintByte1', uint8_t),
    ]


class ZW_ANTITHEFT_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('antiTheftProtectionStatus', uint8_t),
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('antiTheftHintNumberBytes', uint8_t),
        ('antiTheftHintByte1', uint8_t),
    ]


class ZW_ANTITHEFT_SET_V2_FRAME(ZW_ANTITHEFT_SET_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_GET_V2_FRAME(ZW_ANTITHEFT_GET_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_REPORT_V2_FRAME(ZW_ANTITHEFT_REPORT_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_SET_V3_FRAME(ZW_ANTITHEFT_SET_V2_FRAME):
    _fields_ = [
        ('zWaveAllianceLockingEntityId1', uint8_t),
        ('zWaveAllianceLockingEntityId2', uint8_t),
    ]


class ZW_ANTITHEFT_GET_V3_FRAME(ZW_ANTITHEFT_GET_V2_FRAME):
    _fields_ = []


class ZW_ANTITHEFT_REPORT_V3_FRAME(ZW_ANTITHEFT_REPORT_V2_FRAME):
    _fields_ = [
        ('zWaveAllianceLockingEntityId1', uint8_t),
        ('zWaveAllianceLockingEntityId2', uint8_t),
    ]

