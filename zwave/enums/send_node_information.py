from . import HOST_CLASS, TXStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(TXStatus):
        pass



