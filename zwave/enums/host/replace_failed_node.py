from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class status(HOST_ENUM):
        RemoveStarted = 0x00
        NotPrimaryController = 0x01
        NoCallbackFunction = 0x02
        NotFound = 0x03
        RemoveProcessBusy = 0x04
        RemoveFailed = 0x05


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        NodeOK = 0x00
        NodeReplaceReady = 0x03
        NodeReplaceDone = 0x04
        NodeReplaceFailed = 0x05
