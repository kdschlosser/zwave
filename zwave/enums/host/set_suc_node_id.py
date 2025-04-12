from . import HOST_ENUM, HOST_CLASS, HOST_FLAG


class command(HOST_CLASS):
    class option(HOST_FLAG):
        MPDUAcknowledgment = 0x00
        LowPowerTransmit = 0x01
        EnableAutomaticRouting = 0x02
        DisableRouting = 0x08
        EnableExploreNPDU = 0x10

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






