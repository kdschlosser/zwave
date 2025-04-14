from . import HOST_ENUM, HOST_CLASS, RXStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass


class unsolicited(HOST_CLASS):

    class rx_status(RXStatus):
        pass
