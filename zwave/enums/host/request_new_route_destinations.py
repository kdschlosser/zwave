from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        Done = 0x00
        Abort = 0x01
        Wait = 0x02
        Disabled = 0x03





