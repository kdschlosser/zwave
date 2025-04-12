
class _ValueStringMeta(type):
    """
    This metaclass is used so a subclass of class that uses this metaclass
    is able to do equality testing between an instance of that subclass and
    other subclasses/instances of other subclasses

    ..code-block:python

        class ZwaveAlarmType(StringValue):
            pass


        class ZwaveAlarmTypeReserved(ZwaveAlarmType):
            value = 0x00
            label = 'Reserved'
            version = 1


        class ZwaveAlarmTypeSmoke(ZwaveAlarmType):
            value = 0x01
            label = 'Smoke'
            version = 1


        print(ZwaveAlarmTypeReserved == ZwaveAlarmTypeReserved)  # True
        print(ZwaveAlarmTypeReserved == ZwaveAlarmTypeSmoke)  # False

        print(ZwaveAlarmTypeReserved == 0x01)  # False
        print(ZwaveAlarmTypeReserved == 0x00)  # True

        print(0x01 == ZwaveAlarmTypeReserved)  # False
        print(0x00 == ZwaveAlarmTypeReserved)  # True

        print(ZwaveAlarmTypeReserved == 'Smoke')  # False
        print(ZwaveAlarmTypeReserved == 'Reserved')  # True

        print('Smoke' == ZwaveAlarmTypeReserved)  # False
        print('Reserved' == ZwaveAlarmTypeReserved)  # True

        print(int(ZwaveAlarmTypeSmoke))  # 1
        print(hex(ZwaveAlarmTypeSmoke))  # 0x1 or 0x01 if using the hex patch
        print(ZwaveAlarmTypeSmoke)  # 'Smoke'
    """

    value = 0x00
    label = ''
    version = 0x00

    def __bool__(cls) -> bool:
        return bool(cls.value)

    def __eq__(
        cls,
        other: Union[int, str, "ValueString", "_ValueStringMeta"]
    ) -> bool:

        if isinstance(other, int):
            return other == cls.value

        if isinstance(other, str):
            return other == cls.label

        try:
            # check to see if the comparison object is a subclass of the class
            # that subclassed CCValue
            if issubclass(other, cls.__mro__[-3]):
                return (
                    other.version >= cls.version and  # NOQA
                    other.value == cls.value  # NOQA
                )
        except TypeError:
            pass

        # check to see if the comparison object is an instance of the class
        # that subclassed CCValue
        try:
            if isinstance(other, cls.__mro__[-3]):
                return (
                    other.cc.version >= cls.version and  # NOQA
                    other.value == cls.value  # NOQA
                )
        except TypeError:
            pass

        return False

    def __ne__(
        cls,
        other: Union[int, str, "ValueString", "_ValueStringMeta"]
    ) -> bool:

        return not cls.__eq__(other)

    def __str__(cls) -> str:
        return cls.label

    def __int__(cls) -> int:
        return cls.value

    def __index__(cls) -> int:
        return cls.value

    def __hex__(cls) -> str:
        val = hex(cls.value)[2:]
        if len(val) % 2:
            val = f'0{val}'

        return f'0x{val.upper()}'


class ValueString(metaclass=_ValueStringMeta):
    """
    Base class for string values

    This class works in combination with py:class:`_StringValueMeta`
    to allow for complex equality testing.

    This class gets subclassed by a class that represets a group of string values.
    When a response is received a comparison is done to determine the correct
    string value. That string value is then constructed passing the command class
    instance to it.

    ..code-block:python

        class ZwaveAlarmType(StringValue):
            pass


        class ZwaveAlarmTypeReserved(ZwaveAlarmType):
            value = 0x00
            label = 'Reserved'
            version = 1


        class ZwaveAlarmTypeSmoke(ZwaveAlarmType):
            value = 0x01
            label = 'Smoke'
            version = 1

        nt1 = ZwaveAlarmTypeReserved(command_class_instance)
        nt2 = ZwaveAlarmTypeSmoke(command_class_instance)
        nt3 = ZwaveAlarmTypeReserved(command_class_instance)

        print(nt1 == nt2)  # False
        print(nt1 == nt3)  # True

        print(nt1 == ZwaveAlarmTypeSmoke)  # False
        print(nt1 == ZwaveAlarmTypeReserved)  # True

        print(ZwaveAlarmTypeSmoke == nt1)  # False
        print(ZwaveAlarmTypeReserved == nt1)  # True

        print(nt1 == 0x01)  # False
        print(nt1 == 0x00)  # True

        print(0x01 == nt1)  # False
        print(0x00 == nt1)  # True

        print(nt1 == 'Smoke')  # False
        print(nt1 == 'Reserved')  # True

        print('Smoke' == nt1)  # False
        print('Reserved' == nt1)  # True

        print(int(nt1))  # 0
        print(hex(nt2))  # 0x1 or 0x01 if using the hex patch
        print(nt1)  # 'Reserved'

    ..see: :py:class:`_StringValueMeta` for more examples of use

    """
    value = 0x00
    label = ''
    version = 0x00

    def __init__(self, cc: "CommandClass", value: Optional[int] = None):
        self.cc = cc
        if value is not None:
            self.value = value

    def __bool__(self) -> bool:
        return bool(self.value)

    def __eq__(
        self,
        other: Union[int, str, "ValueString", "_ValueStringMeta"]
    ) -> bool:
        """
        ..see: :py:class:`StringValue`
        """

        if isinstance(other, int):
            return other == self.value

        if isinstance(other, str):
            return other == self.label

        try:
            # check to see if the comparison object is an instance of the class
            # that subclassed CCValue
            if isinstance(other, self.__class__.__mro__[-3]):
                return (
                    self.cc.version >= other.version and
                    self.value == other.value
                )
        except TypeError:
            pass

        try:
            # check to see if the comparison object is a subclass of the class
            # that subclassed CCValue
            if issubclass(other, self.__class__.__mro__[-3]):
                return (
                    self.cc.version >= other.version and
                    self.value == other.value
                )
        except TypeError:
            pass

        return False

    def __ne__(
        self,
        other: Union[int, str, "ValueString", "_ValueStringMeta"]
    ) -> bool:
        """
        ..see: :py:class:`StringValue`
        """

        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        Wrap an instance of this class in `str` to
        get the label/string of this value
        """
        return self.label

    def __int__(self) -> int:
        """
        Called when builtin `int` class is used on an instance of this class.

        Wrap an instance of this class in `int` to get the underlying raw
        integer value.
        """
        return self.value

    def __index__(self) -> int:
        """
        Called when builtin `hex` function is used on an
        instance of this class.
        """
        return self.value

    def __hex__(self) -> str:
        """
        Only used if `PATCH_HEX` is set to `True`,
        :py:module:`patch_builtins` is imported and the builtin `hex`
        functionm is used on an instance of this class.
        """
        val = hex(self.value)[2:]
        if len(val) % 2:
            val = f'0{val}'

        return f'0x{val.upper()}'