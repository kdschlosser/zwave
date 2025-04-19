from . import HOST_CLASS, HOST_ENUM


class command(HOST_CLASS):

    class security_mode(HOST_ENUM):
        GetSecurityKeys = 0x00  # parameter fields not used
        GetSecurity2PublicDSK = 0x02  # parameter fields not used
        SetSecurityInclusionRequestedKeys = 0x05  # The Parameter field MUST contain Requested Security Classes during Security Bootstrapping.
        GetSecurityCapabilities = 0xFE  # parameter fields not used


class response(HOST_CLASS):

    class security_mode(HOST_ENUM):
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

    class security_key(HOST_ENUM):
        # GetSecurityKeys Masks
        S2_Unauthenticated = 0x01
        S2Authenticated = 0x02
        S2Access = 0x04
        S0 = 0x80


class callback(HOST_CLASS):
    pass
