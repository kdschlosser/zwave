from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class neighbor_discovery(HOST_ENUM):
        Started = 0x00
        Completed = 0x01
        Failed = 0x02
        NotSupported = 0x03





