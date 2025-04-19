from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class new_route_response(HOST_ENUM):
        FailedOrBusy = 0x00
        Started = 0x01


class callback(HOST_CLASS):

    class new_route_status(HOST_ENUM):
        UpdateDone = 0x00
        UpdateAbort = 0x01
        UpdateBusy = 0x02
        UpdateDisabled = 0x03
