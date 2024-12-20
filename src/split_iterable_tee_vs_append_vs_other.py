from itertools import tee

from src.z_tester import tester_2d


def _append(outer):
    for inner in outer:
        _list1 = []
        appendToList1 = _list1.append
        _list2 = []
        appendToList2 = _list2.append

        for el in inner:
            if el % 2 == 0:
                appendToList1(el)
            else:
                appendToList2(el)

def _append2(outer):
    for inner in outer:
        _list1 = []
        appendToList1 = _list1.append
        _list2 = []
        appendToList2 = _list2.append

        for el in inner:
            if el % 2 == 0:
                appendToList1(el)
            else:
                appendToList2(el)


def _tee(outer):
    __tee = tee
    for inner in outer:
        iter1, iter2 = __tee(inner)
        _list1 = list((el for el in iter1 if el % 2 == 0))
        _list2 = list((el for el in iter2 if el % 2 != 0))


def _comprehension(outer):
    for inner in outer:
        _list1 = [el for el in inner if el % 2 == 0]
        _list2 = [el for el in inner if el % 2 != 0]


tester_2d(
    (
        _append,
        _tee,
        _comprehension,
    )
)

