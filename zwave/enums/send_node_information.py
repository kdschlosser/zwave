from . import HOST_CLASS, TXStatus, TXOption


class command(HOST_CLASS):

    class tx_option(TXOption):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class tx_status(TXStatus):
        pass



