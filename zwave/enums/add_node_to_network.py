from . import HOST_ENUM, HOST_CLASS, AddNodeToNetworkStatus


class command(HOST_CLASS):

    class mode(HOST_ENUM):
        AddAnyNode = 0x01
        AddControllerNode = 0x02
        AddEndNode = 0x03
        AddExistingNode = 0x04
        StopInclusion = 0x05
        StopControllerReplication = 0x06
        SmartStartIncludeNode = 0x08
        StartSmartStart = 0x09


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(AddNodeToNetworkStatus):
        pass
