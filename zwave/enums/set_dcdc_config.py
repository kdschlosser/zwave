from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class dcdc_configuration(HOST_ENUM):
        Auto = 0x00
        Bypass = 0x01
        LowNoise = 0x02


class response(HOST_CLASS):

    class cmd_res(HOST_ENUM):
        Fail = 0x00
        Success = 0x01


class callback(HOST_CLASS):
    pass



