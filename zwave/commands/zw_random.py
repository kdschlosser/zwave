"""
Z-Wave 500 Series Appl. Programmers Guide v6.8x.0x
INS13954
2020-04-21
"""

from . import (
    DATA_FRAME,
    FRAME_TYPE_REQUEST,
    FRAME_TYPE_RESPONSE,
    FRAME_TYPE_CALLBACK,
    FRAME_TYPE_ACK,
    NODE_ID_8_FRAME,
    NODE_ID_16_FRAME,
    NODE_ID_FIELDS,
    uint8_t
)


class FUNC_ZW_RANDOM_CMD(DATA_FRAME):
    """
    This function implements a simple pseudo-random number generator that generates a sequence of
    numbers, the elements of which are approximately independent of each other. The same sequence of
    pseudo-random numbers will be repeated in case the module is power cycled.

    An application MAY use this function for implementing random behavior, e.g., when multiple nodes
    respond to a multicast message. The Z-Wave protocol MAY also use this function for random backoff,
    etc.

    Due to its simple nature, an application MUST NOT use this function for obtaining random values for
    security key calculation and encryption.
    """
    id = 0x1D
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    @property
    def packet_length(self):
        return 0


class FUNC_ZW_RANDOM_RSP(DATA_FRAME):
    id = 0x1D
    frame_type = FRAME_TYPE_RESPONSE | FRAME_TYPE_ACK

    _fields_ = [('generated_number', uint8_t)]

    @property
    def generated_number(self) -> int:
        return self._generated_number
