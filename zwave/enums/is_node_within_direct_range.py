from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class direct_range_status(HOST_ENUM):
        IsNotDirect = 0x00
        IsDirect = 0x01


class callback(HOST_CLASS):
    pass


