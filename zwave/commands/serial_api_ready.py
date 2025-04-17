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

from ..enums import serial_api_ready


class FUNC_SERIAL_API_READY_CMD(DATA_FRAME):
    """
    The Ready Command is used by the host to inform the Z-Wave module that it is ready to receive a
    command on the UART.
    """
    id = 0xEF
    frame_type = FRAME_TYPE_REQUEST | FRAME_TYPE_ACK

    _fields_ = [('_serial_link_state', uint8_t)]

    serial_link_states = serial_api_ready.command.serial_link_state

    @property
    def packet_length(self):
        return 0

    @property
    def serial_link_state(self) -> serial_link_states:
        return self.serial_link_states(self._serial_link_state)

    @serial_link_state.setter
    def serial_link_state(self, value: serial_link_states):
        self._serial_link_state = value.value  # NOQA
