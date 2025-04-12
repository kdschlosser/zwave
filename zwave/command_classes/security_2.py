# Security 2 Command Class
# Transport-Encapsulation
# ==============================
COMMAND_CLASS_SECURITY_2 = 0x9F

SECURITY_2_VERSION = 0x01
# Security 2 Nonce Get
SECURITY_2_NONCE_GET = 0x01
# Security 2 Nonce Report
SECURITY_2_NONCE_REPORT = 0x02
# Security 2 Message Encapsulation
SECURITY_2_MESSAGE_ENCAPSULATION = 0x03
# Security 2 KEX Get
KEX_GET = 0x04
# Security 2 KEX Report
KEX_REPORT = 0x05
# Security 2 KEX Set
KEX_SET = 0x06
# Security 2 KEX Fail
KEX_FAIL = 0x07
# Security 2 Public Key Report
PUBLIC_KEY_REPORT = 0x08
# Security 2 Network Key Get
SECURITY_2_NETWORK_KEY_GET = 0x09
# Security 2 Network Key Report
SECURITY_2_NETWORK_KEY_REPORT = 0x0A
# Security 2 Network Key Verify
SECURITY_2_NETWORK_KEY_VERIFY = 0x0B
# Security 2 Transfer End
SECURITY_2_TRANSFER_END = 0x0C
# Security 2 Commands Supported Get
SECURITY_2_COMMANDS_SUPPORTED_GET = 0x0D
# Security 2 Commands Supported Report
SECURITY_2_COMMANDS_SUPPORTED_REPORT = 0x0E

# Values used for Security 2 Nonce Report command
SECURITY_2_NONCE_REPORT_PROPERTIES1_SOS_BIT_MASK = 0x01
SECURITY_2_NONCE_REPORT_PROPERTIES1_MOS_BIT_MASK = 0x02
SECURITY_2_NONCE_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
SECURITY_2_NONCE_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Security 2 Message Encapsulation command
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_EXTENSION_BIT_MASK = 0x01
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_ENCRYPTED_EXTENSION_BIT_MASK = 0x02
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_MASK = 0xFC
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Kex Report command
KEX_REPORT_PROPERTIES1_ECHO_BIT_MASK = 0x01
KEX_REPORT_PROPERTIES1_REQUEST_CSA_BIT_MASK = 0x02
KEX_REPORT_PROPERTIES1_RESERVED_MASK = 0xFC
KEX_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Kex Set command
KEX_SET_PROPERTIES1_ECHO_BIT_MASK = 0x01
KEX_SET_PROPERTIES1_REQUEST_CSA_BIT_MASK = 0x02
KEX_SET_PROPERTIES1_RESERVED_MASK = 0xFC
KEX_SET_PROPERTIES1_RESERVED_SHIFT = 0x02
# Values used for Kex Fail command
KEX_FAIL_KEX_KEY = 0x01
KEX_FAIL_KEX_SCHEME = 0x02
KEX_FAIL_KEX_CURVES = 0x03
KEX_FAIL_DECRYPT = 0x05
KEX_FAIL_CANCEL = 0x06
KEX_FAIL_AUTH = 0x07
KEX_FAIL_KEY_GET = 0x08
KEX_FAIL_KEY_VERIFY = 0x09
KEX_FAIL_KEY_REPORT = 0x0A
# Values used for Public Key Report command
PUBLIC_KEY_REPORT_PROPERTIES1_INCLUDING_NODE_BIT_MASK = 0x01
PUBLIC_KEY_REPORT_PROPERTIES1_RESERVED_MASK = 0xFE
PUBLIC_KEY_REPORT_PROPERTIES1_RESERVED_SHIFT = 0x01
# Values used for Security 2 Transfer End command
SECURITY_2_TRANSFER_END_PROPERTIES1_KEY_REQUEST_COMPLETE_BIT_MASK = 0x01
SECURITY_2_TRANSFER_END_PROPERTIES1_KEY_VERIFIED_BIT_MASK = 0x02
SECURITY_2_TRANSFER_END_PROPERTIES1_RESERVED_MASK = 0xFC
SECURITY_2_TRANSFER_END_PROPERTIES1_RESERVED_SHIFT = 0x02

SECURITY_2_VERSION_V2 = 0x02
SECURITY_2_NONCE_GET_V2 = 0x01
SECURITY_2_NONCE_REPORT_V2 = 0x02
SECURITY_2_MESSAGE_ENCAPSULATION_V2 = 0x03
KEX_GET_V2 = 0x04
KEX_REPORT_V2 = 0x05
KEX_SET_V2 = 0x06
KEX_FAIL_V2 = 0x07
PUBLIC_KEY_REPORT_V2 = 0x08
SECURITY_2_NETWORK_KEY_GET_V2 = 0x09
SECURITY_2_NETWORK_KEY_REPORT_V2 = 0x0A
SECURITY_2_NETWORK_KEY_VERIFY_V2 = 0x0B
SECURITY_2_TRANSFER_END_V2 = 0x0C
SECURITY_2_COMMANDS_SUPPORTED_GET_V2 = 0x0D
SECURITY_2_COMMANDS_SUPPORTED_REPORT_V2 = 0x0E
NLS_NODE_LIST_GET_V2 = 0x0F
NLS_NODE_LIST_REPORT_V2 = 0x10
NLS_STATE_GET_V2 = 0x11
NLS_STATE_REPORT_V2 = 0x12
NLS_STATE_SET_V2 = 0x13
# Values used for Security 2 Nonce Report command
SECURITY_2_NONCE_REPORT_PROPERTIES1_SOS_BIT_MASK_V2 = 0x01
SECURITY_2_NONCE_REPORT_PROPERTIES1_MOS_BIT_MASK_V2 = 0x02
SECURITY_2_NONCE_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
SECURITY_2_NONCE_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
# Values used for Security 2 Message Encapsulation command
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_EXTENSION_BIT_MASK_V2 = 0x01
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_ENCRYPTED_EXTENSION_BIT_MASK_V2 = 0x02
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
SECURITY_2_MESSAGE_ENCAPSULATION_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
# Values used for Kex Report command
KEX_REPORT_PROPERTIES1_ECHO_BIT_MASK_V2 = 0x01
KEX_REPORT_PROPERTIES1_REQUEST_CSA_BIT_MASK_V2 = 0x02
KEX_REPORT_PROPERTIES1_NLS_SUPPORT_BIT_MASK_V2 = 0x04
KEX_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xF8
KEX_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x03
# Values used for Kex Set command
KEX_SET_PROPERTIES1_ECHO_BIT_MASK_V2 = 0x01
KEX_SET_PROPERTIES1_REQUEST_CSA_BIT_MASK_V2 = 0x02
KEX_SET_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
KEX_SET_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
# Values used for Kex Fail command
KEX_FAIL_KEX_KEY_V2 = 0x01
KEX_FAIL_KEX_SCHEME_V2 = 0x02
KEX_FAIL_KEX_CURVES_V2 = 0x03
KEX_FAIL_DECRYPT_V2 = 0x05
KEX_FAIL_CANCEL_V2 = 0x06
KEX_FAIL_AUTH_V2 = 0x07
KEX_FAIL_KEY_GET_V2 = 0x08
KEX_FAIL_KEY_VERIFY_V2 = 0x09
KEX_FAIL_KEY_REPORT_V2 = 0x0A
# Values used for Public Key Report command
PUBLIC_KEY_REPORT_PROPERTIES1_INCLUDING_NODE_BIT_MASK_V2 = 0x01
PUBLIC_KEY_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
PUBLIC_KEY_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01
# Values used for Security 2 Transfer End command
SECURITY_2_TRANSFER_END_PROPERTIES1_KEY_REQUEST_COMPLETE_BIT_MASK_V2 = 0x01
SECURITY_2_TRANSFER_END_PROPERTIES1_KEY_VERIFIED_BIT_MASK_V2 = 0x02
SECURITY_2_TRANSFER_END_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
SECURITY_2_TRANSFER_END_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02
# Values used for Nls Node List Report command
NLS_NODE_LIST_REPORT_PROPERTIES1_LAST_NODE_BIT_MASK_V2 = 0x01
NLS_NODE_LIST_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFE
NLS_NODE_LIST_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x01
# Values used for Nls State Report command
NLS_STATE_REPORT_PROPERTIES1_CAPABILITY_BIT_MASK_V2 = 0x01
NLS_STATE_REPORT_PROPERTIES1_NLS_STATE_BIT_MASK_V2 = 0x02
NLS_STATE_REPORT_PROPERTIES1_RESERVED_MASK_V2 = 0xFC
NLS_STATE_REPORT_PROPERTIES1_RESERVED_SHIFT_V2 = 0x02

class ZW_SECURITY_2_NONCE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('sequenceNumber', uint8_t)]


class ZW_SECURITY_2_NONCE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('properties1', uint8_t),
        ('receiversEntropyInput1', uint8_t),
        ('receiversEntropyInput2', uint8_t),
        ('receiversEntropyInput3', uint8_t),
        ('receiversEntropyInput4', uint8_t),
        ('receiversEntropyInput5', uint8_t),
        ('receiversEntropyInput6', uint8_t),
        ('receiversEntropyInput7', uint8_t),
        ('receiversEntropyInput8', uint8_t),
        ('receiversEntropyInput9', uint8_t),
        ('receiversEntropyInput10', uint8_t),
        ('receiversEntropyInput11', uint8_t),
        ('receiversEntropyInput12', uint8_t),
        ('receiversEntropyInput13', uint8_t),
        ('receiversEntropyInput14', uint8_t),
        ('receiversEntropyInput15', uint8_t),
        ('receiversEntropyInput16', uint8_t),
    ]


class VG_SECURITY_2_MESSAGE_ENCAPSULATION_VG(ctypes.Structure):
    _fields_ = [
        ('extensionLength', uint8_t),
        ('properties1', uint8_t),
        ('extension1', uint8_t),
    ]


class ZW_SECURITY_2_MESSAGE_ENCAPSULATION_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sequenceNumber', uint8_t),
        ('properties1', uint8_t),
        ('variantgroup1', VG_SECURITY_2_MESSAGE_ENCAPSULATION_VG),
        ('ccmCiphertextObject1', uint8_t),
    ]


class ZW_KEX_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_KEX_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('supportedKexSchemes', uint8_t),
        ('supportedEcdhProfiles', uint8_t),
        ('requestedKeys', uint8_t),
    ]


class ZW_KEX_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('selectedKexScheme', uint8_t),
        ('selectedEcdhProfile', uint8_t),
        ('grantedKeys', uint8_t),
    ]


class ZW_KEX_FAIL_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('kexFailType', uint8_t)]


class ZW_PUBLIC_KEY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('ecdhPublicKey1', uint8_t),
    ]


class ZW_SECURITY_2_NETWORK_KEY_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('requestedKey', uint8_t)]


class ZW_SECURITY_2_NETWORK_KEY_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('grantedKey', uint8_t),
        ('networkKey1', uint8_t),
        ('networkKey2', uint8_t),
        ('networkKey3', uint8_t),
        ('networkKey4', uint8_t),
        ('networkKey5', uint8_t),
        ('networkKey6', uint8_t),
        ('networkKey7', uint8_t),
        ('networkKey8', uint8_t),
        ('networkKey9', uint8_t),
        ('networkKey10', uint8_t),
        ('networkKey11', uint8_t),
        ('networkKey12', uint8_t),
        ('networkKey13', uint8_t),
        ('networkKey14', uint8_t),
        ('networkKey15', uint8_t),
        ('networkKey16', uint8_t),
    ]


class ZW_SECURITY_2_NETWORK_KEY_VERIFY_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SECURITY_2_TRANSFER_END_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_SECURITY_2_COMMANDS_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_SECURITY_2_COMMANDS_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('commandClass1', uint8_t)]


class ZW_SECURITY_2_NONCE_GET_V2_FRAME(ZW_SECURITY_2_NONCE_GET_FRAME):
    _fields_ = []


class ZW_SECURITY_2_NONCE_REPORT_V2_FRAME(ZW_SECURITY_2_NONCE_REPORT_FRAME):
    _fields_ = []


class ZW_SECURITY_2_MESSAGE_ENCAPSULATION_V2_FRAME(ZW_SECURITY_2_MESSAGE_ENCAPSULATION_FRAME):
    _fields_ = []


class ZW_KEX_GET_V2_FRAME(ZW_KEX_GET_FRAME):
    _fields_ = []


class ZW_KEX_REPORT_V2_FRAME(ZW_KEX_REPORT_FRAME):
    _fields_ = []


class ZW_KEX_SET_V2_FRAME(ZW_KEX_SET_FRAME):
    _fields_ = []


class ZW_KEX_FAIL_V2_FRAME(ZW_KEX_FAIL_FRAME):
    _fields_ = []


class ZW_PUBLIC_KEY_REPORT_V2_FRAME(ZW_PUBLIC_KEY_REPORT_FRAME):
    _fields_ = []


class ZW_SECURITY_2_NETWORK_KEY_GET_V2_FRAME(ZW_SECURITY_2_NETWORK_KEY_GET_FRAME):
    _fields_ = []


class ZW_SECURITY_2_NETWORK_KEY_REPORT_V2_FRAME(ZW_SECURITY_2_NETWORK_KEY_REPORT_FRAME):
    _fields_ = []


class ZW_SECURITY_2_NETWORK_KEY_VERIFY_V2_FRAME(ZW_SECURITY_2_NETWORK_KEY_VERIFY_FRAME):
    _fields_ = []


class ZW_SECURITY_2_TRANSFER_END_V2_FRAME(ZW_SECURITY_2_TRANSFER_END_FRAME):
    _fields_ = []


class ZW_SECURITY_2_COMMANDS_SUPPORTED_GET_V2_FRAME(ZW_SECURITY_2_COMMANDS_SUPPORTED_GET_FRAME):
    _fields_ = []


class ZW_SECURITY_2_COMMANDS_SUPPORTED_REPORT_V2_FRAME(ZW_SECURITY_2_COMMANDS_SUPPORTED_REPORT_FRAME):
    _fields_ = []


class ZW_NLS_NODE_LIST_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('request', uint8_t)]


class ZW_NLS_NODE_LIST_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('idMsbOfNodeN', uint8_t),
        ('idLsbOfNodeN', uint8_t),
        ('grantedKeysBitmaskOfNodeN', uint8_t),
        ('nlsStateOfNodeN', uint8_t),
    ]


class ZW_NLS_STATE_GET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_NLS_STATE_REPORT_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_NLS_STATE_SET_V2_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('nlsState', uint8_t)]

