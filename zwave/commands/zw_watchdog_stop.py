"""
Z-Wave Host API Specification
0.7.2
2021.09.02
"""

from . import DATA_FRAME, FRAME_TYPE_REQUEST


class FUNC_ZW_WATCHDOG_STOP_CMD(DATA_FRAME):
    """
    Stop Hardware Watchdog (700 series and newer)

    This command is used to stop Watchdog functionality on Z-Wave module.
    """
    id = 0xD3
    frame_type = FRAME_TYPE_REQUEST

    @property
    def packet_length(self):
        return 0
