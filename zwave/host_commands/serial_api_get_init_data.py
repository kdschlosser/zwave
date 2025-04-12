from . import HOST_COMMAND, HOST_RESPONSE, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t


class SerialApiGetInitData(HOST_COMMAND):
    id = 0x02
    frame_type = FRAME_TYPE_ACK | FRAME_TYPE_RESPONSE


class SerialApiGetInitDataResponse(HOST_RESPONSE):
    id = 0x02

    _fields_ = [
        ('_zwave_api_version', uint8_t),
        ('_reserved', uint8_t, 4),
        ('_sis_flag', uint8_t, 1),
        ('_primary_flag', uint8_t, 1),
        ('_timer_flag', uint8_t, 1),
        ('_controller_flag', uint8_t, 1),
        ('_zwave_node_list_len', uint8_t),
        ('_zwave_node_list', uint8_t * 34),
    ]

    @property
    def zwave_api_version(self):
        version = self._zwave_api_version

        if version > 9:
            version = f'v{version - 9}.0'
        else:
            version = f'v{version}.0.non-standard'

        return version

    @property
    def is_controller(self):
        return bool(self._controller_flag)

    @property
    def supports_timer_functions(self):
        return bool(self._timer_flag)

    @property
    def is_primary_controller(self):
        return bool(self._primary_flag)

    @property
    def is_sis_enabled(self):
        return bool(self._sis_flag)

    @property
    def zwave_node_list_len(self):
        return self._zwave_node_list_len

    @property
    def zwave_node_list(self):
        res = []
        for i in range(self.zwave_node_list_len):
            for bit in range(8):
                if self._zwave_node_list[i] & (1 << bit):
                    res.append((i * 8) + bit + 1)

        return res

    @property
    def chip_type(self):
        return self._zwave_node_list[self.zwave_node_list_len + 1]

    @property
    def chip_version(self):
        return self._zwave_node_list[self.zwave_node_list_len + 2]
