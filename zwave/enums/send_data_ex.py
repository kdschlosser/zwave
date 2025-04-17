from . import HOST_CLASS, HOST_ENUM, TXOption, TXStatus


class command(HOST_CLASS):

    class tx_option(TXOption):
        pass

    class tx_security_option(HOST_ENUM):
        S2VerifyDelivery = 0x01
        S2SinglecastFollowup = 0x02
        S2FirstSinglecastFollowup = 0x03

    class security_key(HOST_ENUM):
        NoKey = 0x00
        S2UnauthenticatedKey = 0x01
        S2AuthenticatedKey = 0x02
        S2AccessKey = 0x03
        S0Key = 0x04


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):

    class tx_status(TXStatus):
        pass





