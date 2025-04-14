from . import HOST_ENUM, HOST_CLASS, HOST_FLAG


class command(HOST_CLASS):

    class node_ids(HOST_FLAG):
        NodeID2002 = 0x01
        NodeID2003 = 0x02
        NodeID2004 = 0x04
        NodeID2005 = 0x08


class response(HOST_CLASS):
    pass


class callback(HOST_CLASS):
    pass
