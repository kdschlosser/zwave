from . import HOST_ENUM, HOST_CLASS, FailedNodeCommandStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class status(FailedNodeCommandStatus):
        pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        NodeOK = 0x00
        NodeReplaceReady = 0x03
        NodeReplaceDone = 0x04
        NodeReplaceFailed = 0x05
