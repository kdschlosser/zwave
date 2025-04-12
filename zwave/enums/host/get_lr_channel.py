from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class long_range(HOST_ENUM):
        ChannelA = 0x01
        ChannelB = 0x02


class callback(HOST_CLASS):
    pass
