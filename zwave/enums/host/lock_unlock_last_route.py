from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class lock_mode(HOST_ENUM):
        DoNotSaveRoute = 0x00
        SaveRoute = 0x01


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass

