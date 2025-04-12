# Demand Control Plan Configuration Command Class
# Application
# ==============================
COMMAND_CLASS_DCP_CONFIG = 0x3A

DCP_CONFIG_VERSION = 0x01
# DCP List Supported Get
DCP_LIST_SUPPORTED_GET = 0x01
# DCP List Supported report
DCP_LIST_SUPPORTED_REPORT = 0x02
# DCP List Set
DCP_LIST_SET = 0x03
# DCP List Remove
DCP_LIST_REMOVE = 0x04

# Values used for Dcp List Set command
DCP_LIST_SET_PROPERTIES1_NUMBER_OF_DC_MASK = 0x03
DCP_LIST_SET_PROPERTIES1_RESERVED_MASK = 0xFC
DCP_LIST_SET_PROPERTIES1_RESERVED_SHIFT = 0x02


class ZW_DCP_LIST_REMOVE_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
    ]


class VG_DCP_LIST_SET_VG(ctypes.Structure):
    _fields_ = [
        ('genericDeviceClass', uint8_t),
        ('specificDeviceClass', uint8_t),
    ]


class ZW_DCP_LIST_SET_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('year1', uint8_t),
        ('year2', uint8_t),
        ('month', uint8_t),
        ('day', uint8_t),
        ('hourLocalTime', uint8_t),
        ('minuteLocalTime', uint8_t),
        ('secondLocalTime', uint8_t),
        ('dcpRateId', uint8_t),
        ('properties1', uint8_t),
        ('variantgroup1', VG_DCP_LIST_SET_VG),
        ('startYear1', uint8_t),
        ('startYear2', uint8_t),
        ('startMonth', uint8_t),
        ('startDay', uint8_t),
        ('startHourLocalTime', uint8_t),
        ('startMinuteLocalTime', uint8_t),
        ('startSecondLocalTime', uint8_t),
        ('durationHourTime', uint8_t),
        ('durationMinuteTime', uint8_t),
        ('durationSecondTime', uint8_t),
        ('eventPriority', uint8_t),
        ('loadShedding', uint8_t),
        ('startAssociationGroup', uint8_t),
        ('stopAssociationGroup', uint8_t),
        ('randomizationInterval', uint8_t),
    ]


class ZW_DCP_LIST_SUPPORTED_GET_FRAME(ZW_COMMON_FRAME):
    _fields_ = []


class ZW_DCP_LIST_SUPPORTED_REPORT_FRAME(ZW_COMMON_FRAME):
    _fields_ = [
        ('dcpListSize', uint8_t),
        ('freeDcpListEntries', uint8_t),
    ]

