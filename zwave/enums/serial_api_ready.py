from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class serial_link_state(HOST_ENUM):
        Detached = 0x00
        Connected = 0x01


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
