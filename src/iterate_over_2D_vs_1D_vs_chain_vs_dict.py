from itertools import repeat, chain

from src.z_data import data
from src.z_tester import tester

list10 = list(range(10))
list2D = [list(list10) for _ in repeat(None, 10)]
list100 = list(range(100))


num = data.M

def iter_1D():
    _list100 = list100
    for _ in repeat(None, num):
        for el in _list100:
            pass

def iter_2D_double_for():
    _list2D = list2D
    for _ in repeat(None, num):
        for inner in _list2D:
            for el in inner:
                pass

def iter_2D_chain():
    _list2D = list2D
    for _ in repeat(None, num):
        for el in chain.from_iterable(_list2D):
            pass


tester(
    (
        iter_1D,
        iter_2D_double_for,
        iter_2D_chain,
    )
)
