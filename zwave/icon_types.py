import enum as _enum
from . import _utils


class _ICON_ENUM(_utils.ENUM):
    _replace = _enum.nonmember(('RFID', 'CO2 ', 'CO '))

   
class ICON_TYPE(_ICON_ENUM):

    @_utils.member
    class UNASSIGNED(_ICON_ENUM):
        id = _enum.nonmember(0x00)

        GENERIC = 0x0000

    @_utils.member
    class CENTRAL_CONTROLLER(_ICON_ENUM):
        id = _enum.nonmember(0x01)

        GENERIC = 0x0100

    @_utils.member
    class DISPLAY_SIMPLE(_ICON_ENUM):
        id = _enum.nonmember(0x02)

        GENERIC = 0x0200

    @_utils.member
    class DOOR_LOCK_KEYPAD(_ICON_ENUM):
        id = _enum.nonmember(0x03)

        GENERIC = 0x0300

    @_utils.member
    class FAN_SWITCH(_ICON_ENUM):
        id = _enum.nonmember(0x04)

        GENERIC = 0x0500

    @_utils.member
    class GENERIC_GATEWAY(_ICON_ENUM):
        id = _enum.nonmember(0x05)

        GENERIC = 0x0500

    @_utils.member
    class LIGHT_DIMMER_SWITCH(_ICON_ENUM):
        id = _enum.nonmember(0x06)

        GENERIC = 0x0600
        PLUGIN = 0x0601
        WALL_OUTLET = 0x0602
        CEILING_OUTLET = 0x0603
        WALL_LAMP = 0x0604
        LAMP_POST_HIGH = 0x0605
        LAMP_POST_LOW = 0x0606

    @_utils.member
    class ON_OFF_POWER_SWITCH(_ICON_ENUM):
        id = _enum.nonmember(0x07)

        GENERIC = 0x0700
        PLUGIN = 0x0701
        WALL_OUTLET = 0x0702
        CEILING_OUTLET = 0x0703
        WALL_LAMP = 0x0704
        LAMP_POST_HIGH = 0x0705
        LAMP_POST_LOW = 0x0706

    @_utils.member
    class POWER_STRIP(_ICON_ENUM):
        id = _enum.nonmember(0x08)

        GENERIC = 0x0800
        INDIVIDUAL_OUTLET = 0x08FF

    @_utils.member
    class REMOTE_CONTROL_AV(_ICON_ENUM):
        id = _enum.nonmember(0x09)

        GENERIC = 0x0900

    @_utils.member
    class REMOTE_CONTROL_MULTI_PURPOSE(_ICON_ENUM):
        id = _enum.nonmember(0x0A)

        GENERIC = 0x0A00

    @_utils.member
    class REMOTE_CONTROL_SIMPLE(_ICON_ENUM):
        id = _enum.nonmember(0x0B)

        GENERIC = 0x0B00
        KEYFOB = 0x0B01

    @_utils.member
    class NOTIFICATION(_ICON_ENUM):
        id = _enum.nonmember(0x0C)

        GENERIC = 0x0C00
        SMOKE_ALARM = 0x0C01
        CO_ALARM = 0x0C02
        CO2_ALARM = 0x0C03
        HEAT_ALARM = 0x0C04
        WATER_ALARM = 0x0C05
        ACCESS_CONTROL = 0x0C06
        HOME_SECURITY = 0x0C07
        POWER_MANAGEMENT = 0x0C08
        SYSTEM = 0x0C09
        EMERGENCY_ALARM = 0x0C0A
        CLOCK = 0x0C0B
        APPLIANCE = 0x0C0C
        HOME_HEALTH = 0x0C0D
        SIREN = 0x0C0E
        WATER_VALVE = 0x0C0F
        WEATHER_ALARM = 0x0C10
        IRRIGATION = 0x0C11
        GAS_ALARM = 0x0C12
        MULTIDEVICE = 0x0CFF

    @_utils.member
    class SENSOR_MULTILEVEL(_ICON_ENUM):
        id = _enum.nonmember(0x0D)

        GENERIC = 0x0D00
        AIR_TEMPERATURE = 0x0D01
        GENERAL_PURPOSE_VALUE = 0x0D02
        LUMINANCE = 0x0D03
        POWER = 0x0D04
        HUMIDITY = 0x0D05
        VELOCITY = 0x0D06
        DIRECTION = 0x0D07
        ATMOSPHERIC_PRESSURE = 0x0D08
        BAROMETRIC_PRESSURE = 0x0D09
        SOLOR_RADIATION = 0x0D0A
        DEW_POINT = 0x0D0B
        RAIN_RATE = 0x0D0C
        TIDE_LEVEL = 0x0D0D
        WEIGHT = 0x0D0E
        VOLTAGE = 0x0D0F
        CURRENT = 0x0D10
        CO2_LEVEL = 0x0D11
        AIR_FLOW = 0x0D12
        TANK_CAPACITY = 0x0D13
        DISTANCE = 0x0D14
        ANGLE_POSITION = 0x0D15
        ROTATION = 0x0D16
        WATER_TEMPERATURE = 0x0D17
        SOIL_TEMPERATURE = 0x0D18
        SEISMIC_INTENSITY = 0x0D19
        SEISMIC_MAGNITUDE = 0x0D1A
        ULTRAVIOLET = 0x0D1B
        ELECTRICAL_RESISTIVITY = 0x0D1C
        ELECTRICAL_CONDUCTIVITY = 0x0D1D
        LOUDNESS = 0x0D1E
        MOISTURE = 0x0D1F
        FREQUENCY = 0x0D20
        TIME = 0x0D21
        TARGET_TEMPERATURE = 0x0D22
        MULTIDEVICE = 0x0DFF

    @_utils.member
    class SET_TOP_BOX(_ICON_ENUM):
        id = _enum.nonmember(0x0E)

        GENERIC = 0x0E00

    @_utils.member
    class SIREN(_ICON_ENUM):
        id = _enum.nonmember(0x0F)

        GENERIC = 0x0F00

    @_utils.member
    class SUB_ENERGY_METER(_ICON_ENUM):
        id = _enum.nonmember(0x10)

        GENERIC = 0x1000

    @_utils.member
    class SUB_SYSTEM_CONTROLLER(_ICON_ENUM):
        id = _enum.nonmember(0x11)

        GENERIC = 0x1100

    @_utils.member
    class THERMOSTAT(_ICON_ENUM):
        id = _enum.nonmember(0x12)

        GENERIC = 0x1200
        LINE_VOLTAGE = 0x1201
        SETBACK = 0x1202

    @_utils.member
    class THERMOSTAT_SETBACK(_ICON_ENUM):
        id = _enum.nonmember(0x13)

        GENERIC = 0x1300

    @_utils.member
    class TV(_ICON_ENUM):
        id = _enum.nonmember(0x14)

        GENERIC = 0x1400

    @_utils.member
    class VALVE_OPEN_CLOSE(_ICON_ENUM):
        id = _enum.nonmember(0x15)

        GENERIC = 0x1500

    @_utils.member
    class WALL_CONTROLLER(_ICON_ENUM):
        id = _enum.nonmember(0x16)

        GENERIC = 0x1600

    @_utils.member
    class WHOLE_HOME_METER_SIMPLE(_ICON_ENUM):
        id = _enum.nonmember(0x17)

        GENERIC = 0x1700

    @_utils.member
    class WINDOW_COVERING_NO_POSITION_ENDPOINT(_ICON_ENUM):
        id = _enum.nonmember(0x18)

        GENERIC = 0x1800

    @_utils.member
    class WINDOW_COVERING_ENDPOINT_AWARE(_ICON_ENUM):
        id = _enum.nonmember(0x19)

        GENERIC = 0x1900

    @_utils.member
    class WINDOW_COVERING_POSITION_ENDPOINT_AWARE(_ICON_ENUM):
        id = _enum.nonmember(0x1A)

        GENERIC = 0x1A00

    @_utils.member
    class DIMMER_WALL_SWITCH(_ICON_ENUM):
        id = _enum.nonmember(0x1C)

        GENERIC = 0x1C00
        ONE_BUTTON = 0x1C01
        TWO_BUTTONS = 0x1C02
        THREE_BUTTONS = 0x1C03
        FOUR_BUTTONS = 0x1C04
        ONE_ROTARY = 0x1CF1

    @_utils.member
    class ON_OFF_WALL_SWITCH(_ICON_ENUM):
        id = _enum.nonmember(0x1D)

        GENERIC = 0x1D00
        ONE_BUTTON = 0x1D01
        TWO_BUTTONS = 0x1D02
        THREE_BUTTONS = 0x1D03
        FOUR_BUTTONS = 0x1D04
        DOOR_BELL = 0x1DE1
        ONE_ROTARY = 0x1DF1

    @_utils.member
    class REPEATER(_ICON_ENUM):
        id = _enum.nonmember(0x1B)

        GENERIC = 0x1B00

    @_utils.member
    class BARRIER(_ICON_ENUM):
        id = _enum.nonmember(0x1E)

        GENERIC = 0x1E00

    @_utils.member
    class IRRIGATION(_ICON_ENUM):
        id = _enum.nonmember(0x1F)

        GENERIC = 0x1F00

    @_utils.member
    class ENTRY_CONTROL(_ICON_ENUM):
        id = _enum.nonmember(0x20)

        GENERIC = 0x2000
        KEYPAD_NUMERIC = 0x2001
        RFID_TAG_READER_NO_BUTTON = 0x2002
