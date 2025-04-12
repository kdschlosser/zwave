# Security 0 Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_SECURITY = 0x98

SECURITY_VERSION = 0x01
# Security Commands Supported Get
SECURITY_COMMANDS_SUPPORTED_GET = 0x02
# Security Commands Supported Report
SECURITY_COMMANDS_SUPPORTED_REPORT = 0x03
# Security Scheme Get
SECURITY_SCHEME_GET = 0x04
# Security Scheme Report
SECURITY_SCHEME_REPORT = 0x05
# Network Key Set
NETWORK_KEY_SET = 0x06
# Network Key Verify
NETWORK_KEY_VERIFY = 0x07
# Security Scheme Inherit
SECURITY_SCHEME_INHERIT = 0x08
# Nonce Challenge Request
SECURITY_NONCE_GET = 0x40
# Nonce Challenge Response
SECURITY_NONCE_REPORT = 0x80
# Security Message Encapsulation
SECURITY_MESSAGE_ENCAPSULATION = 0x81
# Security Message Encapsulation
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET = 0xC1

# Values used for Security Commands Supported Report command
SECURITY_COMMANDS_SUPPORTED_REPORT_COMMAND_CLASS_MARK = 0xEF
# Values used for Security Message Encapsulation command
SECURITY_MESSAGE_ENCAPSULATION_PROPERTIES1_SEQUENCE_COUNTER_MASK = 0x0F
SECURITY_MESSAGE_ENCAPSULATION_PROPERTIES1_SEQUENCED_BIT_MASK = 0x10
SECURITY_MESSAGE_ENCAPSULATION_PROPERTIES1_SECOND_FRAME_BIT_MASK = 0x20
SECURITY_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_MASK = 0xC0
SECURITY_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_SHIFT = 0x06
# Values used for Security Message Encapsulation Nonce Get command
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_PROPERTIES1_SEQUENCE_COUNTER_MASK = 0x0F
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_PROPERTIES1_SEQUENCED_BIT_MASK = 0x10
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_PROPERTIES1_SECOND_FRAME_BIT_MASK = 0x20
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_PROPERTIES1_RESERVED_MASK = 0xC0
SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_PROPERTIES1_RESERVED_SHIFT = 0x06


class ZW_NETWORK_KEY_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('networkKeyByte1', uint8_t)]


class ZW_NETWORK_KEY_VERIFY_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SECURITY_COMMANDS_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SECURITY_COMMANDS_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('reportsToFollow', uint8_t),
        ('commandClassSupport1', uint8_t),
        ('commandClassMark', uint8_t),
        ('commandClassControl1', uint8_t),
    ]


class ZW_SECURITY_MESSAGE_ENCAPSULATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('initializationVectorByte1', uint8_t),
        ('initializationVectorByte2', uint8_t),
        ('initializationVectorByte3', uint8_t),
        ('initializationVectorByte4', uint8_t),
        ('initializationVectorByte5', uint8_t),
        ('initializationVectorByte6', uint8_t),
        ('initializationVectorByte7', uint8_t),
        ('initializationVectorByte8', uint8_t),
        ('properties1', uint8_t),
        ('commandClassIdentifier', uint8_t),
        ('commandIdentifier', uint8_t),
        ('commandByte1', uint8_t),
        ('receiversNonceIdentifier', uint8_t),
        ('messageAuthenticationCodeByte1', uint8_t),
        ('messageAuthenticationCodeByte2', uint8_t),
        ('messageAuthenticationCodeByte3', uint8_t),
        ('messageAuthenticationCodeByte4', uint8_t),
        ('messageAuthenticationCodeByte5', uint8_t),
        ('messageAuthenticationCodeByte6', uint8_t),
        ('messageAuthenticationCodeByte7', uint8_t),
        ('messageAuthenticationCodeByte8', uint8_t),
    ]


class ZW_SECURITY_MESSAGE_ENCAPSULATION_NONCE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('initializationVectorByte1', uint8_t),
        ('initializationVectorByte2', uint8_t),
        ('initializationVectorByte3', uint8_t),
        ('initializationVectorByte4', uint8_t),
        ('initializationVectorByte5', uint8_t),
        ('initializationVectorByte6', uint8_t),
        ('initializationVectorByte7', uint8_t),
        ('initializationVectorByte8', uint8_t),
        ('properties1', uint8_t),
        ('commandClassIdentifier', uint8_t),
        ('commandIdentifier', uint8_t),
        ('commandByte1', uint8_t),
        ('receiversNonceIdentifier', uint8_t),
        ('messageAuthenticationCodeByte1', uint8_t),
        ('messageAuthenticationCodeByte2', uint8_t),
        ('messageAuthenticationCodeByte3', uint8_t),
        ('messageAuthenticationCodeByte4', uint8_t),
        ('messageAuthenticationCodeByte5', uint8_t),
        ('messageAuthenticationCodeByte6', uint8_t),
        ('messageAuthenticationCodeByte7', uint8_t),
        ('messageAuthenticationCodeByte8', uint8_t),
    ]


class ZW_SECURITY_NONCE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SECURITY_NONCE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('nonceByte1', uint8_t),
        ('nonceByte2', uint8_t),
        ('nonceByte3', uint8_t),
        ('nonceByte4', uint8_t),
        ('nonceByte5', uint8_t),
        ('nonceByte6', uint8_t),
        ('nonceByte7', uint8_t),
        ('nonceByte8', uint8_t),
    ]


class ZW_SECURITY_SCHEME_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedSecuritySchemes', uint8_t)]


class ZW_SECURITY_SCHEME_INHERIT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedSecuritySchemes', uint8_t)]


class ZW_SECURITY_SCHEME_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('supportedSecuritySchemes', uint8_t)]

