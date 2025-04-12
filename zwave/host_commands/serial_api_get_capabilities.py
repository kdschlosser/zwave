from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from .. import mfg_ids


class SerialApiGetCapabilities(HOST_COMMAND):
    id = 0x07
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class SerialApiGetCapabilitiesResponse(HOST_RESPONSE):
    id = 0x07

    _fields_ = [
        ('_zwave_api_version1', uint8_t),
        ('_zwave_api_version2', uint8_t),
        ('_zwave_api_mfg_id1', uint8_t),
        ('_zwave_api_mfg_id2', uint8_t),
        ('_zwave_api_product_type1', uint8_t),
        ('_zwave_api_product_type2', uint8_t),
        ('_zwave_api_product_id1', uint8_t),
        ('_zwave_api_product_id2', uint8_t),
        ('_zwave_api_supported_commands', uint8_t * 32)
    ]

    @property
    def api_version(self):
        return self._zwave_api_version1 << 8 | self._zwave_api_version2

    @property
    def mfg_version(self):
        return mfg_ids.MFG_ID(self._zwave_api_mfg_id1 << 8 | self._zwave_api_mfg_id2)

    @property
    def product_type(self):
        return self._zwave_api_product_type1 << 8 | self._zwave_api_product_type2

    @property
    def product_id(self):
        return self._zwave_api_product_id1 << 8 | self._zwave_api_product_id2

    @property
    def supported_commands(self) -> list[HOST_COMMAND]:
        res = []
        for i in range(32):
            for bit in range(8):
                if self._zwave_api_supported_commands[i] & (1 << bit):
                    res.append(HOST_COMMAND.from_id((i * 8) + bit + 1))

        return res


