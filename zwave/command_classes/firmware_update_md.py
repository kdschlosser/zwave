# Firmware Update Meta Data Command Class
# Management
# ==============================
COMMAND_CLASS_FIRMWARE_UPDATE_MD = 0x7A

FIRMWARE_UPDATE_MD_VERSION = 0x01
# Firmware Meta Data Get
FIRMWARE_MD_GET = 0x01
# Firmware Meta Data Report
FIRMWARE_MD_REPORT = 0x02
# Firmware Update Meta Data Request Get
FIRMWARE_UPDATE_MD_REQUEST_GET = 0x03
# Firmware Update Meta Data Request Report
FIRMWARE_UPDATE_MD_REQUEST_REPORT = 0x04
# Firmware Update Meta Data Get
FIRMWARE_UPDATE_MD_GET = 0x05
# Firmware Update Meta Data Report
FIRMWARE_UPDATE_MD_REPORT = 0x06
# Firmware Update Meta Data Status Report
FIRMWARE_UPDATE_MD_STATUS_REPORT = 0x07

# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK = 0x80
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V2 = 0x02
FIRMWARE_MD_GET_V2 = 0x01
FIRMWARE_MD_REPORT_V2 = 0x02
FIRMWARE_UPDATE_MD_GET_V2 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V2 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V2 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V2 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V2 = 0x07

# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V2 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V2 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V2 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V2 = 0x80
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V2 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V2 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V2 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V2 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V2 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V2 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V3 = 0x03
FIRMWARE_MD_GET_V3 = 0x01
FIRMWARE_MD_REPORT_V3 = 0x02
FIRMWARE_UPDATE_MD_GET_V3 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V3 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V3 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V3 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V3 = 0x07
# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V3 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V3 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V3 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V3 = 0x80
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V3 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V3 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V3 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V3 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V3 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V3 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V3 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V3 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V3 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V4 = 0x04
FIRMWARE_MD_GET_V4 = 0x01
FIRMWARE_MD_REPORT_V4 = 0x02
FIRMWARE_UPDATE_MD_GET_V4 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V4 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V4 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V4 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V4 = 0x07
# Firmware Update Activation Set
FIRMWARE_UPDATE_ACTIVATION_SET_V4 = 0x08
# Firmware Update Activation Report
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V4 = 0x09

# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V4 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V4 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V4 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V4 = 0x80
# Values used for Firmware Update Md Request Get command
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_ACTIVATION_BIT_MASK_V4 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_MASK_V4 = 0xFE
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_SHIFT_V4 = 0x01
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V4 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V4 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V4 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V4 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V4 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V4 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V4 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_MANUFACTURER_ID_V4 = 0x02
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_ID_V4 = 0x03
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_TARGET_V4 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_INFORMATION_V4 = 0x05
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_FORMAT_V4 = 0x06
FIRMWARE_UPDATE_MD_STATUS_REPORT_INSUFFICIENT_MEMORY_V4 = 0x07
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_WAITING_FOR_ACTIVATION_V4 = 0xFD
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V4 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V4 = 0xFF
# Values used for Firmware Update Activation Status Report command
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_INVALID_COMBINATION_V4 = 0x00
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_ERROR_ACTIVATING_THE_FIRMWARE_V4 = 0x01
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_FIRMWARE_UPDATE_COMPLETED_SUCCESSFULLY_V4 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V5 = 0x05
FIRMWARE_MD_GET_V5 = 0x01
FIRMWARE_MD_REPORT_V5 = 0x02
FIRMWARE_UPDATE_MD_GET_V5 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V5 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V5 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V5 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V5 = 0x07
FIRMWARE_UPDATE_ACTIVATION_SET_V5 = 0x08
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V5 = 0x09
# Firmware Update Meta Data Prepare Get
FIRMWARE_UPDATE_MD_PREPARE_GET_V5 = 0x0A
# Firmware Update Meta Data Prepare Report
FIRMWARE_UPDATE_MD_PREPARE_REPORT_V5 = 0x0B

# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V5 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V5 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V5 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V5 = 0x80
# Values used for Firmware Update Md Request Get command
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_ACTIVATION_BIT_MASK_V5 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_MASK_V5 = 0xFE
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_SHIFT_V5 = 0x01
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V5 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V5 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V5 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V5 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_HARDWARE_VERSION_V5 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V5 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V5 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V5 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_MANUFACTURER_ID_V5 = 0x02
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_ID_V5 = 0x03
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_TARGET_V5 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_INFORMATION_V5 = 0x05
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_FORMAT_V5 = 0x06
FIRMWARE_UPDATE_MD_STATUS_REPORT_INSUFFICIENT_MEMORY_V5 = 0x07
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_HARDWARE_VERSION_V5 = 0x08
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_WAITING_FOR_ACTIVATION_V5 = 0xFD
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V5 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V5 = 0xFF
# Values used for Firmware Update Activation Status Report command
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_INVALID_COMBINATION_V5 = 0x00
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_ERROR_ACTIVATING_THE_FIRMWARE_V5 = 0x01
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_FIRMWARE_UPDATE_COMPLETED_SUCCESSFULLY_V5 = 0xFF
# Values used for Firmware Update Md Prepare Report command
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_COMBINATION_V5 = 0x00
FIRMWARE_UPDATE_MD_PREPARE_REPORT_REQUIRES_AUTHENTICATION_V5 = 0x01
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_FRAGMENT_SIZE_V5 = 0x02
FIRMWARE_UPDATE_MD_PREPARE_REPORT_NOT_DOWNLOADABLE_V5 = 0x03
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_HARDWARE_VERSION_V5 = 0x04
FIRMWARE_UPDATE_MD_PREPARE_REPORT_VALID_COMBINATION_V5 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V6 = 0x06
FIRMWARE_MD_GET_V6 = 0x01
FIRMWARE_MD_REPORT_V6 = 0x02
FIRMWARE_UPDATE_MD_GET_V6 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V6 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V6 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V6 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V6 = 0x07
FIRMWARE_UPDATE_ACTIVATION_SET_V6 = 0x08
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V6 = 0x09
FIRMWARE_UPDATE_MD_PREPARE_GET_V6 = 0x0A
FIRMWARE_UPDATE_MD_PREPARE_REPORT_V6 = 0x0B
# Values used for Firmware Md Report command
FIRMWARE_MD_REPORT_PROPERTIES1_CC_BIT_MASK_V6 = 0x01
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_MASK_V6 = 0xFE
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_SHIFT_V6 = 0x01
# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V6 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V6 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V6 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V6 = 0x80
# Values used for Firmware Update Md Request Get command
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_ACTIVATION_BIT_MASK_V6 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_MASK_V6 = 0xFE
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_SHIFT_V6 = 0x01
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V6 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V6 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V6 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V6 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_HARDWARE_VERSION_V6 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_REPORT_ANOTHER_FIRMWARE_IMAGE_V6 = 0x05
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INSUFFICIENT_BATTERY_LEVEL_V6 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V6 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V6 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V6 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_MANUFACTURER_ID_V6 = 0x02
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_ID_V6 = 0x03
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_TARGET_V6 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_INFORMATION_V6 = 0x05
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_FORMAT_V6 = 0x06
FIRMWARE_UPDATE_MD_STATUS_REPORT_INSUFFICIENT_MEMORY_V6 = 0x07
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_HARDWARE_VERSION_V6 = 0x08
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_WAITING_FOR_ACTIVATION_V6 = 0xFD
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V6 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V6 = 0xFF
# Values used for Firmware Update Activation Status Report command
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_INVALID_COMBINATION_V6 = 0x00
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_ERROR_ACTIVATING_THE_FIRMWARE_V6 = 0x01
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_FIRMWARE_UPDATE_COMPLETED_SUCCESSFULLY_V6 = 0xFF
# Values used for Firmware Update Md Prepare Report command
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_COMBINATION_V6 = 0x00
FIRMWARE_UPDATE_MD_PREPARE_REPORT_REQUIRES_AUTHENTICATION_V6 = 0x01
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_FRAGMENT_SIZE_V6 = 0x02
FIRMWARE_UPDATE_MD_PREPARE_REPORT_NOT_DOWNLOADABLE_V6 = 0x03
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_HARDWARE_VERSION_V6 = 0x04
FIRMWARE_UPDATE_MD_PREPARE_REPORT_VALID_COMBINATION_V6 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V7 = 0x07
FIRMWARE_MD_GET_V7 = 0x01
FIRMWARE_MD_REPORT_V7 = 0x02
FIRMWARE_UPDATE_MD_GET_V7 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V7 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V7 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V7 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V7 = 0x07
FIRMWARE_UPDATE_ACTIVATION_SET_V7 = 0x08
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V7 = 0x09
FIRMWARE_UPDATE_MD_PREPARE_GET_V7 = 0x0A
FIRMWARE_UPDATE_MD_PREPARE_REPORT_V7 = 0x0B
# Values used for Firmware Md Report command
FIRMWARE_MD_REPORT_PROPERTIES1_CC_BIT_MASK_V7 = 0x01
FIRMWARE_MD_REPORT_PROPERTIES1_ACTIVATION_BIT_MASK_V7 = 0x02
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_MASK_V7 = 0xFC
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_SHIFT_V7 = 0x02
# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V7 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_ZERO_BIT_MASK_V7 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V7 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V7 = 0x80
# Values used for Firmware Update Md Request Get command
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_ACTIVATION_BIT_MASK_V7 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_MASK_V7 = 0xFE
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_SHIFT_V7 = 0x01
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V7 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V7 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V7 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V7 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_HARDWARE_VERSION_V7 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_REPORT_ANOTHER_FIRMWARE_IMAGE_V7 = 0x05
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INSUFFICIENT_BATTERY_LEVEL_V7 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V7 = 0xFF
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V7 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V7 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_MANUFACTURER_ID_V7 = 0x02
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_ID_V7 = 0x03
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_TARGET_V7 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_INFORMATION_V7 = 0x05
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_FORMAT_V7 = 0x06
FIRMWARE_UPDATE_MD_STATUS_REPORT_INSUFFICIENT_MEMORY_V7 = 0x07
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_HARDWARE_VERSION_V7 = 0x08
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_WAITING_FOR_ACTIVATION_V7 = 0xFD
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V7 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V7 = 0xFF
# Values used for Firmware Update Activation Status Report command
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_INVALID_COMBINATION_V7 = 0x00
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_ERROR_ACTIVATING_THE_FIRMWARE_V7 = 0x01
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_FIRMWARE_UPDATE_COMPLETED_SUCCESSFULLY_V7 = 0xFF
# Values used for Firmware Update Md Prepare Report command
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_COMBINATION_V7 = 0x00
FIRMWARE_UPDATE_MD_PREPARE_REPORT_REQUIRES_AUTHENTICATION_V7 = 0x01
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_FRAGMENT_SIZE_V7 = 0x02
FIRMWARE_UPDATE_MD_PREPARE_REPORT_NOT_DOWNLOADABLE_V7 = 0x03
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_HARDWARE_VERSION_V7 = 0x04
FIRMWARE_UPDATE_MD_PREPARE_REPORT_VALID_COMBINATION_V7 = 0xFF

FIRMWARE_UPDATE_MD_VERSION_V8 = 0x08
FIRMWARE_MD_GET_V8 = 0x01
FIRMWARE_MD_REPORT_V8 = 0x02
FIRMWARE_UPDATE_MD_GET_V8 = 0x05
FIRMWARE_UPDATE_MD_REPORT_V8 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_GET_V8 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_V8 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_V8 = 0x07
FIRMWARE_UPDATE_ACTIVATION_SET_V8 = 0x08
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V8 = 0x09
FIRMWARE_UPDATE_MD_PREPARE_GET_V8 = 0x0A
FIRMWARE_UPDATE_MD_PREPARE_REPORT_V8 = 0x0B
# Values used for Firmware Md Report command
FIRMWARE_MD_REPORT_PROPERTIES1_CC_BIT_MASK_V8 = 0x01
FIRMWARE_MD_REPORT_PROPERTIES1_ACTIVATION_BIT_MASK_V8 = 0x02
FIRMWARE_MD_REPORT_PROPERTIES1_NON_SECURE_BIT_MASK_V8 = 0x04
FIRMWARE_MD_REPORT_PROPERTIES1_RESUME_BIT_MASK_V8 = 0x08
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_MASK_V8 = 0xF0
FIRMWARE_MD_REPORT_PROPERTIES1_RESERVED1_SHIFT_V8 = 0x04
# Values used for Firmware Update Md Get command
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_REPORT_NUMBER_1_MASK_V8 = 0x7F
FIRMWARE_UPDATE_MD_GET_PROPERTIES1_RES_BIT_MASK_V8 = 0x80
# Values used for Firmware Update Md Report command
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_REPORT_NUMBER_1_MASK_V8 = 0x7F
FIRMWARE_UPDATE_MD_REPORT_PROPERTIES1_LAST_BIT_MASK_V8 = 0x80
# Values used for Firmware Update Md Request Get command
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_ACTIVATION_BIT_MASK_V8 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_NON_SECURE_BIT_MASK_V8 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESUME_BIT_MASK_V8 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_MASK_V8 = 0xF8
FIRMWARE_UPDATE_MD_REQUEST_GET_PROPERTIES1_RESERVED_SHIFT_V8 = 0x03
# Values used for Firmware Update Md Request Report command
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_COMBINATION_V8 = 0x00
FIRMWARE_UPDATE_MD_REQUEST_REPORT_REQUIRES_AUTHENTICATION_V8 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_FRAGMENT_SIZE_V8 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_NOT_UPGRADABLE_V8 = 0x03
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INVALID_HARDWARE_VERSION_V8 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_REPORT_ANOTHER_FIRMWARE_IMAGE_V8 = 0x05
FIRMWARE_UPDATE_MD_REQUEST_REPORT_INSUFFICIENT_BATTERY_LEVEL_V8 = 0x06
FIRMWARE_UPDATE_MD_REQUEST_REPORT_VALID_COMBINATION_V8 = 0xFF
FIRMWARE_UPDATE_MD_REQUEST_REPORT_PROPERTIES1_RESERVED_BIT_MASK_V8 = 0x01
FIRMWARE_UPDATE_MD_REQUEST_REPORT_PROPERTIES1_NON_SECURE_BIT_MASK_V8 = 0x02
FIRMWARE_UPDATE_MD_REQUEST_REPORT_PROPERTIES1_RESUME_BIT_MASK_V8 = 0x04
FIRMWARE_UPDATE_MD_REQUEST_REPORT_PROPERTIES1_RESERVED1_MASK_V8 = 0xF8
FIRMWARE_UPDATE_MD_REQUEST_REPORT_PROPERTIES1_RESERVED1_SHIFT_V8 = 0x03
# Values used for Firmware Update Md Status Report command
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_WITHOUT_CHECKSUM_ERROR_V8 = 0x00
FIRMWARE_UPDATE_MD_STATUS_REPORT_UNABLE_TO_RECEIVE_V8 = 0x01
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_MANUFACTURER_ID_V8 = 0x02
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_ID_V8 = 0x03
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_FIRMWARE_TARGET_V8 = 0x04
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_INFORMATION_V8 = 0x05
FIRMWARE_UPDATE_MD_STATUS_REPORT_INVALID_FILE_HEADER_FORMAT_V8 = 0x06
FIRMWARE_UPDATE_MD_STATUS_REPORT_INSUFFICIENT_MEMORY_V8 = 0x07
FIRMWARE_UPDATE_MD_STATUS_REPORT_DOES_NOT_MATCH_THE_HARDWARE_VERSION_V8 = 0x08
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_WAITING_FOR_ACTIVATION_V8 = 0xFD
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_STORED_V8 = 0xFE
FIRMWARE_UPDATE_MD_STATUS_REPORT_SUCCESSFULLY_V8 = 0xFF
# Values used for Firmware Update Activation Status Report command
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_INVALID_COMBINATION_V8 = 0x00
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_ERROR_ACTIVATING_THE_FIRMWARE_V8 = 0x01
FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_FIRMWARE_UPDATE_COMPLETED_SUCCESSFULLY_V8 = 0xFF
# Values used for Firmware Update Md Prepare Report command
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_COMBINATION_V8 = 0x00
FIRMWARE_UPDATE_MD_PREPARE_REPORT_REQUIRES_AUTHENTICATION_V8 = 0x01
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_FRAGMENT_SIZE_V8 = 0x02
FIRMWARE_UPDATE_MD_PREPARE_REPORT_NOT_DOWNLOADABLE_V8 = 0x03
FIRMWARE_UPDATE_MD_PREPARE_REPORT_INVALID_HARDWARE_VERSION_V8 = 0x04
FIRMWARE_UPDATE_MD_PREPARE_REPORT_VALID_COMBINATION_V8 = 0xFF






class ZW_FIRMWARE_MD_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_FIRMWARE_MD_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('numberOfReports', uint8_t),
        ('properties1', uint8_t),
        ('reportNumber2', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('properties1', uint8_t),
        ('reportNumber2', uint8_t),
        ('data1', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('status', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('status', uint8_t)]


class ZW_FIRMWARE_MD_GET_V2_FRAME(ZW_FIRMWARE_MD_GET_FRAME):
    _fields_ = []


class ZW_FIRMWARE_MD_REPORT_V2_FRAME(ZW_FIRMWARE_MD_REPORT_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_GET_V2_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V2_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_FRAME):
    _fields_ = [
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V2_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V2_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V2_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_FRAME):
    _fields_ = []


class ZW_FIRMWARE_MD_GET_V3_FRAME(ZW_FIRMWARE_MD_GET_V2_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V3_FRAME(ZW_FIRMWARE_MD_REPORT_V2_FRAME):
    _fields_ = [
        ('firmware0Id1', uint8_t),
        ('firmware0Id2', uint8_t),
        ('firmware0Checksum1', uint8_t),
        ('firmware0Checksum2', uint8_t),
        ('firmwareUpgradable', uint8_t),
        ('numberOfFirmwareTargets', uint8_t),
        ('maxFragmentSize1', uint8_t),
        ('maxFragmentSize2', uint8_t),
        ('variantgroup1', VG_FIRMWARE_MD_REPORT_V3_VG),
    ]


class ZW_FIRMWARE_UPDATE_MD_GET_V3_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V2_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V3_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V2_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V3_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V2_FRAME):
    _fields_ = [
        ('firmwareTarget', uint8_t),
        ('fragmentSize1', uint8_t),
        ('fragmentSize2', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V3_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V2_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V3_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V2_FRAME):
    _fields_ = [
        ('waittime1', uint8_t),
        ('waittime2', uint8_t),
    ]


class ZW_FIRMWARE_MD_GET_V4_FRAME(ZW_FIRMWARE_MD_GET_V3_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V4_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V4_FRAME(ZW_FIRMWARE_MD_REPORT_V3_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_GET_V4_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V3_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V4_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V3_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V4_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V3_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V4_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V3_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V4_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V3_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
        ('firmwareTarget', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V4_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
        ('checksum1', uint8_t),
        ('checksum2', uint8_t),
        ('firmwareTarget', uint8_t),
        ('firmwareUpdateStatus', uint8_t),
    ]


class ZW_FIRMWARE_MD_GET_V5_FRAME(ZW_FIRMWARE_MD_GET_V4_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V5_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V5_FRAME(ZW_FIRMWARE_MD_REPORT_V4_FRAME):
    _fields_ = [('hardwareVersion', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_GET_V5_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V4_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V5_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V4_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V5_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V4_FRAME):
    _fields_ = [('hardwareVersion', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V5_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V4_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V5_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V4_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V5_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V4_FRAME):
    _fields_ = [('hardwareVersion', uint8_t)]


class ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V5_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V4_FRAME):
    _fields_ = [('hardwareVersion', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V5_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('manufacturerId1', uint8_t),
        ('manufacturerId2', uint8_t),
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
        ('firmwareTarget', uint8_t),
        ('fragmentSize1', uint8_t),
        ('fragmentSize2', uint8_t),
        ('hardwareVersion', uint8_t),
    ]


class ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V5_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('status', uint8_t),
        ('firmwareChecksum1', uint8_t),
        ('firmwareChecksum2', uint8_t),
    ]


class ZW_FIRMWARE_MD_GET_V6_FRAME(ZW_FIRMWARE_MD_GET_V5_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V6_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V6_FRAME(ZW_FIRMWARE_MD_REPORT_V5_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_GET_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V6_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V6_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V6_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V5_FRAME):
    _fields_ = []


class ZW_FIRMWARE_MD_GET_V7_FRAME(ZW_FIRMWARE_MD_GET_V6_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V7_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V7_FRAME(ZW_FIRMWARE_MD_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_GET_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V7_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V7_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V7_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V6_FRAME):
    _fields_ = []


class ZW_FIRMWARE_MD_GET_V8_FRAME(ZW_FIRMWARE_MD_GET_V7_FRAME):
    _fields_ = []


class VG_FIRMWARE_MD_REPORT_V8_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareId1', uint8_t),
        ('firmwareId2', uint8_t),
    ]


class ZW_FIRMWARE_MD_REPORT_V8_FRAME(ZW_FIRMWARE_MD_REPORT_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_GET_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_GET_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REPORT_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_REPORT_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_GET_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_REQUEST_REPORT_V7_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_STATUS_REPORT_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V8_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_SET_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V8_FRAME(ZW_FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_GET_V7_FRAME):
    _fields_ = []


class ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V8_FRAME(ZW_FIRMWARE_UPDATE_MD_PREPARE_REPORT_V7_FRAME):
    _fields_ = []





