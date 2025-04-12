from typing import Union

from ..values.string import ValueString
from .. import _utils


class _COMMAND_CLASS_Meta(type):
    id: int = 0x00
    label: str = ''

    _registered = []

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        setattr(cls, 'label', name)
        if bases[0].__name__ == 'COMMAND_CLASS':
            _COMMAND_CLASS_Meta._registered.append(cls)

    def __eq__(
        cls,
        other: Union[int, str, "COMMAND_CLASS", "_COMMAND_CLASS_Meta"]
    ) -> bool:

        if isinstance(other, int):
            return other == cls.id

        if isinstance(other, str):
            return other == cls.label

        try:
            if issubclass(other, COMMAND_CLASS):
                return other.id == cls.id
        except TypeError:
            pass

        try:
            if isinstance(other, COMMAND_CLASS):
                return other.id == cls.id

        except TypeError:
            pass

        return False

    def __ne__(
        cls,
        other: Union[int, str,  "COMMAND_CLASS", "_COMMAND_CLASS_Meta"]
    ) -> bool:

        return not cls.__eq__(other)

    def __str__(cls) -> str:
        return cls.label

    def __int__(cls) -> int:
        return cls.id

    def __index__(cls) -> int:
        return cls.id

    def __hex__(cls) -> str:
        return _utils.int_to_hex(cls.id)

    def from_id(cls, id):
        if id not in _COMMAND_CLASS_Meta._registered:
            raise ValueError(f'Command Class `{_utils.int_to_hex(id)}` not found')

        index = _COMMAND_CLASS_Meta._registered.index(id)
        return _COMMAND_CLASS_Meta._registered[index]


class COMMAND_CLASS(metaclass=_COMMAND_CLASS_Meta):
    id: int = 0x00
    label: str = ''
    _supported_command_classes: list["COMMAND_CLASS"] = []

    @property
    def supported_command_classes(self):
        return self._supported_command_classes[:]

    def __init__(self, com_device, node_id):
        self._com_device = com_device
        self.node_id = node_id
        self.version = 0
        self.name = ''

    def __eq__(
        self,
        other: Union[int, str, "COMMAND_CLASS", "_COMMAND_CLASSMeta"]
    ) -> bool:
        """
        ..see: :py:class:`StringValue`
        """

        if isinstance(other, int):
            return other == self.node_id

        if isinstance(other, str):
            if other == self.name:
                return True

            return other in self._supported_command_classes

        try:
            if (
                not self._supported_command_classes and
                isinstance(other, COMMAND_CLASS)
            ):
                return (
                    self.node_id == other.node_id and
                    self.id == other.id
                )
        except TypeError:
            pass

        try:
            if issubclass(other, COMMAND_CLASS):
                if self._supported_command_classes:
                    return other.id in self._supported_command_classes
                else:
                    return self.id == other.id
        except TypeError:
            pass

        return False

    def __ne__(
        self,
        other: Union[int, str, "COMMAND_CLASS", "_COMMAND_CLASSMeta"]
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
        if self._supported_command_classes:
            return self.node_id
        else:
            return self.id

    def __index__(self) -> int:
        """
        Called when builtin `hex` function is used on an
        instance of this class.
        """
        if self._supported_command_classes:
            return self.node_id
        else:
            return self.id

    def __hex__(self) -> str:
        """
        Only used if `PATCH_HEX` is set to `True`,
        :py:module:`patch_builtins` is imported and the builtin `hex`
        functionm is used on an instance of this class.
        """

        if self._supported_command_classes:
            val = self.node_id
        else:
            val = self.id

        return _utils.int_to_hex(val)


class Command(bytearray):
    version = 0x00
    id = 0x00

    @classmethod
    def is_command(cls, cc: CommandClass, data: bytearray):
        return cc.version >= cls.version and data[0] == cls.id

    def __init__(self, cc: CommandClass):
        self.cc = cc
        super().__init__()



import ctypes

uint8_t = ctypes.c_uint8


class ZW_COMMON_FRAME(ctypes.Structure):
    _CMD = 0x00
    _CC = 0x00

    _fields_ = [
        ('cmdClass', uint8_t),
        ('cmd', uint8_t),
    ]

    def __init__(self):
        super().__init__(cmdClass=self._CC, cmd=self.cmd)

    def __len__(self):
        return 2



__all__ = ('CommandClass', 'Command', 'StringValue')
