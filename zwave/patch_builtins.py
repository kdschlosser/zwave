import builtins

from . import PATCH_HEX


if PATCH_HEX:
    _hex_ = builtins.hex


    def _hex(obj):
        try:
            return obj.__hex__()

        except TypeError:
            return obj.__hex__(obj)
        except AttributeError:
            pass

        return _hex_(obj)

    builtins.hex = _hex
