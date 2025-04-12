# # ********** Basic Device Class identifiers *************

import enum as _enum
from . import _utils


class BASIC_TYPE(_utils.ENUM):
    UNKNOWN = 0x00
    CONTROLLER = 0x01
    STATIC_CONTROLLER = 0x02
    END_NODE = 0x03
    ROUTING_END_NODE = 0x04


class _GENERIC_ENUM(_utils.ENUM):
    _replace = _enum.nonmember(('PC', 'TV', 'IR', 'ZIP', 'AV', ' NET', 'HRV'))
    _zwave_plus_v1 = _enum.nonmember(())
    _zwave_plus_v2 = _enum.nonmember(())


class GENERIC_TYPE(_GENERIC_ENUM):

    @_utils.member
    class UNKNOWN(_GENERIC_ENUM):
        id = _enum.nonmember(0x00)

        UNKNOWN = 0x00

    @_utils.member
    class CONTROLLER(_GENERIC_ENUM):
        id = _enum.nonmember(0x01)
        _zwave_plus_v1 = _enum.nonmember((0x01, 0x04, 0x06))
        _zwave_plus_v2 = _enum.nonmember((0x00,))

        UNKNOWN = 0x00
        PORTABLE_REMOTE = 0x01
        PORTABLE_SCENE = 0x02
        PORTABLE_INSTALLER_TOOL = 0x03
        REMOTE_AV = 0x04
        REMOTE_SIMPLE = 0x06

    @_utils.member
    class STATIC_CONTROLLER(_GENERIC_ENUM):
        id = _enum.nonmember(0x02)
        _zwave_plus_v1 = _enum.nonmember((0x01, 0x04, 0x05, 0x06, 0x07))
        _zwave_plus_v2 = _enum.nonmember((0x07,))

        UNKNOWN = 0x00
        PC = 0x01
        SCENE = 0x02
        INSTALLER_TOOL = 0x03
        SET_TOP_BOX = 0x04
        SUB_SYSTEM = 0x05
        TV = 0x06
        GATEWAY = 0x07

    @_utils.member
    class AV_CONTROL_POINT(_GENERIC_ENUM):
        id = _enum.nonmember(0x03)
        _zwave_plus_v1 = _enum.nonmember((0x00, 0x01))
        _zwave_plus_v2 = _enum.nonmember((0x00, 0x01))

        UNKNOWN = 0x00
        SOUND_SWITCH = 0x01
        SATELLITE_RECEIVER = 0x04
        SATELLITE_RECEIVER_V2 = 0x11
        DOORBELL = 0x12

    @_utils.member
    class DISPLAY(_GENERIC_ENUM):
        id = _enum.nonmember(0x04)
        _zwave_plus_v1 = _enum.nonmember((0x01,))
        _zwave_plus_v2 = _enum.nonmember(())

        UNKNOWN = 0x00
        SIMPLE = 0x01

    @_utils.member
    class NETWORK_EXTENDER(_GENERIC_ENUM):
        id = _enum.nonmember(0x05)

        UNKNOWN = 0x00
        SECURE = 0x01

    @_utils.member
    class APPLIANCE(_GENERIC_ENUM):
        id = _enum.nonmember(0x06)

        UNKNOWN = 0x00
        GENERAL = 0x01
        KITCHEN = 0x02
        LAUNDRY = 0x03

    @_utils.member
    class NOTIFICATION(_GENERIC_ENUM):
        id = _enum.nonmember(0x07)

        _zwave_plus_v1 = _enum.nonmember((0x01,))
        _zwave_plus_v2 = _enum.nonmember((0x01,))

        UNKNOWN = 0x00
        SENSOR = 0x01

    @_utils.member
    class THERMOSTAT(_GENERIC_ENUM):
        id = _enum.nonmember(0x08)

        _zwave_plus_v1 = _enum.nonmember((0x05, 0x06))
        _zwave_plus_v2 = _enum.nonmember((0x06, ))

        UNKNOWN = 0x00
        HEATING = 0x01
        GENERAL = 0x02
        SETBACK_SCHEDULE = 0x03
        SETPOINT = 0x04
        SETBACK = 0x05
        GENERAL_V2 = 0x06

    @_utils.member
    class WINDOW_COVERING(_GENERIC_ENUM):
        id = _enum.nonmember(0x09)

        UNKNOWN = 0x00
        SIMPLE = 0x01

    @_utils.member
    class REPEATER(_GENERIC_ENUM):
        id = _enum.nonmember(0x0F)

        _zwave_plus_v1 = _enum.nonmember((0x01, 0x03))
        _zwave_plus_v2 = _enum.nonmember((0x01, 0x03))

        UNKNOWN = 0x00
        SLAVE = 0x01
        VIRTUAL = 0x02
        IR = 0x03

    @_utils.member
    class SWITCH_BINARY(_GENERIC_ENUM):
        id = _enum.nonmember(0x10)
        _zwave_plus_v1 = _enum.nonmember((0x01, 0x02, 0x04, 0x05, 0x06, 0x07))
        _zwave_plus_v2 = _enum.nonmember((0x00, 0x02, ))

        UNKNOWN = 0x00
        POWER = 0x01
        SCENE = 0x03
        STRIP = 0x04
        SIREN = 0x05
        VALVE = 0x06
        COLOR_TUNABLE = 0x02
        IRRIGATION = 0x07

    @_utils.member
    class SWITCH_MULTILEVEL(_GENERIC_ENUM):
        id = _enum.nonmember(0x11)
        _zwave_plus_v1 = _enum.nonmember((0x01, 0x02, 0x05, 0x06, 0x07, 0x08))
        _zwave_plus_v2 = _enum.nonmember((0x00, 0x02, 0x05, 0x06, 0x07,))

        UNKNOWN = 0x00
        CLASS_A_MOTOR = 0x05
        CLASS_B_MOTOR = 0x06
        CLASS_C_MOTOR = 0x07
        MULTIPOSITION_MOTOR = 0x03
        POWER = 0x01
        SCENE = 0x04
        FAN = 0x08
        COLOR_TUNABLE = 0x02

    @_utils.member
    class SWITCH_REMOTE(_GENERIC_ENUM):
        id = _enum.nonmember(0x12)

        UNKNOWN = 0x00
        BINARY = 0x01
        MULTILEVEL = 0x02
        TOGGLE_BINARY = 0x03
        TOGGLE_MULTILEVEL = 0x04

    @_utils.member
    class SWITCH_TOGGLE(_GENERIC_ENUM):
        id = _enum.nonmember(0x13)

        UNKNOWN = 0x00
        BINARY = 0x01
        MULTILEVEL = 0x02

    @_utils.member
    class ZIP_NODE(_GENERIC_ENUM):
        id = _enum.nonmember(0x15)

        UNKNOWN = 0x00
        ADVANCED = 0x02
        TUN = 0x01

    @_utils.member
    class VENTILATION(_GENERIC_ENUM):
        id = _enum.nonmember(0x16)

        UNKNOWN = 0x00
        RESIDENTIAL_HRV = 0x01

    @_utils.member
    class SECURITY_PANEL(_GENERIC_ENUM):
        id = _enum.nonmember(0x17)

        UNKNOWN = 0x00
        ZONED = 0x01

    @_utils.member
    class WALL_CONTROLLER(_GENERIC_ENUM):
        id = _enum.nonmember(0x18)

        _zwave_plus_v1 = _enum.nonmember((0x01,))
        _zwave_plus_v2 = _enum.nonmember((0x00,))

        UNKNOWN = 0x00
        BASIC = 0x01

    @_utils.member
    class SENSOR_ALARM(_GENERIC_ENUM):
        id = _enum.nonmember(0xA1)

        UNKNOWN = 0x00
        BASIC_ROUTING = 0x01
        ROUTING = 0x02
        BASIC_ZENSOR_NET = 0x03
        ZENSOR_NET = 0x04
        ADVANCED_ZENSOR_NET = 0x05
        BASIC_ROUTING_SMOKE = 0x06
        ROUTING_SMOKE = 0x07
        BASIC_ZENSOR_NET_SMOKE = 0x08
        ZENSOR_NET_SMOKE = 0x09
        ADVANCED_ZENSOR_NET_SMOKE = 0x0A
        ALARM = 0x0B

    @_utils.member
    class SENSOR_BINARY(_GENERIC_ENUM):
        id = _enum.nonmember(0x20)

        UNKNOWN = 0x00
        ROUTING = 0x01

    @_utils.member
    class SENSOR_MULTILEVEL(_GENERIC_ENUM):
        id = _enum.nonmember(0x21)

        _zwave_plus_v1 = _enum.nonmember((0x01,))
        _zwave_plus_v2 = _enum.nonmember((0x01,))

        UNKNOWN = 0x00
        ROUTING = 0x01
        CHIMNEY_FAN = 0x02

    @_utils.member
    class METER_PULSE(_GENERIC_ENUM):
        id = _enum.nonmember(0x30)

        UNKNOWN = 0x00

    @_utils.member
    class METER(_GENERIC_ENUM):
        id = _enum.nonmember(0x31)

        _zwave_plus_v1 = _enum.nonmember((0x01, 0x03))
        _zwave_plus_v2 = _enum.nonmember((0x00,))

        UNKNOWN = 0x00
        SIMPLE = 0x01
        ADVANCED_ENERGY_CONTROL = 0x02
        SIMPLE_WHOLE_HOME = 0x03

    @_utils.member
    class ENTRY_CONTROL(_GENERIC_ENUM):
        id = _enum.nonmember(0x40)

        _zwave_plus_v1 = _enum.nonmember((0x03, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B))
        _zwave_plus_v2 = _enum.nonmember((0x01, 0x06, 0x08, 0x09, 0x0B))

        UNKNOWN = 0x00
        DOOR_LOCK = 0x01
        ADVANCED_DOOR_LOCK = 0x02
        SECURE_KEYPAD_DOOR_LOCK = 0x03
        SECURE_KEYPAD_DOOR_LOCK_DEADBOLT = 0x04
        SECURE_DOOR = 0x05
        SECURE_GATE = 0x06
        SECURE_BARRIER_ADDON = 0x07
        SECURE_BARRIER_OPEN_ONLY = 0x08
        SECURE_BARRIER_CLOSE_ONLY = 0x09
        SECURE_LOCKBOX = 0x0A
        SECURE_KEYPAD = 0x0B

    @_utils.member
    class SEMI_INTEROPERABLE(_GENERIC_ENUM):
        id = _enum.nonmember(0x50)

        UNKNOWN = 0x00
        ENERGY_PRODUCTION = 0x01

    @_utils.member
    class NON_INTEROPERABLE(_GENERIC_ENUM):
        id = _enum.nonmember(0xFF)

        UNKNOWN = 0x00


from typing import Union


SPECIFIC_TYPES = Union[
    GENERIC_TYPE.UNKNOWN,
    GENERIC_TYPE.CONTROLLER,
    GENERIC_TYPE.STATIC_CONTROLLER,
    GENERIC_TYPE.AV_CONTROL_POINT,
    GENERIC_TYPE.DISPLAY,
    GENERIC_TYPE.NETWORK_EXTENDER,
    GENERIC_TYPE.APPLIANCE,
    GENERIC_TYPE.NOTIFICATION,
    GENERIC_TYPE.THERMOSTAT,
    GENERIC_TYPE.WINDOW_COVERING,
    GENERIC_TYPE.REPEATER,
    GENERIC_TYPE.SWITCH_BINARY,
    GENERIC_TYPE.SWITCH_MULTILEVEL,
    GENERIC_TYPE.SWITCH_REMOTE,
    GENERIC_TYPE.SWITCH_TOGGLE,
    GENERIC_TYPE.ZIP_NODE,
    GENERIC_TYPE.VENTILATION,
    GENERIC_TYPE.SECURITY_PANEL,
    GENERIC_TYPE.WALL_CONTROLLER,
    GENERIC_TYPE.SENSOR_ALARM,
    GENERIC_TYPE.SENSOR_BINARY,
    GENERIC_TYPE.SENSOR_MULTILEVEL,
    GENERIC_TYPE.METER_PULSE,
    GENERIC_TYPE.METER,
    GENERIC_TYPE.ENTRY_CONTROL,
    GENERIC_TYPE.SEMI_INTEROPERABLE,
    GENERIC_TYPE.NON_INTEROPERABLE,
]

del Union
