from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    
    class mode(HOST_ENUM):
        StartAdd = 0x01
        StopAdd = 0x05
        StopAddFailure = 0x06


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        InclusionStarted = 0x01
        NodeFound = 0x02
        InclusionOngoingEndNode = 0x03
        InclusionOngoingControllerNode = 0x04
        InclusionCompletedProtocol = 0x05
        InclusionCompleted = 0x06



