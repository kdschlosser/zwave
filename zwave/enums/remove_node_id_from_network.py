from . import HOST_CLASS, RemoveNodeFromNetworkCommandMode, RemoveNodeFromNetworkCommandStatus


class command(HOST_CLASS):
    class mode(RemoveNodeFromNetworkCommandMode):
        pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(RemoveNodeFromNetworkCommandStatus):
        pass

