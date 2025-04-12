
class ZW_USER_CAPABILITIES_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class VG_USER_CAPABILITIES_REPORT_VG(ctypes.Structure):
    _fields_ = [('supportedUserTypesBitMask', uint8_t)]


class ZW_USER_CAPABILITIES_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfSupportedUserUniqueIdentifiers1', uint8_t),
        ('numberOfSupportedUserUniqueIdentifiers2', uint8_t),
        ('supportedCredentialRulesBitMask', uint8_t),
        ('maxLengthOfUserName', uint8_t),
        ('properties1', uint8_t),
        ('supportedUserTypesBitMaskLength', uint8_t),
        ('variantgroup1', VG_USER_CAPABILITIES_REPORT_VG),
    ]


class ZW_CREDENTIAL_CAPABILITIES_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class VG_CREDENTIAL_CAPABILITIES_REPORT_VG(ctypes.Structure):
    _fields_ = [('credentialType', uint8_t)]


class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_1(ctypes.Structure):
    _fields_ = [('properties2', uint8_t)]



class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_2(ctypes.Structure):
    _fields_ = [
        ('numberOfSupportedCredentialSlots1', uint8_t),
        ('numberOfSupportedCredentialSlots2', uint8_t),
    ]


class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_3(ctypes.Structure):
    _fields_ = [('minLengthOfCredentialData', uint8_t)]



class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_4(ctypes.Structure):
    _fields_ = [('maxLengthOfCredentialData', uint8_t)]



class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_5(ctypes.Structure):
    _fields_ = [('clRecommendedTimeout', uint8_t)]



class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_6(ctypes.Structure):
    _fields_ = [('clNumberOfSteps', uint8_t)]



class VG_CREDENTIAL_CAPABILITIES_REPORT_VG_7(ctypes.Structure):
    _fields_ = [('maximumCredentialHashLength', uint8_t)]


class ZW_CREDENTIAL_CAPABILITIES_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('numberOfSupportedCredentialTypes', uint8_t),
        ('variantgroup1', VG_CREDENTIAL_CAPABILITIES_REPORT_VG),
        ('variantgroup1_1', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_1),
        ('variantgroup1_2', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_2),
        ('variantgroup1_3', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_3),
        ('variantgroup1_4', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_4),
        ('variantgroup1_5', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_5),
        ('variantgroup1_6', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_6),
        ('variantgroup1_7', VG_CREDENTIAL_CAPABILITIES_REPORT_VG_7),
    ]


class ZW_USER_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('userType', uint8_t),
        ('properties2', uint8_t),
        ('credentialRule', uint8_t),
        ('expiringTimeoutMinutes1', uint8_t),
        ('expiringTimeoutMinutes2', uint8_t),
        ('properties3', uint8_t),
        ('userNameLength', uint8_t),
        ('userName1', uint8_t),
    ]


class ZW_USER_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
    ]


class ZW_USER_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userReportType', uint8_t),
        ('nextUserUniqueIdentifier1', uint8_t),
        ('nextUserUniqueIdentifier2', uint8_t),
        ('userModifierType', uint8_t),
        ('userModifierNodeId1', uint8_t),
        ('userModifierNodeId2', uint8_t),
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('userType', uint8_t),
        ('properties1', uint8_t),
        ('credentialRule', uint8_t),
        ('expiringTimeoutMinutes1', uint8_t),
        ('expiringTimeoutMinutes2', uint8_t),
        ('properties2', uint8_t),
        ('userNameLength', uint8_t),
        ('userName1', uint8_t),
    ]


class ZW_CREDENTIAL_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('credentialType', uint8_t),
        ('credentialSlot1', uint8_t),
        ('credentialSlot2', uint8_t),
        ('properties1', uint8_t),
        ('credentialLength', uint8_t),
        ('credentialData1', uint8_t),
    ]


class ZW_CREDENTIAL_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('credentialType', uint8_t),
        ('credentialSlot1', uint8_t),
        ('credentialSlot2', uint8_t),
    ]


class ZW_CREDENTIAL_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('credentialReportType', uint8_t),
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('credentialType', uint8_t),
        ('credentialSlot1', uint8_t),
        ('credentialSlot2', uint8_t),
        ('properties1', uint8_t),
        ('credentialLength', uint8_t),
        ('credentialData1', uint8_t),
        ('credentialModifierType', uint8_t),
        ('credentialModifierNodeId1', uint8_t),
        ('credentialModifierNodeId2', uint8_t),
        ('nextCredentialType', uint8_t),
        ('nextCredentialSlot1', uint8_t),
        ('nextCredentialSlot2', uint8_t),
    ]


class ZW_CREDENTIAL_LEARN_START_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('credentialType', uint8_t),
        ('credentialSlot1', uint8_t),
        ('credentialSlot2', uint8_t),
        ('properties1', uint8_t),
        ('credentialLearnTimeout', uint8_t),
    ]


class ZW_CREDENTIAL_LEARN_CANCEL_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_CREDENTIAL_LEARN_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('credentialLearnStatus', uint8_t),
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('credentialType', uint8_t),
        ('credentialSlot1', uint8_t),
        ('credentialSlot2', uint8_t),
        ('credentialLearnStepsRemaining', uint8_t),
    ]


class ZW_USER_CREDENTIAL_ASSOCIATION_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('credentialType', uint8_t),
        ('sourceCredentialSlot1', uint8_t),
        ('sourceCredentialSlot2', uint8_t),
        ('destinationUserUniqueIdentifier1', uint8_t),
        ('destinationUserUniqueIdentifier2', uint8_t),
        ('destinationCredentialSlot1', uint8_t),
        ('destinationCredentialSlot2', uint8_t),
    ]


class ZW_USER_CREDENTIAL_ASSOCIATION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('credentialType', uint8_t),
        ('sourceCredentialSlot1', uint8_t),
        ('sourceCredentialSlot2', uint8_t),
        ('destinationUserUniqueIdentifier1', uint8_t),
        ('destinationUserUniqueIdentifier2', uint8_t),
        ('destinationCredentialSlot1', uint8_t),
        ('destinationCredentialSlot2', uint8_t),
        ('userCredentialAssociationStatus', uint8_t),
    ]


class ZW_ALL_USERS_CHECKSUM_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ALL_USERS_CHECKSUM_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('allUsersChecksum1', uint8_t),
        ('allUsersChecksum2', uint8_t),
    ]


class ZW_USER_CHECKSUM_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
    ]


class ZW_USER_CHECKSUM_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('userUniqueIdentifier1', uint8_t),
        ('userUniqueIdentifier2', uint8_t),
        ('userChecksum1', uint8_t),
        ('userChecksum2', uint8_t),
    ]


class ZW_CREDENTIAL_CHECKSUM_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('credentialType', uint8_t)]


class ZW_CREDENTIAL_CHECKSUM_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('credentialType', uint8_t),
        ('credentialChecksum1', uint8_t),
        ('credentialChecksum2', uint8_t),
    ]


class ZW_ADMIN_PIN_CODE_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('adminCode1', uint8_t),
    ]


class ZW_ADMIN_PIN_CODE_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_ADMIN_PIN_CODE_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('adminCode1', uint8_t),
    ]

