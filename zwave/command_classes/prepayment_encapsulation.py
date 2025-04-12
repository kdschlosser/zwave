# Prepayment Encapsulation Command Class
# Application
# ==============================
COMMAND_CLASS_PREPAYMENT_ENCAPSULATION = 0x41

PREPAYMENT_ENCAPSULATION_VERSION = 0x01
# Prepayment Encapsulation
CMD_ENCAPSULATION = 0x01


class ZW_CMD_ENCAPSULATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('data1', uint8_t)]

