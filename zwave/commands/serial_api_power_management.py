"""
Serial API Host Appl. Prg. Guide
INS12350
2018-03-06
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    uint8_t,
    uint16_t
)

from ..enums import serial_api_power_management


# TODO: Get command ids
class FUNC_POWER_MANAGEMENT_CMD(DATA_FRAME):
    """
    The Serial API Power Management Commands is designed for use in a system where a Z-Wave module
    is connected to a host CPU system via a serial port and a number of I/O pins are used for control of the
    power to the Host CPU system.
    """

    id = 0xEE
    sub_command_id = None
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK
    _fields_ = [('_config_cmd', uint8_t)]

    @property
    def packet_length(self):
        return 0

    @property
    def config_cmd(self) -> int:
        return self._config_cmd

    @config_cmd.setter
    def config_cmd(self, value: int):
        self._config_cmd = value  # NOQA


class PM_PIN_UP_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    The Pin Configuration Command is used to map the power management input pin PoweredUp to a
    physical IO pin.
    """

    sub_command_id = None

    _fields_ = [
        ('_io_pin', uint8_t),
        ('_active_level', uint8_t),

    ]

    io_pins = serial_api_power_management.command.io_pin
    active_levels = serial_api_power_management.command.active_level

    @property
    def packet_length(self):
        return 3

    @property
    def io_pin(self) -> io_pins:
        return self.io_pins(self._io_pin)

    @io_pin.setter
    def io_pin(self, value: io_pins):
        self._io_pin = value.value  # NOQA

    @property
    def active_level(self) -> active_levels:
        return self.active_levels(self._active_level)

    @active_level.setter
    def active_level(self, value: active_levels):
        self._active_level = value.value  # NOQA


class PM_POWERUP_MODE_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    The Power up Mode Configuration Command is used to configure the state of the PowerCtrl pins when
    the Serial API has to power up the host CPU system
    """

    sub_command_id = None

    _fields_ = [
        ('_number_of_pins', uint8_t),
        ('_data', uint8_t * 8),
    ]

    io_pins = serial_api_power_management.command.io_pin
    active_levels = serial_api_power_management.command.active_level

    @property
    def packet_length(self):
        return self._number_of_pins * 2 + 2

    @property
    def io_pin1(self) -> io_pins | None:
        if self._number_of_pins >= 1:
            return self.io_pins(self._data[0])

    @io_pin1.setter
    def io_pin1(self, value: io_pins):
        pin = self.io_pin1

        self._data[0] = value.value  # NOQA

        if pin is None:
            self._number_of_pins += 1

    @property
    def pin1_active_level(self) -> active_levels | None:
        if self._number_of_pins >= 1:
            return self.active_levels(self._data[1])

    @pin1_active_level.setter
    def pin1_active_level(self, value: active_levels):
        if self._number_of_pins >= 1:
            self._data[1] = value.value  # NOQA

    @property
    def io_pin2(self) -> io_pins | None:
        if self._number_of_pins >= 2:
            return self.io_pins(self._data[2])

    @io_pin2.setter
    def io_pin2(self, value: io_pins):
        if self._number_of_pins >= 1:
            pin = self.io_pin2

            self._data[2] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin2_active_level(self) -> active_levels | None:
        if self._number_of_pins >= 2:
            return self.active_levels(self._data[3])

    @pin2_active_level.setter
    def pin2_active_level(self, value: active_levels):
        if self._number_of_pins >= 2:
            self._data[3] = value.value  # NOQA

    @property
    def io_pin3(self) -> io_pins | None:
        if self._number_of_pins >= 3:
            return self.io_pins(self._data[4])

    @io_pin3.setter
    def io_pin3(self, value: io_pins):
        if self._number_of_pins >= 2:
            pin = self.io_pin3

            self._data[4] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin3_active_level(self) -> active_levels | None:
        if self._number_of_pins >= 3:
            return self.active_levels(self._data[5])

    @pin3_active_level.setter
    def pin3_active_level(self, value: active_levels):
        if self._number_of_pins >= 3:
            self._data[5] = value.value  # NOQA

    @property
    def io_pin4(self) -> io_pins | None:
        if self._number_of_pins == 4:
            return self.io_pins(self._data[6])

    @io_pin4.setter
    def io_pin4(self, value: io_pins):
        if self._number_of_pins >= 3:
            pin = self.io_pin4

            self._data[6] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin4_active_level(self) -> active_levels | None:
        if self._number_of_pins == 4:
            return self.active_levels(self._data[7])

    @pin4_active_level.setter
    def pin4_active_level(self, value: active_levels):
        if self._number_of_pins == 4:
            self._data[7] = value.value  # NOQA


class PM_POWERUP_ZWAVE_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    Wake up the host CPU when receiving a Z-Wave command where the first 5 bytes of the frame matches
    the specified value and mask.
    """

    sub_command_id = None

    _fields_ = [
        ('_wakup_match_mode', uint8_t),
        ('_number_of_match_bytes', uint8_t),  # 8 is the max
        ('_data', uint8_t * 16),
    ]

    wakeup_match_modes = serial_api_power_management.command.wakeup_match_mode
    active_levels = serial_api_power_management.command.active_level

    @property
    def packet_length(self):
        return self._number_of_pins * 2 + 2

    @property
    def wakeup_match_mode(self) -> wakeup_match_modes:
        return self.wakeup_match_modes(self._wakeup_match_mode)

    @wakeup_match_mode.setter
    def wakeup_match_mode(self, value: wakeup_match_modes):
        self._wakeup_match_mode = value.value  # NOQA

    @property
    def values_masks(self) -> bytearray:
        return bytearray(self._data[:self._number_of_match_bytes * 2])

    @values_masks.setter
    def values_masks(self, value: bytearray):
        if len(value) % 2:
            raise ValueError

        if len(value) > 16:
            raise ValueError

        for i, item in enumerate(value):
            self._data[i] = item

        self._number_of_match_bytes = len(value) // 2  # NOQA


class PM_POWERUP_TIMER_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    The Power Up on Timer Configuration Command is used to specify that the Z-Wave module should
    power up the host CPU system after a specified time has passed.
    """

    sub_command_id = None

    _fields_ = [
        ('_timer_resolution', uint8_t),
        ('_time', uint16_t),
    ]

    timer_resolutions = serial_api_power_management.command.timer_resolution

    @property
    def packet_length(self):
        return self._number_of_pins * 2 + 2

    @property
    def timer_resolution(self) -> timer_resolutions | None:
        return self.timer_resolutions(self._timer_resolution)

    @timer_resolution.setter
    def timer_resolution(self, value: timer_resolutions):
        self._timer_resolution = value.value  # NOQA

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value: int):
        self._time = value  # NOQA


class PM_POWERUP_EXTERNAL_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    The External Power Up Configuration Command is used to specify that a level change on an input pin
    should trigger a power up of the host CPU system
    """

    sub_command_id = None

    _fields_ = [
        ('_io_pin', uint8_t),
        ('_power_up_level', uint8_t),
    ]

    io_pins = serial_api_power_management.command.io_pin
    power_up_levels = serial_api_power_management.command.active_level

    @property
    def packet_length(self):
        return 3

    @property
    def io_pin(self) -> io_pins:
        return self.io_pins(self._io_pin)

    @io_pin.setter
    def io_pin(self, value: io_pins):
        self._io_pin = value.value  # NOQA

    @property
    def power_up_level(self) -> power_up_levels:
        return self.power_up_levels(self._power_up_level)

    @power_up_level.setter
    def power_up_level(self, value: power_up_levels):
        self._power_up_level = value.value  # NOQA


class PM_POWERDOWN_MODE_CONFIGURATION_CMD(FUNC_POWER_MANAGEMENT_CMD):
    """
    The Power down Mode Configuration Command is used to request that the Z-Wave module sets a
    specific power down mode. If the PoweredUp pin is configured the PowerCtrl pins will not be changed
    before the PoweredUp pin goes NOT active.
    """

    sub_command_id = None

    _fields_ = [
        ('_number_of_pins', uint8_t),
        ('_data', uint8_t * 8),
    ]

    io_pins = serial_api_power_management.command.io_pin
    power_down_levels = serial_api_power_management.command.active_level

    @property
    def packet_length(self):
        return self._number_of_pins * 2 + 2

    @property
    def io_pin1(self) -> io_pins | None:
        if self._number_of_pins >= 1:
            return self.io_pins(self._data[0])

    @io_pin1.setter
    def io_pin1(self, value: io_pins):
        pin = self.io_pin1

        self._data[0] = value.value  # NOQA

        if pin is None:
            self._number_of_pins += 1

    @property
    def pin1_power_down_level(self) -> power_down_levels | None:
        if self._number_of_pins >= 1:
            return self.power_down_levels(self._data[1])

    @pin1_power_down_level.setter
    def pin1_power_down_level(self, value: power_down_levels):
        if self._number_of_pins >= 1:
            self._data[1] = value.value  # NOQA

    @property
    def io_pin2(self) -> io_pins | None:
        if self._number_of_pins >= 2:
            return self.io_pins(self._data[2])

    @io_pin2.setter
    def io_pin2(self, value: io_pins):
        if self._number_of_pins >= 1:
            pin = self.io_pin2

            self._data[2] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin2_power_down_level(self) -> power_down_levels | None:
        if self._number_of_pins >= 2:
            return self.power_down_levels(self._data[3])

    @pin2_power_down_level.setter
    def pin2_power_down_level(self, value: power_down_levels):
        if self._number_of_pins >= 2:
            self._data[3] = value.value  # NOQA

    @property
    def io_pin3(self) -> io_pins | None:
        if self._number_of_pins >= 3:
            return self.io_pins(self._data[4])

    @io_pin3.setter
    def io_pin3(self, value: io_pins):
        if self._number_of_pins >= 2:
            pin = self.io_pin3

            self._data[4] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin3_power_down_level(self) -> power_down_levels | None:
        if self._number_of_pins >= 3:
            return self.power_down_levels(self._data[5])

    @pin3_power_down_level.setter
    def pin3_power_down_level(self, value: power_down_levels):
        if self._number_of_pins >= 3:
            self._data[5] = value.value  # NOQA

    @property
    def io_pin4(self) -> io_pins | None:
        if self._number_of_pins == 4:
            return self.io_pins(self._data[6])

    @io_pin4.setter
    def io_pin4(self, value: io_pins):
        if self._number_of_pins >= 3:
            pin = self.io_pin4

            self._data[6] = value.value  # NOQA

            if pin is None:
                self._number_of_pins += 1

    @property
    def pin4_power_down_level(self) -> power_down_levels | None:
        if self._number_of_pins == 4:
            return self.power_down_levels(self._data[7])

    @pin4_power_down_level.setter
    def pin4_power_down_level(self, value: power_down_levels):
        if self._number_of_pins == 4:
            self._data[7] = value.value  # NOQA

