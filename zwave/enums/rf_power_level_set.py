from . import HOST_CLASS, HOST_ENUM


class command(HOST_CLASS):

    class power_level(HOST_ENUM):
        PowerNormal = 0x00
        PowerMinus1dB = 0x01
        PowerMinus2dB = 0x02
        PowerMinus3dB = 0x03
        PowerMinus4dB = 0x04
        PowerMinus5dB = 0x05
        PowerMinus6dB = 0x06
        PowerMinus7dB = 0x07
        PowerMinus8dB = 0x08
        PowerMinus9dB = 0x09


class response(HOST_CLASS):

    class power_level(command.power_level):
        pass


class callback(HOST_CLASS):
    pass





