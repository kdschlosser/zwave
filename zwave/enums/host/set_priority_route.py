from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class route_speed(HOST_ENUM):
        RouteSpeed9600 = 0x01
        RouteSpeed40k = 0x02
        RouteSpeed100k = 0x03


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
