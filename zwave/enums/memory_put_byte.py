from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class response(HOST_ENUM):
        Error = 0x00
        NoChange = 0x01
        ByteWritten = 0x02


class callback(HOST_CLASS):
    pass
