"""
Serial API Host Appl. Prg. Guide
INS12350
2018-03-06
"""

from . import DATA_FRAME, FRAME_TYPE_REQUEST


class FUNC_ZW_WATCHDOG_START_CMD(DATA_FRAME):
    """
    Start Hardware Watchdog (700 series and newer)
    """
    id = 0xD2
    frame_type = FRAME_TYPE_REQUEST

    @property
    def packet_length(self):
        return 0
