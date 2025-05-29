import sys

if sys.version.startswith('2'):
    from zz_py2 import prnt, vzip, vrange
else:
    from zz_py3 import prnt, vzip, vrange


__all__ = ('prnt', 'vzip', 'vrange')
