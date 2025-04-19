from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):

    class exclusion_request_status(HOST_ENUM):
        LearnModeNotSet = 0x00
        QueuedForTransmission = 0x01


class callback(HOST_CLASS):
    pass



