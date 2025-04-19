"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

# TODO: finish this commamnd

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)

from ..enums import security_setup



class FUNC_ZW_SECURITY_SETUP_CMD(DATA_FRAME):
    """
    Security Setup Command

    This command is used to set the Requested Security Keys and Requested Authentication method prior
    to inclusion (add). The Requested Security Keys and Authentication is requested by the protocol during
    S2 inclusion.
    """
    id = 0x9C
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    security_modes = security_setup.command.security_mode

    _fields_ = [
        ('_security_mode', uint8_t),
        ('_parameter_length', uint8_t),
        ('_parameters', uint8_t * 255)
    ]

    @property
    def packet_length(self):
        return 0

    @property
    def security_mode(self) -> security_modes:
        return self.security_modes(self._security_mode)

    @security_mode.setter
    def security_mode(self, value: security_modes):
        self._security_mode = value.value  # NOQA

    @property
    def parameters(self) -> list:
        return None


class FUNC_ZW_SECURITY_SETUP_RSP(DATA_FRAME):
    id = 0x9C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    security_modes = security_setup.command.security_mode

    _fields_ = [
        ('_security_mode', uint8_t),
        ('_parameter_length', uint8_t),
        ('_parameters', uint8_t * 255)
    ]

    @property
    def security_mode(self) -> security_modes:
        return self.security_modes(self._security_mode)

    @security_mode.setter
    def security_mode(self, value: security_modes):
        self._security_mode = value.value  # NOQA

    @property
    def parameters(self) -> list:
        return None
