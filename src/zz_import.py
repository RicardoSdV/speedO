import sys

if sys.version.startswith('2'):
    from zz_py2 import prnt, vzip, vrange
    from time import clock
else:
    from zz_py3 import prnt, vzip, vrange
    from time import perf_counter as clock

__all__ = ('prnt', 'vzip', 'vrange', 'clock')
