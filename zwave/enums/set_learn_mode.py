from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):

    class learn_mode(HOST_ENUM):
        Disabled = 0x00
        InclusionExclusionDeprecated = 0x01
        NetworkWideInclusionDeprecated = 0x02
        NetworkWideExclusionDeprecated = 0x03
        NetworkWideInclusion = 0x81
        Exclusion = 0x82
        NetworkWideExclusion = 0x83
        SmartStart = 0x84


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class learn_mode_status(HOST_ENUM):
        Started = 0x01
        Completed = 0x06
        Failed = 0x07


