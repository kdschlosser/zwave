from . import HOST_CLASS, HOST_ENUM


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class status(HOST_ENUM):
        Idle = 0x00
        Routing = 0x01
        SUC = 0x02


class callback(HOST_CLASS):
    pass
