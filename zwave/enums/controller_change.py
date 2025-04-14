from . import HOST_CLASS, PrimaryControllerMode, AddNodeToNetworkStatus


class command(HOST_CLASS):
    
    class mode(PrimaryControllerMode):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(AddNodeToNetworkStatus):
        pass
