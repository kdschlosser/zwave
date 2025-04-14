from . import HOST_CLASS, LongRangeChannel


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class long_range(LongRangeChannel):
        pass


class callback(HOST_CLASS):
    pass
