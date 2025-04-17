"""
Serial API Host Appl. Prg. Guide
INS12350
2022-12-01
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import get_dcdc_config


class FUNC_GET_DCDC_CONFIG_CMD(DATA_FRAME):
    """
    ???
    """
    id = 0xDE
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_GET_DCDC_CONFIG_RSP(DATA_FRAME):
    """
    ???
    """
    id = 0xDE
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_dcdc_configuration', uint8_t)]

    dcdc_configurations = get_dcdc_config.response.dcdc_configuration

    @property
    def dcdc_configuration(self) -> dcdc_configurations:
        return self.dcdc_configurations(self._dcdc_configuration)
