"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    FRAME_TYPE_RESPONSE,
    uint8_t,
    uint16_t
)

from ..enums import nvm_backup_restore


class FUNC_NVM_BACKUP_RESTORE_CMD(DATA_FRAME):
    """
    This command is used to read and write the firmware data of the Z-Wave API Module.

    (700+ series)
    """
    id = 0x2E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [
        ('_sub_command', uint8_t),
        ('_firmware_data_len', uint8_t),
        ('_address_offset', uint16_t),
        ('_data', uint8_t * 256)
    ]

    sub_commands = nvm_backup_restore.command.sub_command

    @property
    def packet_length(self):
        return self._firmware_data_len + 4

    @property
    def sub_command(self) -> sub_commands:
        return self.sub_commands(self._sub_command)

    @sub_command.setter
    def sub_command(self, value: sub_commands):
        self._sub_commamnd = value.value  # NOQA

    @property
    def address_offset(self) -> int:
        return self._address_offset

    @address_offset.setter
    def address_offset(self, value: int):
        self._address_offset = value  # NOQA

    @property
    def data(self) -> bytearray:
        res = bytearray(self._firmware_data_len)
        for i in range(self._firmware_data_len):
            res[i] = self._data[i]

        return res

    @data.setter
    def data(self, value: bytearray):
        self._firmware_data_len = len(value)  # NOQA
        for i, item in enumerate(value):
            self._data[i] = item


class FUNC_NVM_BACKUP_RESTORE_RSP(DATA_FRAME):
    id = 0x2E
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [
        ('_status', uint8_t),
        ('_firmware_data_len', uint8_t),
        ('_address_offset_h', uint8_t),
        ('_address_offset_l', uint8_t),
        ('_data', uint8_t * 256)
    ]

    statuses = nvm_backup_restore.response.status

    @property
    def status(self) -> statuses:
        return self.statuses(self._status)

    @property
    def address_offset(self) -> int:
        return self._address_offset_h << 8 | self._address_offset_l

    @property
    def data(self) -> bytearray:
        res = bytearray(self._firmware_data_len)
        for i in range(self._firmware_data_len):
            res[i] = self._data[i]

        return res
