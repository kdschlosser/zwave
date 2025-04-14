from . import HOST_ENUM, HOST_CLASS, DeviceOption


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass


class unsolicited(HOST_CLASS):

    class option(DeviceOption):
        pass

    class wakeup(HOST_ENUM):
        Reset = 0x00
        WakeUpTimer = 0x01
        WakeUpBeam = 0x02
        WatchdogReset = 0x03
        ExternalInterrupt = 0x04
        PowerUp = 0x05
        USBSuspend = 0x06
        SoftwareReset = 0x07
        EmergencyWatchdogReset = 0x08
        BrownoutCircuit = 0x09
        Unknown = 0xFF
