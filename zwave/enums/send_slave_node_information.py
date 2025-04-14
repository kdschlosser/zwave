from . import HOST_CLASS, TXOption, TXStatus


class command(HOST_CLASS):

    class option(TXOption):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(TXStatus):
        pass





