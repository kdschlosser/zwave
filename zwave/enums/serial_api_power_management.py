from . import HOST_ENUM, HOST_CLASS


class command(HOST_CLASS):
    class io_pin(HOST_ENUM):
        PinP00 = 0x00
        PinP01 = 0x01
        PinP02 = 0x02
        PinP03 = 0x03
        PinP04 = 0x04
        PinP05 = 0x05
        PinP06 = 0x06
        PinP07 = 0x07
        PinP10 = 0x10
        PinP11 = 0x11
        PinP12 = 0x12
        PinP13 = 0x13
        PinP14 = 0x14
        PinP15 = 0x15
        PinP16 = 0x16
        PinP17 = 0x17
        PinP22 = 0x22
        PinP23 = 0x23
        PinP24 = 0x24
        PinP30 = 0x30
        PinP31 = 0x31
        PinP32 = 0x32
        PinP33 = 0x33
        PinP34 = 0x34
        PinP35 = 0x35
        PinP36 = 0x36
        PinP37 = 0x37

    class active_level(HOST_ENUM):
        Low = 0x00
        High = 0x01

    class wakeup_match_mode(HOST_ENUM):
        WakeUpAll = 0x01
        WakeUpAllNoBroadcast = 0x02
        WakeUpMask = 0x03

    class timer_resolution(HOST_ENUM):
        Seconds = 0x01
        Minutes = 0x02




class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
