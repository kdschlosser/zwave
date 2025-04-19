from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class route_status(HOST_ENUM):
        LostAccept = 0x00
        LostFailed = 0x01
        UpdateAbort = 0x02
        UpdateDone = 0x03






