from itertools import repeat

from src.z_data import data

num = data.M10

class _Tuple(tuple):
    pass

class _SlotyTuple(tuple):
    __slots__ = ()

_list = [1, 2, 3, 4, 5, 6]

def tupleLiteral():
    for _ in repeat(None, num):
        t = (1, 2, 3, 4, 5, 6)
        a, b, c, d, e, f = t



