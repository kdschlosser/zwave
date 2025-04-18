from . import HOST_CLASS, HOST_ENUM, TXOption, TXStatus


class command(HOST_CLASS):

    class tx_option(TXOption):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class tx_status(TXStatus):
        pass





