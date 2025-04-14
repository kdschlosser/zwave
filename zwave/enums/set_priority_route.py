from . import HOST_CLASS, RouteDataRate


class command(HOST_CLASS):

    class route_speed(RouteDataRate):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
