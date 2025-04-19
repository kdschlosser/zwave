from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class network_update_status(HOST_ENUM):
        UpdateDone = 0x00
        UpdateAborted = 0x01
        SUCBusy = 0x02
        UpdateOverflow = 0x03
