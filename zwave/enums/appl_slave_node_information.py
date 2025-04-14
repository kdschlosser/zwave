from . import HOST_CLASS, DeviceOption


class command(HOST_CLASS):

    class option(DeviceOption):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
