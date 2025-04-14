from . import HOST_CLASS, LongRangeChannel


class command(HOST_CLASS):

    class long_range(LongRangeChannel):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
