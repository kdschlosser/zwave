import enum

class _Enum(enum.Enum):

    @staticmethod
    def _name_to_string_(name: str) -> str:
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
    def signal_name(self):
        return self.__class__.__qualname__

    @property
    def label(self):
        return self._name_to_string_(self._name_)

    def __str__(self):
        return self.label


class ReplaceFailedNode:
    class Response:
        class Status(ENUM):
            RemoveStarted = 0x00
            NotPrimaryController = 0x01
            NoCallbackFunction = 0x02
            NotFound = 0x03
            RemoveProcessBusy = 0x04
            RemoveFailed = 0x05

    class Callback:
        class Status(ENUM):







