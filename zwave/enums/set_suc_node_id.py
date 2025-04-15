from . import HOST_ENUM, HOST_CLASS, TXOption


class command(HOST_CLASS):

    class tx_option(TXOption):
        pass

    class suc_state(HOST_ENUM):
        ControllerIsNotSUC_SIS = 0x00
        ControllerIsSUC_SIS = 0x01

    class capability(HOST_ENUM):
        IsNotSIS = 0x00
        IsSIS = 0x01


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class suc_status(HOST_ENUM):
        Succeeded = 0x05
        Failed = 0x06
