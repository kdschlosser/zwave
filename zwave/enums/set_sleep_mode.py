from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):

    class mode(HOST_ENUM):
        Stop = 0x00
        WakeUpTimer = 0x01
        WakeUpTimerFast = 0x02
        FrequentlyListening = 0x03


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass





