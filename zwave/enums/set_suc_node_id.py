from . import HOST_ENUM, HOST_CLASS, TXOption


class command(HOST_CLASS):

    class option(TXOption):
        pass

    class suc_state(HOST_ENUM):
        ControllerIsNotSUCOrSIS = 0x00
        ControllerIsSUCOrSIS = 0x01

    class capability(HOST_ENUM):
        IsNotSIS = 0x00
        IsSIS = 0x01


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        SetSUCSucceeded = 0x05
        SetSUCFailed = 0x06






