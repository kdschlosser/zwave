"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import firmware_update_nvm


class FUNC_ZW_FIRMWARE_UPDATE_NVM_CMD(DATA_FRAME):
    # TODO: Override to_bytes
    """
    ZWave Firmware Update API

    The Firmware Update API is also supported by the serial API enabling firmware update via
    Serial API also called Over The Wire (OTW) firmware update. This is an alternative to program the chip
    in programming mode [3] via SPI, UART or USB. However, OTW requires a target containing a boot
    loader and serial API support.
    """
    id = 0x78
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_functionality', uint8_t)
    ]

    _stored_data: bytearray | None = None

    functionalities = firmware_update_nvm.command.functionality

    @property
    def packet_length(self):
        if self._stored_data is None:
            return 1
        else:
            return len(self._stored_data) + 1

    @property
    def functionality(self) -> functionalities:
        return self.functionalities(self._functionality)

    @property
    def data(self) -> bytearray:
        if self._stored_data is None:
            return bytearray(0)
        else:
            return self._stored_data

    @data.setter
    def data(self, value: bytearray):
        self._stored_data = value
