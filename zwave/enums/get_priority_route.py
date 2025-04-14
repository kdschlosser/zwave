from . import HOST_CLASS, RouteDataRate


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class route_speed(RouteDataRate):
        pass


class callback(HOST_CLASS):
    pass
