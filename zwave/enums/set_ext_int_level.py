from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class int_src(HOST_ENUM):
        INT0 = 0x00
        INT1 = 0x01


class response(HOST_CLASS):
    pass

class callback(HOST_CLASS):
    pass



