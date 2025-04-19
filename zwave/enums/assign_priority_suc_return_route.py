from . import HOST_CLASS, HOST_ENUM, RouteDataRate, TXStatus


class command(HOST_CLASS):
    class route_speed(RouteDataRate):
        pass


class response(HOST_CLASS):

    class suc_route_response(HOST_ENUM):
        AlreadyActive = 0x00
        Started = 0x01


class callback(HOST_CLASS):

    class tx_status(TXStatus):
        pass
