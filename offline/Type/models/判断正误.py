import inspect
from . import 不定数填空

_map = {
    '不定数填空': '判断正误',
    '填空': '判断正误',
}
_code = inspect.getsource(不定数填空)
for _k, _v in _map.items():
    _code = _code.replace(_k, _v)
exec(_code)
