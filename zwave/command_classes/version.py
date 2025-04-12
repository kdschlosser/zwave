# Version Command Class
# Management
# ==============================
COMMAND_CLASS_VERSION = 0x86

VERSION_VERSION = 0x01
# Version Get
VERSION_GET = 0x11
# Version Report
VERSION_REPORT = 0x12
# Version Command Class Get
VERSION_COMMAND_CLASS_GET = 0x13
# Version Command Class Report
VERSION_COMMAND_CLASS_REPORT = 0x14

VERSION_VERSION_V2 = 0x02
VERSION_COMMAND_CLASS_GET_V2 = 0x13
VERSION_COMMAND_CLASS_REPORT_V2 = 0x14
VERSION_GET_V2 = 0x11
VERSION_REPORT_V2 = 0x12

VERSION_VERSION_V3 = 0x03
VERSION_COMMAND_CLASS_GET_V3 = 0x13
VERSION_COMMAND_CLASS_REPORT_V3 = 0x14
VERSION_GET_V3 = 0x11
VERSION_REPORT_V3 = 0x12
# Version Capabilities Get
VERSION_CAPABILITIES_GET_V3 = 0x15
# Version Capabilities Report
VERSION_CAPABILITIES_REPORT_V3 = 0x16
# Version Z-Wave Software Get
VERSION_ZWAVE_SOFTWARE_GET_V3 = 0x17
# Version Z-Wave Software Report
VERSION_ZWAVE_SOFTWARE_REPORT_V3 = 0x18

# Values used for Version Capabilities Report command
VERSION_CAPABILITIES_REPORT_PROPERTIES1_VERSION_BIT_MASK_V3 = 0x01
VERSION_CAPABILITIES_REPORT_PROPERTIES1_COMMAND_CLASS_BIT_MASK_V3 = 0x02
VERSION_CAPABILITIES_REPORT_PROPERTIES1_Z_WAVE_SOFTWARE_BIT_MASK_V3 = 0x04
VERSION_CAPABILITIES_REPORT_PROPERTIES1_RESERVED1_MASK_V3 = 0xF8
VERSION_CAPABILITIES_REPORT_PROPERTIES1_RESERVED1_SHIFT_V3 = 0x03

class ZW_VERSION_COMMAND_CLASS_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('requestedCommandClass', uint8_t)]


class ZW_VERSION_COMMAND_CLASS_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('requestedCommandClass', uint8_t),
        ('commandClassVersion', uint8_t),
    ]


class ZW_VERSION_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_VERSION_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('zWaveLibraryType', uint8_t),
        ('zWaveProtocolVersion', uint8_t),
        ('zWaveProtocolSubVersion', uint8_t),
        ('applicationVersion', uint8_t),
        ('applicationSubVersion', uint8_t),
    ]


class ZW_VERSION_COMMAND_CLASS_GET_V2_FRAME(ZW_VERSION_COMMAND_CLASS_GET_FRAME):
    _fields_ = []


class ZW_VERSION_COMMAND_CLASS_REPORT_V2_FRAME(ZW_VERSION_COMMAND_CLASS_REPORT_FRAME):
    _fields_ = []


class ZW_VERSION_GET_V2_FRAME(ZW_VERSION_GET_FRAME):
    _fields_ = []


class VG_VERSION_REPORT_V2_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareVersion', uint8_t),
        ('firmwareSubVersion', uint8_t),
    ]


class ZW_VERSION_REPORT_V2_FRAME(ZW_VERSION_REPORT_FRAME):
    _fields_ = [
        ('firmware0Version', uint8_t),
        ('firmware0SubVersion', uint8_t),
        ('hardwareVersion', uint8_t),
        ('numberOfFirmwareTargets', uint8_t),
        ('variantgroup1', VG_VERSION_REPORT_V2_VG),
    ]


class ZW_VERSION_COMMAND_CLASS_GET_V3_FRAME(ZW_VERSION_COMMAND_CLASS_GET_V2_FRAME):
    _fields_ = []


class ZW_VERSION_COMMAND_CLASS_REPORT_V3_FRAME(ZW_VERSION_COMMAND_CLASS_REPORT_V2_FRAME):
    _fields_ = []


class ZW_VERSION_GET_V3_FRAME(ZW_VERSION_GET_V2_FRAME):
    _fields_ = []


class VG_VERSION_REPORT_V3_VG(ctypes.Structure):
    _fields_ = [
        ('firmwareVersion', uint8_t),
        ('firmwareSubVersion', uint8_t),
    ]


class ZW_VERSION_REPORT_V3_FRAME(ZW_VERSION_REPORT_V2_FRAME):
    _fields_ = []


class ZW_VERSION_CAPABILITIES_GET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_VERSION_CAPABILITIES_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [('properties1', uint8_t)]


class ZW_VERSION_ZWAVE_SOFTWARE_GET_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_VERSION_ZWAVE_SOFTWARE_REPORT_V3_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('sdkVersion1', uint8_t),
        ('sdkVersion2', uint8_t),
        ('sdkVersion3', uint8_t),
        ('applicationFrameworkApiVersion1', uint8_t),
        ('applicationFrameworkApiVersion2', uint8_t),
        ('applicationFrameworkApiVersion3', uint8_t),
        ('applicationFrameworkBuildNumber1', uint8_t),
        ('applicationFrameworkBuildNumber2', uint8_t),
        ('hostInterfaceVersion1', uint8_t),
        ('hostInterfaceVersion2', uint8_t),
        ('hostInterfaceVersion3', uint8_t),
        ('hostInterfaceBuildNumber1', uint8_t),
        ('hostInterfaceBuildNumber2', uint8_t),
        ('zWaveProtocolVersion1', uint8_t),
        ('zWaveProtocolVersion2', uint8_t),
        ('zWaveProtocolVersion3', uint8_t),
        ('zWaveProtocolBuildNumber1', uint8_t),
        ('zWaveProtocolBuildNumber2', uint8_t),
        ('applicationVersion1', uint8_t),
        ('applicationVersion2', uint8_t),
        ('applicationVersion3', uint8_t),
        ('applicationBuildNumber1', uint8_t),
        ('applicationBuildNumber2', uint8_t),
    ]

