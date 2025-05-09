# Prepayment Command Class
# Application
# ==============================
COMMAND_CLASS_PREPAYMENT = 0x3F

PREPAYMENT_VERSION = 0x01
# Prepayment Balance Get
PREPAYMENT_BALANCE_GET = 0x01
# Prepayment Balance Report
PREPAYMENT_BALANCE_REPORT = 0x02
# Prepayment Supported Get
PREPAYMENT_SUPPORTED_GET = 0x03
# Prepayment Supported Report
PREPAYMENT_SUPPORTED_REPORT = 0x04

# Values used for Prepayment Balance Get command
PREPAYMENT_BALANCE_GET_PROPERTIES1_RESERVED_MASK = 0x3F
PREPAYMENT_BALANCE_GET_PROPERTIES1_BALANCE_TYPE_MASK = 0xC0
PREPAYMENT_BALANCE_GET_PROPERTIES1_BALANCE_TYPE_SHIFT = 0x06
PREPAYMENT_BALANCE_GET_BALANCE_TYPE_UTILITY = 0x00
PREPAYMENT_BALANCE_GET_BALANCE_TYPE_MONETARY = 0x01
# Values used for Prepayment Balance Report command
PREPAYMENT_BALANCE_REPORT_PROPERTIES1_METER_TYPE_MASK = 0x3F
PREPAYMENT_BALANCE_REPORT_PROPERTIES1_BALANCE_TYPE_MASK = 0xC0
PREPAYMENT_BALANCE_REPORT_PROPERTIES1_BALANCE_TYPE_SHIFT = 0x06
PREPAYMENT_BALANCE_REPORT_PROPERTIES2_SCALE_MASK = 0x1F
PREPAYMENT_BALANCE_REPORT_PROPERTIES2_BALANCE_PRECISION_MASK = 0xE0
PREPAYMENT_BALANCE_REPORT_PROPERTIES2_BALANCE_PRECISION_SHIFT = 0x05
PREPAYMENT_BALANCE_REPORT_PROPERTIES3_RESERVED1_MASK = 0x1F
PREPAYMENT_BALANCE_REPORT_PROPERTIES3_DEBT_PRECISION_MASK = 0xE0
PREPAYMENT_BALANCE_REPORT_PROPERTIES3_DEBT_PRECISION_SHIFT = 0x05
PREPAYMENT_BALANCE_REPORT_PROPERTIES4_RESERVED2_MASK = 0x1F
PREPAYMENT_BALANCE_REPORT_PROPERTIES4_EMER_CREDIT_PRECISION_MASK = 0xE0
PREPAYMENT_BALANCE_REPORT_PROPERTIES4_EMER_CREDIT_PRECISION_SHIFT = 0x05
# Values used for Prepayment Supported Report command
PREPAYMENT_SUPPORTED_REPORT_PROPERTIES1_TYPES_SUPPORTED_MASK = 0x0F
PREPAYMENT_SUPPORTED_REPORT_PROPERTIES1_RESERVED_MASK = 0xF0
PREPAYMENT_SUPPORTED_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x04


class ZW_PREPAYMENT_BALANCE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_PREPAYMENT_BALANCE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('properties2', uint8_t),
        ('balanceValue1', uint8_t),
        ('balanceValue2', uint8_t),
        ('balanceValue3', uint8_t),
        ('balanceValue4', uint8_t),
        ('properties3', uint8_t),
        ('debt1', uint8_t),
        ('debt2', uint8_t),
        ('debt3', uint8_t),
        ('debt4', uint8_t),
        ('properties4', uint8_t),
        ('emerCredit1', uint8_t),
        ('emerCredit2', uint8_t),
        ('emerCredit3', uint8_t),
        ('emerCredit4', uint8_t),
        ('currency1', uint8_t),
        ('currency2', uint8_t),
        ('currency3', uint8_t),
        ('debtRecoveryPercentage', uint8_t),
    ]


class ZW_PREPAYMENT_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_PREPAYMENT_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]

