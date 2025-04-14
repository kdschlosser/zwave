from . import HOST_ENUM, HOST_CLASS, RFRegion


class command(HOST_CLASS):
    class node_id_base_type(HOST_ENUM):
        EightBit = 0x01
        SixteenBit = 0x02

    class rf_region(RFRegion):
        pass


class response(HOST_CLASS):

    class rf_region(RFRegion):
        pass
