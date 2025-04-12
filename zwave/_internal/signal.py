import inspect


_signals = {}


class RegisteredSignal:

    def __init__(self, name, target_func, callback_func, **kwargs):
        self.__name = name
        self.__oneshot = False
        self.__callback_func = callback_func
        self.__kwargs = kwargs

        self.__sig = inspect.signature(target_func)

    def __call__(self, ret, **kwargs):
        for key, value in self.__kwargs.items():
            if key not in kwargs:
                break

            if value != kwargs[key]:
                break
        else:
            self.__callback_func(self.name, ret, **kwargs)
            return True

        return False

    @property
    def name(self):
        return self.__name

    @property
    def oneshot(self):
        return self.__oneshot

    @oneshot.setter
    def oneshot(self, value):
        self.__oneshot = value


_signal_mapping = {}


def register(name_or_func, **kwargs):
    def wrapper(func):
        signal_func = None

        if isinstance(name_or_func, str):
            signal_name = name_or_func

            if name_or_func in _signal_mapping:
                signal_func = _signal_mapping[name_or_func]

        elif isinstance(name_or_func, SignalWrapper):
            signal_name = name_or_func.name
            signal_func = name_or_func
        else:
            signal_name = f'{name_or_func.__module__}.{name_or_func.__qualname__}'
            signal_func = name_or_func

        if signal_name not in _signals:
            _signals[signal_name] = []

        wrapper_func = RegisteredSignal(signal_name, signal_func, func, **kwargs)

        _signals[signal_name].append(wrapper_func)

        return wrapper_func

    return wrapper


class SignalWrapper:

    def __init__(self, name, func):
        self.__name = name
        self.__func = func
        sig = inspect.signature(func)
        target_params = sig.parameters.values()
        self.__target_args = [arg for arg in target_params
                              if arg.kind == arg.POSITIONAL_OR_KEYWORD]

    @property
    def name(self):
        return self.__name

    def __call__(self, *args, **kwargs):
        for i, arg in enumerate(args):
            kwargs[self.__target_args[i].name] = arg

        for arg in self.__target_args[len(args):]:
            if arg.name not in kwargs and arg.default != arg.empty:
                kwargs[arg.name] = arg.default

        ret = self.__func(**kwargs)

        for cb in _signals[self.name][:]:
            if cb(ret, **kwargs) and cb.oneshot:
                _signals[self.name].remove(cb)

        return ret


def new(name=None):
    name = name

    def wrapper(func):
        if name is None:
            signal_name = f'{func.__module__}.{func.__qualname__}'
        else:
            signal_name = name

        if signal_name not in _signal_mapping:
            _signal_mapping[signal_name] = func

        if signal_name not in _signals:
            _signals[signal_name] = []

        return SignalWrapper(signal_name, func)

    return wrapper


# ******************  example use  ***************************
#
# @new('TestClass')
# class TestClass:
#
#     def __init__(self, arg1, arg2, arg3, arg4=15):
#         print('INIT CALLED:', arg1, arg2, arg3, arg4)
#         pass
#
#
# @register('TestClass', arg2=123, arg4=15)
# def test_func(s_name, ret, arg1, arg2, arg3, arg4):
#     print('SIGNAL CALLED:', s_name, ret, arg1, arg2, arg3, arg4)
#
#
# test_func.oneshot = True
#
#
# tc = TestClass(1, 1, 5, 9)
# tc = TestClass(1, 123, 5,)
# tc = TestClass(1, 123, 5,)
