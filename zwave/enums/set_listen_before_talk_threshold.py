from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):

    class channel(HOST_ENUM):
        Channel0 = 0x00
        Channel1 = 0x01
        Channel2 = 0x02
        Channel3 = 0x03


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass

