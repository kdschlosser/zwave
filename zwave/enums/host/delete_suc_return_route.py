from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


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






