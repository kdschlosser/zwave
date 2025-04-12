from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class mode(HOST_ENUM):
        RemoveAnyNode = 0x01
        RemoveControllerNode = 0x02
        RemoveEndNode = 0x03
        StopExlusion = 0x05


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        ExclusionStarted = 0x01
        NodeFound = 0x02
        ExclusionOngoingEndNode = 0x03
        ExclusionOngoingControllerNode = 0x04
        ExclusionCompleted = 0x06
        ExclusionFailed = 0x07
        ExclusionNotPrimary = 0x23

