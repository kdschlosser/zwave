import ctypes


uint8_t = ctypes.c_uint8

FRAME_TYPE_REQUEST = 0x00
FRAME_TYPE_RESPONSE = 0x01
FRAME_TYPE_CALLBACK = 0x04
FRAME_TYPE_UNSOLICITED = 0x08
FRAME_TYPE_ACK = 0x80


ACK = 0x06
NAK = 0x15
CAN = 0x18
SOF = 0x01


REQUEST_FRAMES = []
RESPONSE_FRAMES = []
CALLBACK_FRAMES = []
UNSOLICITED_FRAMES = []

class _FrameMeta(type(ctypes.Structure)):
    frame_type = 0x00
    id = 0x00

    def __eq__(cls, other):  # NOQA
        if isinstance(other, int):
            return cls.id == other
        elif isinstance(other, DATA_FRAME):
            return super().__eq__(other.__class__)

        return False

    def __ne__(cls, other):  # NOQA
        return not cls.__eq__(other)

    def __init__(cls, name, bases, dct):  # NOQA
        super().__init__(name, bases, dct)

        if cls.frame_type & FRAME_TYPE_RESPONSE:
            RESPONSE_FRAMES.append(cls)
        elif cls.frame_type & FRAME_TYPE_CALLBACK:
            CALLBACK_FRAMES.append(cls)
        elif cls.frame_type & FRAME_TYPE_UNSOLICITED:
            UNSOLICITED_FRAMES.append(cls)
        else:
            REQUEST_FRAMES.append(cls)

    def __call__(cls, *args, **kwargs):
        print(args, kwargs)
        return super().__call__(*args, **kwargs)



class DATA_FRAME(ctypes.Structure, metaclass=_FrameMeta):
    id = 0x00
    frame_type = FRAME_TYPE_UNSOLICITED
    _node_id_len = 1

    _fields_ = [
        ('_sof', uint8_t),
        ('_length', uint8_t),
        ('_frame_type', uint8_t),
        ('_command_id', uint8_t),
    ]

    @property
    def node_id_len(self):
        return self._node_id_len

    @node_id_len.setter
    def node_id_len(self, value):
        self._node_id_len = value

    @property
    def payload_length(self):
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, data: bytearray):  # NOQA
        frame_type, length, type_, command_id = data[:4]

        if frame_type & FRAME_TYPE_RESPONSE:
            if command_id in RESPONSE_FRAMES:
                index = RESPONSE_FRAMES.index(command_id)
                frame_cls = RESPONSE_FRAMES[index]
            else:
                raise FrameError
        elif frame_type & FRAME_TYPE_REQUEST:
            if command_id in UNSOLICITED_FRAMES:
                index = UNSOLICITED_FRAMES.index(command_id)
                frame_cls = UNSOLICITED_FRAMES[index]
            elif command_id in CALLBACK_FRAMES:
                index = CALLBACK_FRAMES.index(command_id)
                frame_cls = CALLBACK_FRAMES[index]
            else:
                raise FrameError
        else:
            raise FrameError

        self = frame_cls.from_buffer_copy(data)
        return self

    def to_bytes(self) -> bytearray:
        self._sof = 0x01  # noqa
        if self.frame_type & FRAME_TYPE_RESPONSE:
            self._frame_type = FRAME_TYPE_RESPONSE  # NOQA

        self._length = self.payload_length + 3  # NOQA
        self.__command_id = self.id  # NOQA
        data = bytearray(self)[:self._length + 1]

        checksum = 0xFF
        for item in data[1:]:
            checksum ^ item
        data += bytearray([checksum])

        return data


SOF_TIMEOUT = 1500  # milliseconds

def rx(serial):
    data = bytearray()

    ACK = 0x06
    NAK = 0x15
    CAN = 0x18
    SOF = 0x01

    byte = serial.rx_byte()

    if byte is None:
        return None

    if byte == 0x01:
        data = bytearray([0x01])

        length = None
        while length is None:
            length = serial.rx_byte()

        data += bytearray([length])
        data += bytearray(serial.rx_bytes(length - 1, SOF_TIMEOUT))

        if len(data) - 1 != length:
            return None

        checksum = 0xFF
        for item in data[1:]:
            checksum ^= item

        if checksum != data[-1]:
            return NAK

        return DATA_FRAME.from_bytes(data[:-1])

    return byte


def send_frame(serial, frame: bytearray):
    serial.tx_bytes(frame)

