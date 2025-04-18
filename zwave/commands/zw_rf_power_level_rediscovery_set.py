from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_ACK,
    uint8_t
)

from ..enums import rf_power_level_rediscovery_set


class FUNC_SET_RF_POWERLEVEL_REDISCOVERY_CMD(DATA_FRAME):
    """
    Set RF Power Level Rediscovery Command

    This command is used to set the power level to RF Module that can be used for finding neighboring
    nodes.
    """

    id = 0x1E
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_power_level', uint8_t)]

    power_levels = rf_power_level_rediscovery_set.command.power_level

    @property
    def packet_length(self):
        return 1

    @property
    def power_level(self) -> power_levels:
        return self.power_levels(self._power_level)

    @power_level.setter
    def power_level(self, value: power_levels):
        self._power_level = value.value  # NOQA
