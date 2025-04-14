from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class library_type(HOST_ENUM):
        StaticController = 0x01
        PortableController = 0x02
        EnhancedEndNode = 0x03
        EndNode = 0x04
        Installer = 0x05
        RoutingEndNode = 0x06
        BridgeController = 0x07


class callback(HOST_CLASS):
    pass


