from . import HOST_CLASS, HOST_ENUM


class command(HOST_CLASS):
    class mode(HOST_ENUM):
        Off = 0x00
        On = 0x01


class response(HOST_CLASS):
    class status(HOST_ENUM):
        Fail = 0x00
        Success = 0x01


class callback(HOST_CLASS):
    pass
