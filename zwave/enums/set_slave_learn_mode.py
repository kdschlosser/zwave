from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):

    class mode(HOST_ENUM):
        Disable = 0x00
        Enable = 0x01
        Add = 0x02
        Remove = 0x03


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class status(HOST_ENUM):
        AssignComplete = 0x00
        AssignNodeIDDone = 0x01
        AssignRangeInfoUpdate = 0x02





