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

from ..enums import set_dcdc_config


class FUNC_SET_DCDC_CONFIG_CMD(DATA_FRAME):
    """
    DCDC Configuration Commands

    The current DCDC configuration can be updated or retrieved using Set DCDC Configuration and Get
    DCDC Configuration Commands, respectively.
    """
    id = 0xDF
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_dcdc_configuration', uint8_t)
    ]

    dcdc_configurations = set_dcdc_config.command.dcdc_configuration

    @property
    def packet_length(self):
        return 1

    @property
    def dcdc_configuration(self) -> dcdc_configurations:
        return self.dcdc_configurations(self._dcdc_configuration)

    @dcdc_configuration.setter
    def dcdc_configuration(self, value: dcdc_configurations):
        self._dcdc_configuration = value.value  # NOQA



class FUNC_SET_DCDC_CONFIG_RSP(DATA_FRAME):
    """
    ???
    """
    id = 0xDF
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('_cmd_res', uint8_t)]

    cmd_reses = set_dcdc_config.response.cmd_res

    @property
    def cmd_res(self) -> cmd_reses:
        return self.cmd_reses(self._cmd_res)

