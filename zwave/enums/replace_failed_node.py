from . import HOST_ENUM, HOST_CLASS, FailedNodeCommandStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class response_status(FailedNodeCommandStatus):
        pass


class callback(HOST_CLASS):

    class operation_status(HOST_ENUM):
        NodeOK = 0x00
        NodeReplaceReady = 0x03
        NodeReplaceDone = 0x04
        NodeReplaceFailed = 0x05
