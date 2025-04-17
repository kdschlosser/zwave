from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    FRAME_TYPE_RESPONSE,
    uint8_t,
    uint16_t
)
from .. import mfg_ids


class FUNC_SERIAL_API_GET_CAPABILITIES_CMD(DATA_FRAME):
    """
    """
    id = 0x07
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK


class FUNC_SERIAL_API_GET_CAPABILITIES_RSP(DATA_FRAME):
    id = 0x07
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_zwave_api_version', uint16_t),
        ('_zwave_api_mfg_id', uint16_t),
        ('_zwave_api_product_type', uint16_t),
        ('_zwave_api_product_id', uint16_t),
        ('_zwave_api_supported_commands', uint8_t * 32)
    ]

    @property
    def packet_length(self):
        return 40

    @property
    def api_version(self) -> int:
        return self._zwave_api_version

    @property
    def mfg_version(self):
        return mfg_ids.MFG_ID(self._zwave_api_mfg_id)

    @property
    def product_type(self) -> int:
        return self._zwave_api_product_type

    @property
    def product_id(self) -> int:
        return self._zwave_api_product_id

    @property
    def supported_commands(self) -> list[DATA_FRAME]:
        res = []
        for i in range(32):
            for bit in range(8):
                if self._zwave_api_supported_commands[i] & (1 << bit):
                    res.append(DATA_FRAME.from_id((i * 8) + bit + 1))

        return res
