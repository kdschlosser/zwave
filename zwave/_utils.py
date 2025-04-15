import enum as _enum
import math as _math


class member(_enum.member):
    """
    Forces item to become an Enum member during class creation.
    """

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if hasattr(self.value, item):
            return getattr(self.value, item)

        raise AttributeError(item)

    def __init__(self, value):
        self.value = value


class ENUM(_enum.Enum):
    _replace = _enum.nonmember(())

    def __getattr__(self, item):
        if item.isupper():
            return getattr(
                self.__class__._member_map_[self._name_].value, item)  # NOQA
        else:
            return _enum.EnumType.__getattr__(self.__class__, item)  # NOQA

    def __call__(self, value):
        membr = self.__class__.__members__[self._name_]

        if isinstance(membr._value_, int):  # NOQA
            return membr

        return membr._value_(value)  # NOQA

    @classmethod
    def _missing_(cls, value):
        for membr in cls.__members__.values():
            try:
                if membr.value.id == value:
                    return membr
            except AttributeError:
                if membr.value == value:
                    return membr

        try:
            return cls.UNKNOWN  # NOQA
        except:  # NOQA
            pass
        try:
            return cls.UNASSIGNED  # NOQA
        except:  # NOQA
            pass

        return cls.GENERIC  # NOQA

    def __str__(self):
        parent = self.__class__.__name__.replace('_', ' ').title()
        name = self._name_.replace('_', ' ').title()

        for text in self._replace:
            parent = parent.replace(text.title(), text)

            if 'Irrigation' not in name:
                name = name.replace(text.title(), text)

        return "%s.%s" % (parent, name)


def int_to_hex(value, num_bits=16):
    return f'0x{hex(value)[2:].zfill(int(_math.ceil(num_bits / 8))).upper()}'


def to_twos_complement(number, bits):
    if number < 0:
        return (1 << bits) + number
    return number


def from_twos_complement(value, bits):
    if value & (1 << (bits - 1)):
        return value - (1 << bits)
    return value


def to_rssi(value: int) -> str:
    if 0x80 <= value <= 0xFF:
        value -= 256
        value = f'{value}dBm'
    elif 0x00 <= value <= 0x7C:
        value = f'+{value}dBm'
    elif value == 0x7D:
        value = '-∞dBm'
    elif value == 0x7E:
        value = '+∞dBm'
    elif value == 0x7F:
        value = None

    return value


def from_rssi(value: str | int) -> int:
    if value is None:
        return None

    if isinstance(value, str):
        value = value.replace('dBm', '')

        if value in ('-∞', '+∞'):
            return None

        value = int(value)

    if value in (0x7D, 0x7E):
        return None

    # clamp the value into the allowed range
    value = max(-128, min(124, value))

    if value < 0:
        value += 256

    return value
