from . import HOST_CLASS, HOST_ENUM, TXStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class return_route_response(HOST_ENUM):
        Failed = 0x00
        Started = 0x01


class callback(HOST_CLASS):

    class tx_status(TXStatus):
        pass






