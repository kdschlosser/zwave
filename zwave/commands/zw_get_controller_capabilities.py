from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)


class FUNC_ZW_GET_CONTROLLER_CAPABILITIES_CMD(DATA_FRAME):
    """
    """
    id = 0x05
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_GET_CONTROLLER_CAPABILITIES_RSP(DATA_FRAME):
    id = 0x05
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_secondary_controller', uint8_t, 1),
        ('_other_network', uint8_t, 1),
        ('_sis_present', uint8_t, 1),
        ('_reserved1', uint8_t, 1),
        ('_suc_enabled', uint8_t, 1),
        ('_no_nodes_included', uint8_t, 1),
        ('_reserved2', uint8_t, 2)
    ]

    @property
    def is_secondary_controller(self):
        return bool(self._secondary_controller)

    @property
    def started_network(self):
        return bool(not self._other_network)

    @property
    def is_sis_present(self):
        return bool(self._sis_present)

    @property
    def is_suc_enabled(self):
        return bool(self._suc_enabled)

    @property
    def has_included_nodes(self):
        return bool(self._no_nodes_included)
