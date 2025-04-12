from . import HOST_ENUM, HOST_CLASS, HOST_FLAG


class command(HOST_CLASS):

    class option(HOST_FLAG):
        MPDUAcknowledgment = 0x00
        LowPowerTransmit = 0x01
        EnableAutomaticRouting = 0x02
        DisableRouting = 0x08
        EnableExploreNPDU = 0x10


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        OK = 0x00
        NoACK = 0x01
        Fail = 0x02
        RoutingNotIdle = 0x03
        NoRoute = 0x04
        Verified = 0x05






