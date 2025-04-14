import enum


# This is to override the output when wrapping them in str()
class _EnumMeta(enum.EnumType):

    def __str__(cls):
        return cls.__qualname__


# this is to override the enum container classes when wrapping them in str()
class _HostMeta(type):

    def __str__(cls):
        return cls.__qualname__


# base class for enum container classes
class HOST_CLASS(_HostMeta):
    pass


# base class for enum classes
# this class provides the "label" property which provides
# user friendly text that can be used in a UI
# it also provides the fully qualified name when wrapping in in str()
class HOST_ENUM(enum.Enum, metaclass=_EnumMeta):

    @staticmethod
    def _name_to_string(name: str) -> str:
        res = ''
        last_char = ''

        for char in name:
            res += last_char

            if last_char and not last_char.isupper() and char.isupper():
                res += ' '

            last_char = char

        res += last_char
        return res

    @property
    def label(self):
        return self._name_to_string(self._name_)

    def __str__(self):
        mod_name = self.__class__.__module__.split('.')[-1]

        return f'{mod_name}.{self.__class__.__qualname__}.{self._name_}'


class RXStatus(HOST_FLAG):
    LowPower = 0x02
    BroadcastAddressing = 0x08
    MulticastAddressing = 0x10
    ExploreNPDU = 0x20
    ForeignFrame = 0x40
    ForeignHomeID = 0x80


class TXStatus(HOST_ENUM):
    OK = 0x00
    NoACK = 0x01
    Fail = 0x02
    RoutingNotIdle = 0x03
    NoRoute = 0x04
    Verified = 0x05


class ResponseStatus(HOST_ENUM):
    DoNotSendCallbackData = 0x00
    SendCallbackData = 0x01


class CommandStatus(HOST_ENUM):
    Fail = 0x00
    Success = 0x01


class BasicDeviceClass(HOST_ENUM):
    Controller = 0x01
    StaticController = 0x02
    EndNode = 0x03
    RoutingEndNode = 0x04


class TXOption(HOST_FLAG):
    ACK = 0x01
    LowPower = 0x02
    AutoRoute = 0x04
    NoRoute = 0x10
    Explore = 0x20


class RFRegion(HOST_ENUM):
    Europe = 0x00
    UnitedStates = 0x01
    Australia = 0x02
    NewZealand = Australia
    HongKong = 0x03
    India = 0x05
    Israel = 0x06
    Russia = 0x07
    China = 0x08
    UnitedStatesLR = 0x09
    Japan = 0x20
    Korea = 0x21
    Undefined = 0xFE
    Default = 0xFF


class DeviceOption(HOST_ENUM):
    NotListening = 0x00
    Listening = 0x80


class RouteDataRate(HOST_ENUM):
    Speed9600bps = 0x01
    Speed40kbps = 0x02
    Speed100kbps = 0x03
    Speed100kbpsLR = 0x04


class PrimaryControllerMode(HOST_ENUM):
    AddStart = 0x01
    AddStop = 0x05
    AddStopFailure = 0x06


class AddNodeToNetworkStatus(HOST_ENUM):
    InclusionStarted = 0x01
    NodeFound = 0x02
    InclusionOngoingEndNode = 0x03
    InclusionOngoingControllerNode = 0x04
    InclusionCompletedProtocol = 0x05
    InclusionCompleted = 0x06


class LongRangeChannel(HOST_ENUM):
    ChannelA = 0x01
    ChannelB = 0x02


class FailedNodeCommandStatus(HOST_ENUM):
    RemoveStarted = 0x00
    NotPrimaryController = 0x01
    NoCallbackFunction = 0x02
    NotFound = 0x03
    RemoveProcessBusy = 0x04
    RemoveFailed = 0x05


class RemoveNodeFromNetworkCommandStatus(HOST_ENUM):
    ExclusionStarted = 0x01
    NodeFound = 0x02
    ExclusionOngoingEndNode = 0x03
    ExclusionOngoingControllerNode = 0x04
    ExclusionCompleted = 0x06
    ExclusionFailed = 0x07
    ExclusionNotPrimary = 0x23


class RemoveNodeFromNetworkCommandMode(HOST_ENUM):
    RemoveAnyNode = 0x01
    RemoveControllerNode = 0x02
    RemoveEndNode = 0x03
    StopExlusion = 0x05
