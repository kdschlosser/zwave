from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):

    class functionality(HOST_ENUM):
        Init = 0x00
        SetNewImage = 0x01
        GetNewImage = 0x02
        UpdateCRC16 = 0x03
        IsValidCRC = 0x04
        Write = 0x05


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass



