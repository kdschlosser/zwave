from . import CommandClass, CommandClassCommands


# Basic Tariff Information Command Class
# Application
# ==============================


class BASIC_TARIFF_INFO_V1_COMMANDS(CommandClassCommands):
    version = 0x01

    GET = 0x01
    REPORT = 0x02


class COMMAND_CLASS_BASIC_TARIFF_INFO(CommandClass):
    id = 0x36
    versions = [
        BASIC_TARIFF_INFO_V1_COMMANDS
    ]


# Values used for Basic Tariff Info Report command
BASIC_TARIFF_INFO_REPORT_PROPERTIES1_TOTAL_NO_IMPORT_RATES_MASK = 0x0F
BASIC_TARIFF_INFO_REPORT_PROPERTIES1_RESERVED1_MASK = 0x70
BASIC_TARIFF_INFO_REPORT_PROPERTIES1_RESERVED1_SHIFT = 0x04
BASIC_TARIFF_INFO_REPORT_PROPERTIES1_DUAL_BIT_MASK = 0x80
BASIC_TARIFF_INFO_REPORT_PROPERTIES2_E1_CURRENT_RATE_IN_USE_MASK = 0x0F
BASIC_TARIFF_INFO_REPORT_PROPERTIES2_RESERVED2_MASK = 0xF0
BASIC_TARIFF_INFO_REPORT_PROPERTIES2_RESERVED2_SHIFT = 0x04
BASIC_TARIFF_INFO_REPORT_PROPERTIES3_E2_CURRENT_RATE_IN_USE_MASK = 0x0F
BASIC_TARIFF_INFO_REPORT_PROPERTIES3_RESERVED3_MASK = 0xF0
BASIC_TARIFF_INFO_REPORT_PROPERTIES3_RESERVED3_SHIFT = 0x04






class ZW_BASIC_TARIFF_INFO_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_BASIC_TARIFF_INFO_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('e1RateConsumptionRegister1', uint8_t),
        ('e1RateConsumptionRegister2', uint8_t),
        ('e1RateConsumptionRegister3', uint8_t),
        ('e1RateConsumptionRegister4', uint8_t),
        ('e1TimeForNextRateHours', uint8_t),
        ('e1TimeForNextRateMinutes', uint8_t),
        ('e1TimeForNextRateSeconds', uint8_t),
        ('properties3', uint8_t),
        ('e2RateConsumptionRegister1', uint8_t),
        ('e2RateConsumptionRegister2', uint8_t),
        ('e2RateConsumptionRegister3', uint8_t),
        ('e2RateConsumptionRegister4', uint8_t),
    ]

