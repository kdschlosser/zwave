from . import DATA_FRAME, FRAME_TYPE_REQUEST, FRAME_TYPE_ACK, FRAME_TYPE_RESPONSE, uint8_t
from ..enums import serial_api_setup
from .. import _utils


class SerialApiSetup(DATA_FRAME):
    id = 0x0B
    sub_command_id = 0x00
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_sub_command', uint8_t),
        ('_data', uint8_t * 256)
    ]


class SerialApiSetupResponse(DATA_FRAME):
    id = 0x0B
    sub_command_id = 0x00
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_sub_command', uint8_t)
    ]


class SerialApiSetupGetSupportedCommands(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x01


class SerialApiSetupGetSupportedCommandsResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x01

    _fields_ = [
        ('_set_node_id_flag', uint8_t, 1),
        ('_set_rf_region_flag', uint8_t, 1),
        ('_get_rf_region_flag', uint8_t, 1),
        ('_get_max_payload_flag', uint8_t, 1),
        ('_get_power_level_flag', uint8_t, 1),
        ('_set_power_level_flag', uint8_t, 1),
        ('_set_tx_status_report_flag', uint8_t, 1),
        ('_get_supported_commands_flag', uint8_t, 1),
        ('_extended_flags', uint8_t * 255)
    ]

    @property
    def supported_sub_commands(self) -> list[SerialApiSetup]:
        res = set()

        if self._get_supported_commands_flag:
            res.add(SerialApiSetupGetSupportedCommands)
        if self._set_tx_status_report_flag:
            res.add(SerialApiSetupSetTXStatusReport)
        if self._set_power_level_flag:
            res.add(SerialApiSetupSetPowerlevel)
        if self._get_power_level_flag:
            res.add(SerialApiSetupGetPowerlevel)
        if self._get_max_payload_flag:
            res.add(SerialApiSetupGetMaximumPayloadSize)
        if self._get_rf_region_flag:
            res.add(SerialApiSetupGetRFRegion)
        if self._set_rf_region_flag:
            res.add(SerialApiSetupSetRFRegion)
        if self._set_node_id_flag:
            res.add(SerialApiSetupSetNodeIDBaseType)

        sub_commands = [
            SerialApiSetupGetSupportedCommands,
            SerialApiSetupSetTXStatusReport,
            SerialApiSetupSetPowerlevel,
            SerialApiSetupGetMaximumPayloadSize,
            SerialApiSetupGetLRMaximumPayloadSize,
            SerialApiSetupGetRFRegion,
            SerialApiSetupSetRFRegion,
            SerialApiSetupSetNodeIDBaseType
        ]

        for i in range(255):
            for bit in range(8):
                if not self._extended_flags[i] & (1 << bit):
                    continue

                cmd_id = (i * 8) + bit + 1
                for sc in sub_commands:
                    if sc.id == cmd_id:
                        res.add(sc)

        return list(res)


class SerialApiSetupSetTXStatusReport(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x02

    @property
    def enable_tx_status_report(self) -> bool:
        return bool(self._data[0])

    @enable_tx_status_report.setter
    def enable_tx_status_report(self, value: bool):
        self._data[0] = int(bool(value))


class SerialApiSetupSetTXStatusReportResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x02

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status


class SerialApiSetupSetPowerlevel(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x04

    @property
    def normal_power_level(self) -> int:
        # api version 7 and above
        return _utils.from_twos_complement(self._data[0], 8) // 10

    @normal_power_level.setter
    def normal_power_level(self, value: int):
        # api version 7 and above
        self._data[0] = _utils.to_twos_complement(int(value * 10), 8)

    @property
    def measured_power_level(self) -> int:
        # api version 7 and above
        return _utils.from_twos_complement(self._data[1], 8) // 10

    @measured_power_level.setter
    def measured_power_level(self, value: int):
        # api version 7 and above
        self._data[1] = _utils.to_twos_complement(int(value * 10), 8)

    @property
    def normal_power_level_ch0(self) -> int:
        # api version 6 and below
        return self._data[0]

    @normal_power_level_ch0.setter
    def normal_power_level_ch0(self, value: int):
        # api version 6 and below
        self._data[0] = value

    @property
    def normal_power_level_ch1(self) -> int:
        # api version 6 and below
        return self._data[1]

    @normal_power_level_ch1.setter
    def normal_power_level_ch1(self, value: int):
        # api version 6 and below
        self._data[1] = value

    @property
    def normal_power_level_ch2(self) -> int:
        # api version 6 and below
        return self._data[2]

    @normal_power_level_ch2.setter
    def normal_power_level_ch2(self, value: int):
        # api version 6 and below
        self._data[2] = value

    @property
    def low_power_level_ch0(self) -> int:
        # api version 6 and below
        mapping = {
            0x3F: 0,
            0x24: 2,
            0x1E: 4,
            0x16: 6,
            0x11: 8,
            0x0E: 10,
            0x0B: 12,
            0x09: 14,
            0x07: 16,
            0x05: 18,
            0x04: 20,
            0x03: 22
        }

        return mapping[self._data[3]]

    @low_power_level_ch0.setter
    def low_power_level_ch0(self, value: int):
        # api version 6 and below
        mapping = {
            0: 0x3F,
            2: 0x24,
            4: 0x1E,
            6: 0x16,
            8: 0x11,
            10: 0x0E,
            12: 0x0B,
            14: 0x09,
            16: 0x07,
            18: 0x05,
            20: 0x04,
            22: 0x03
        }
        if value not in mapping:
            raise ValueError(
                'Power setting must be an even number from 0 to 22'
                )

        self._data[3] = mapping[value]

    @property
    def low_power_level_ch1(self) -> int:
        # api version 6 and below
        mapping = {
            0x3F: 0,
            0x24: 2,
            0x1E: 4,
            0x16: 6,
            0x11: 8,
            0x0E: 10,
            0x0B: 12,
            0x09: 14,
            0x07: 16,
            0x05: 18,
            0x04: 20,
            0x03: 22
        }

        return mapping[self._data[4]]

    @low_power_level_ch1.setter
    def low_power_level_ch1(self, value: int):
        # api version 6 and below
        mapping = {
            0: 0x3F,
            2: 0x24,
            4: 0x1E,
            6: 0x16,
            8: 0x11,
            10: 0x0E,
            12: 0x0B,
            14: 0x09,
            16: 0x07,
            18: 0x05,
            20: 0x04,
            22: 0x03
        }
        if value not in mapping:
            raise ValueError(
                'Power setting must be an even number from 0 to 22'
                )

        self._data[4] = mapping[value]

    @property
    def low_power_level_ch2(self) -> int:
        # api version 6 and below
        mapping = {
            0x3F: 0,
            0x24: 2,
            0x1E: 4,
            0x16: 6,
            0x11: 8,
            0x0E: 10,
            0x0B: 12,
            0x09: 14,
            0x07: 16,
            0x05: 18,
            0x04: 20,
            0x03: 22
        }

        return mapping[self._data[5]]

    @low_power_level_ch2.setter
    def low_power_level_ch2(self, value: int):
        # api version 6 and below
        mapping = {
            0: 0x3F,
            2: 0x24,
            4: 0x1E,
            6: 0x16,
            8: 0x11,
            10: 0x0E,
            12: 0x0B,
            14: 0x09,
            16: 0x07,
            18: 0x05,
            20: 0x04,
            22: 0x03
        }
        if value not in mapping:
            raise ValueError('Power setting must be an even number from 0 to 22')

        self._data[5] = mapping[value]


class SerialApiSetupSetPowerlevelResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x04

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status


class SerialApiSetupGetPowerlevel(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x08


class SerialApiSetupGetPowerlevelResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x08

    @property
    def normal_power_level(self) -> int:
        return _utils.from_twos_complement(self._data[0], 8) // 10

    @property
    def measured_power_level(self) -> int:
        return _utils.from_twos_complement(self._data[1], 8) // 10


class SerialApiSetupGetMaximumPayloadSize(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x10


class SerialApiSetupGetMaximumPayloadSizeResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x10

    @property
    def payload_size(self) -> int:
        return self._data[0]


class SerialApiSetupGetLRMaximumPayloadSize(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x11


class SerialApiSetupGetLRMaximumPayloadSizeResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x11

    @property
    def payload_size(self) -> int:
        return self._data[0]


class SerialApiSetupGetRFRegion(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x20


class SerialApiSetupGetRFRegionResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x20

    rf_regions = serial_api_setup.response.rf_region

    @property
    def rf_region(self) -> rf_regions:
        return self.rf_regions(self._data[0])

    @rf_region.setter
    def rf_region(self, value: rf_regions):
        self._data[0] = value.value


class SerialApiSetupSetRFRegion(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x40

    rf_regions = serial_api_setup.command.rf_region

    @property
    def rf_region(self) -> rf_regions:
        return self.rf_regions(self._data[0])

    @rf_region.setter
    def rf_region(self, value: rf_regions):
        self._data[0] = value.value


class SerialApiSetupSetRFRegionResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x40

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status


class SerialApiSetupSetNodeIDBaseType(SerialApiSetup):
    id = 0x0B
    sub_command_id = 0x80

    node_id_base_types = serial_api_setup.command.node_id_base_type

    @property
    def node_id_base_type(self) -> node_id_base_types:
        return self.node_id_base_types(self._data[0])

    @node_id_base_type.setter
    def node_id_base_type(self, value: node_id_base_types):
        self._data[0] = value.value


class SerialApiSetupSetNodeIDBaseTypeResponse(SerialApiSetupResponse):
    id = 0x0B
    sub_command_id = 0x80

    _fields_ = [('_command_status', uint8_t)]

    @property
    def command_status(self) -> int:
        return self._command_status
