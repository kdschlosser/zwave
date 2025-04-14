from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class protocol_type(HOST_ENUM):
        ZWave = 0x00
        AV = 0x01
        IP = 0x02


class callback(HOST_CLASS):

    pass
