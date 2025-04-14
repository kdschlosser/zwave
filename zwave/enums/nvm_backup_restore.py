from . import HOST_ENUM, HOST_CLASS, HOST_FLAG


class command(HOST_CLASS):

    class sub_command(HOST_FLAG):
        Open = 0x00
        Read = 0x01
        Write = 0x02
        Close = 0x03


class response(HOST_CLASS):

    class status(HOST_ENUM):
        OK = 0x00
        Error = 0x01
        ErrorOperationMismatch = 0x02
        ErrorOperationInterference = 0x03


class callback(HOST_CLASS):
    pass
