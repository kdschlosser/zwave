import enum


# This is to override the output when wrapping them in str()
class _EnumMeta(enum.EnumType):

    def __str__(cls):
        return cls.__qualname__


# this is to override the enum container classes when wrapping them in str()
class _HostMeta(type):

    def __str__(cls):
        return cls.__qualname__


# base class for enum container classes
class HOST_CLASS(_HostMeta):
    pass


# base class for enum classes
# this class provides the "label" property which provides
# user friendly text that can be used in a UI
# it also provides the fully qualified name when wrapping in in str()
class HOST_ENUM(enum.Enum, metaclass=_EnumMeta):

    @staticmethod
    def _name_to_string(name: str) -> str:
        res = ''
        last_char = ''

        for char in name:
            res += last_char

            if last_char and not last_char.isupper() and char.isupper():
                res += ' '

            last_char = char

        res += last_char
        return res

    @property
    def label(self):
        return self._name_to_string(self._name_)

    def __str__(self):
        mod_name = self.__class__.__module__.split('.')[-1]

        return f'{mod_name}.{self.__class__.__qualname__}.{self._name_}'
