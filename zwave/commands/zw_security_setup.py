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


GetSecurityKeys = 0x00  # parameter fields not used
GetSecurity2PublicDSK = 0x02  # parameter fields not used
SetSecurityInclusionRequestedKeys = 0x05  # The Parameter field MUST contain Requested Security Classes during Security Bootstrapping.
GetSecurityCapabilities = 0xFE  # parameter fields not used


# The Parameter field MUST contain the bitmask that
# represents the security keys the Z-Wave module poses.
GetSecurityKeys = 0x00

# The Parameter field MUST describe if the Security 2 DSK.
# (Derived from the Learn Mode Authenticated ECDH key pair) Refer to
# [zwave_encapsulation_cc_spec] for details about the DSK.
GetSecurity2AuthenticatedLearnModeDSK = 0x02


SetRequestedNetworkKeys = 0x05

# The Parameter field MUST be encoded as a bitmask representing the
# supported Security Modes.
#   • Bit 0 in Byte 1 MUST represent mode 0x00
#   • Bit 1 in Byte 1 MUST represent mode 0x01
#   • Bit 2 in Byte 1 MUST represent mode 0x02
#   • etc.
# A bit set to 1 MUST indicate that the corresponding Security Mode
# is supported. A bit set to 0 MUST indicate that the corresponding
# Security Mode is not supported.
GetSecurityCapabilities = 0xFE
UnknownSecurityMode = 0xFF

# GetSecurityKeys Masks
S2_Unauthenticated = 0x01
S2Authenticated = 0x02
S2Access = 0x04
S0 = 0x80


class ZwSecuritySetup(DATA_FRAME):
    """
    ???
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


class ZwSecuritySetupCallback(DATA_FRAME):
    id = 0x9C
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK
