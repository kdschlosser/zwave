from . import HOST_ENUM, HOST_CLASS, RXStatus


class command(HOST_CLASS):
    pass


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass


class unsolicited(HOST_CLASS):

    class rx_status(RXStatus):
        pass

    class event(HOST_ENUM):
        SISNodeIDUpdated = 0x10
        NodeRemoved = 0x20
        NodeAdded = 0x40
        RoutingPending = 0x80
        NodeInfoRequestFailed = 0x81
        NodeInfoRequestDone = 0x82
        NOPPowerReceived = 0x83
        NodeInfoReceived = 0x84
        NodeInfoSmartstartHomeIDReceived = 0x85
        IncludedNodeInfoReceived = 0x86
        LRNodeInfoSmartstartHomeIDReceived = 0x87
