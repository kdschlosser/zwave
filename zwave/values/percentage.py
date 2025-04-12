from typing import Union
import sys


class ValuePercentage(str, int):
    _command_class = None

    @property
    def command_class(self):
        return self._command_class

    @classmethod
    def __new__(cls, *args, **kwargs):
        self = args[0]

        if len(args) > 1:
            value = args[1]
        else:
            value = 0

        if 'command_class' in kwargs:
            command_class = kwargs['command_class']
        else:
            command_class = None

        if isinstance(value, str):
            value = value.replace('%', '')
            value = int(value)
        elif not isinstance(value, int):
            raise TypeError('Incompatable type')

        int.__new__(cls, self, value)
        str.__new__(cls, self, str(value) + '%')
        self._command_class = command_class

    def __bool__(self) -> bool:
        return int.__bool__(self)

    def __eq__(self, other: Union[int, str]) -> bool:
        if isinstance(other, int):
            return int.__eq__(self, other)

        if isinstance(other, str):
            if '%' not in other:
                return str.__eq__(self, str(other) + '%')
            else:
                return str.__eq__(self, str(other))

        return False

    def __ne__(self, other: Union[int, str]) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        Wrap an instance of this class in `str` to
        get the label/string of this value
        """
        return str.__str__(self)

    def __int__(self) -> int:
        """
        Called when builtin `int` class is used on an instance of this class.

        Wrap an instance of this class in `int` to get the underlying raw
        integer value.
        """
        return int.__int__(self)

    def __index__(self) -> int:
        """
        Called when builtin `hex` function is used on an
        instance of this class.
        """
        return int.__index__(self)

    def __hex__(self) -> str:
        """
        Only used if `PATCH_HEX` is set to `True`,
        :py:module:`patch_builtins` is imported and the builtin `hex`
        functionm is used on an instance of this class.
        """
        return f'0x{hex(int(self))[2:].zfill(2).upper()}'

    def __add__(self, other):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real + other.real, command_class=self._command_class)
        if isinstance(other, int):
            return self.real + other
        if isinstance(other, str):
            return str(self) + other

        raise TypeError

    def __radd__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real + self.real)
            str.__new__(other, str(int(other)) + '%')
            return other

        if isinstance(other, (int, float)):
            return other + self.real

        if isinstance(other, str):
            return other + str(self)

        raise TypeError

    def __iadd__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real + other.real)
            str.__new__(self, str(int(self)) + '%')
        elif isinstance(other, int):
            int.__new__(self, self.real + other)
            str.__new__(self, str(int(self)) + '%')
        elif isinstance(other, str):
            str.__new__(self, str(self) + other)
        else:
            raise TypeError

        return self

    def __sub__(self, other):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real - other.real, command_class=self._command_class)

        if isinstance(other, (int, float)):
            return int.__sub__(self, other)

        raise TypeError

    def __rsub__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real - self.real)
            str.__new__(str(int(other)) + '%')
            return other
        if isinstance(other, (int, float)):
            return other - self.real
        else:
            raise TypeError

    def __isub__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real - other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real - other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __mul__(self, other):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real * other.real, command_class=self._command_class)

        if isinstance(other, (int, float)):
            return int.__mul__(self, other)

        raise TypeError

    def __rmul__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real * self.real)
            str.__new__(other, str(int(other)) + '%')
            return other

        if isinstance(other, (int, float)):
            return other * self.real

        raise TypeError

    def __imul__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real * other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real * other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __floordiv__(self, other: int):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real // other.real, command_class=self._command_class)

        if isinstance(other, (int, float)):
            return int.__floordiv__(self, other)

        raise TypeError

    def __rfloordiv__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real // self.real)
            str.__new__(other, str(int(other.real)) + '%')
            return other

        if isinstance(other, (int, float)):
            return other // self.real

        raise TypeError

    def __ifloordiv__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real // other.real)
        elif isinstance(other, (int, float)):
            int.__new__(self, int(self.real // other))
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __truediv__(self, other: int) -> float:
        raise NotImplementedError

    def __rtruediv__(self, other: int) -> float:
        if isinstance(other, (int, float)):
            return other / self.real
        else:
            raise TypeError

    def __itruediv__(self, other):
        raise NotImplementedError

    def __mod__(self, other: int):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real % other.real, command_class=self._command_class)

        if isinstance(other, (int, float)):
            return int.__mod__(self, other)

        raise TypeError

    def __rmod__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real % self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, (int, float)):
            return other % self.real

        raise TypeError

    def __imod__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real % other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real % other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __or__(self, other: int):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real | other.real, command_class=self._command_class)

        if isinstance(other, int):
            return int.__or__(self, other)

        raise TypeError

    def __ror__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real | self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, int):
            return other | self.real

        raise TypeError

    def __ior__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real | other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real | other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __and__(self, other: int):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real & other.real, command_class=self._command_class)

        if isinstance(other, int):
            return int.__and__(self, other)

        raise TypeError

    def __rand__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real & self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, int):
            return other & self.real

        raise TypeError

    def __iand__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real & other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real & other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __xor__(self, other: int):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real ^ other.real, command_class=self._command_class)

        if isinstance(other, int):
            return int.__xor__(self, other)

        raise TypeError

    def __rxor__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real ^ self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, int):
            return other ^ self.real

        raise TypeError

    def __ixor__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real ^ other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real ^ other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __pow__(self, other: int, mod: int | None = None):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(self.real.__pow__(other.real, mod), command_class=self._command_class)

        if isinstance(other, (int, float)):
            return self.real.__pow__(other, mod)

        raise TypeError

    def __ipow__(self, other: int, mod: int | None = None):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real.__pow__(other.real, mod))
            str.__new__(self, str(int(self)) + '%')
            return self

        if isinstance(other, (int, float)):
            int.__new__(self, self.real.__pow__(other, mod))
            str.__new__(self, str(int(self)) + '%')
            return self

        raise TypeError

    def __rpow__(self, other: int, mod: int | None = None):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real.__pow__(self.real, mod))
            str.__new__(other, str(int(self)) + '%')
            return other

        if isinstance(other, (int, float)):
            return other.__rpow__(self.real, mod)

        raise TypeError

    def __lshift__(self, other):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(
                self.real << other.real,
                command_class=self._command_class
            )

        if isinstance(other, int):
            return int.__lshift__(self, other)

        raise TypeError

    def __rlshift__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real << self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, int):
            return other << self.real

        raise TypeError

    def __ilshift__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real << other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real << other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __rshift__(self, other):
        if isinstance(other, ValuePercentage):
            return ValuePercentage(
                self.real >> other.real,
                command_class=self._command_class
            )

        if isinstance(other, int):
            return int.__rshift__(self, other)

        raise TypeError

    def __rrshift__(self, other: int):
        if isinstance(other, ValuePercentage):
            int.__new__(other, other.real >> self.real)
            str.__new__(str(int(other)) + '%')
            return other

        if isinstance(other, int):
            return other >> self.real

        raise TypeError

    def __irshift__(self, other):
        if isinstance(other, ValuePercentage):
            int.__new__(self, self.real >> other.real)
        elif isinstance(other, int):
            int.__new__(self, self.real >> other)
        else:
            raise TypeError

        str.__new__(self, str(int(self)) + '%')
        return self

    def __float__(self):
        return int.__float__(self)

    def __ge__(self, other):
        if isinstance(other, ValuePercentage):
            return int.__ge__(self, other.real)
        if isinstance(other, (int, float)):
            return int.__ge__(self, other)
        if isinstance(other, str):
            return str(self).replace('%', '') >= other.replace('%', '')
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, ValuePercentage):
            return int.__gt__(self, other.real)
        if isinstance(other, (int, float)):
            return int.__gt__(self, other)
        if isinstance(other, str):
            return str(self).replace('%', '') > other.replace('%', '')
        raise TypeError

    def __le__(self, other):
        if isinstance(other, ValuePercentage):
            return int.__le__(self, other.real)
        if isinstance(other, (int, float)):
            return int.__le__(self, other)
        if isinstance(other, str):
            return str(self).replace('%', '') <= other.replace('%', '')
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, ValuePercentage):
            return int.__lt__(self, other.real)
        if isinstance(other, (int, float)):
            return int.__lt__(self, other)
        if isinstance(other, str):
            return str(self).replace('%', '') < other.replace('%', '')
        raise TypeError

    @property
    def real(self) -> int:
        return int.real.fget(self)

    @property
    def imag(self):
        return int.imag.fget(self)

    @property
    def numerator(self) -> int:
        return int.numerator.fget(self)

    @property
    def denominator(self):
        return int.denominator.fget(self)

    def conjugate(self) -> int:
        return int.conjugate(self)

    def bit_length(self) -> int:
        return int.bit_length(self)

    def bit_count(self) -> int:
        return int.bit_count(self)

    if sys.version_info >= (3, 11):
        def to_bytes(self, length=1, byteorder="big", *, signed=False) -> bytes:
            return int.to_bytes(self, length, byteorder, signed=signed)

        @classmethod
        def from_bytes(cls, bytes, byteorder="big", *, signed=False):  # NOQA
            raise NotImplementedError
    else:
        def to_bytes(self, length, byteorder, *, signed=False) -> bytes:  # NOQA
            return int.to_bytes(self, length, byteorder, signed=signed)

        @classmethod
        def from_bytes(cls, bytes, byteorder, *, signed=False):  # NOQA
            raise NotImplementedError

    if sys.version_info >= (3, 12):
        def is_integer(self):
            return int.is_integer(self)
