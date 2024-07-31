"""
This is to have IPLs compete to see which one is faster on init, i.e. when needing to resize.
"""

from itertools import repeat, islice
from random import choice
from string import printable
from typing import *

from src.z_data import data
from src.z_tester import tester

class IPL:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self):
        self._idx = -1
        self._list = []
        self._len_list = 0  # Yes, faster than len()

    def append(self, element):
        self._idx += 1
        try:
            self._list[self._idx] = element
        except IndexError:
            self._list.append(element)
            self._len_list += 1

    def reset(self):
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = []
        self._len_list = 0
        self._idx = -1

class IPL2:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self):
        self._idx = -1
        self._list = [None]
        self._len_list = 1  # Yes, faster than len()

    def append(self, element):
        self._idx += 1
        try:
            self._list[self._idx] = element
        except IndexError:
            self._len_list *= 2
            self._list.extend(repeat(None, self._len_list))
            self._list[self._idx] = element

    def reset(self):
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = [None]
        self._len_list = 1
        self._idx = -1

class IPL3:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self) -> None:
        self._list: 'List[Any]' = []  # Yes, composition faster than inheritance
        self._len_list = 0  # Yes, faster than len()
        self._idx = -1

    def append(self, element: 'Any') -> None:
        self._idx += 1
        if self._len_list == self._idx:
            self._list.append(element)
            self._len_list += 1
        else:
            self._list[self._idx] = element

    def reset(self) -> 'Iterator[Any]':
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = []
        self._len_list = 0
        self._idx = -1

class IPL4:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self) -> None:
        self._list: 'List[Any]' = [None]  # Yes, composition faster than inheritance
        self._len_list = 1  # Yes, faster than len()
        self._idx = -1

    def append(self, element: 'Any') -> None:
        self._idx += 1
        if self._len_list == self._idx:
            self._len_list *= 2
            self._list.extend(repeat(None, self._len_list))
            self._list[self._idx] = element
        else:
            self._list[self._idx] = element

    def reset(self) -> 'Iterator[Any]':
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = [None]
        self._len_list = 1
        self._idx = -1

class IPL5:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self):
        self._idx = -1
        self._list = [None] * 8
        self._len_list = 8  # Yes, faster than len()

    def append(self, element):
        self._idx += 1
        try:
            self._list[self._idx] = element
        except IndexError:
            self._len_list *= 2
            self._list.extend(repeat(None, self._len_list))
            self._list[self._idx] = element

    def reset(self):
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = [None] * 8
        self._len_list = 8
        self._idx = -1

class FixedIPL:
    __slots__ = ('_idx', '_list', '_len_list')

    def __init__(self, size):
        self._idx = -1
        self._list = [None] * size
        self._len_list = size  # Yes, faster than len()

    def append(self, element):
        self._idx += 1
        self._list[self._idx] = element

    def reset(self):
        yield from islice(self._list, self._idx+1)
        self._idx = -1

    def clear(self) -> None:
        self._list = [None]
        self._len_list = 1
        self._idx = -1


rep_cnt = data.k100
outer_num = data.hun

lines1 = tuple((''.join(choice(printable) for _ in repeat(None, 120)) for _ in repeat(None, outer_num)))
lines2 = tuple(reversed(lines1))

ipls  = [IPL() for _ in repeat(None, rep_cnt)]
ipls2 = [IPL2() for _ in repeat(None, rep_cnt)]
ipls3 = [IPL3() for _ in repeat(None, rep_cnt)]
ipls4 = [IPL4() for _ in repeat(None, rep_cnt)]
ipls5 = [IPL5() for _ in repeat(None, rep_cnt)]
ipls6 = [FixedIPL(outer_num) for _ in repeat(None, rep_cnt)]


def run_ipl():
    _lines1 = lines1
    for ipl in ipls:
        for line in _lines1: ipl.append(line)

def run_ipl2():
    _lines1 = lines1
    for ipl in ipls:
        for line in _lines1: ipl.append(line)

def run_ipl3():
    _lines1 = lines1

    for ipl in ipls:
        for line in _lines1: ipl.append(line)

def run_ipl4():
    _lines1 = lines1
    for ipl in ipls:
        for line in _lines1: ipl.append(line)

def run_ipl5():
    _lines1 = lines1
    for ipl in ipls5:
        for line in _lines1: ipl.append(line)

def run_ipl6():
    _lines1 = lines1
    for ipl in ipls6:
        for line in _lines1: ipl.append(line)

tester(
    (
        run_ipl,
        run_ipl2,
        run_ipl3,
        run_ipl4,
        run_ipl5,
        run_ipl6,
    ),
    num_repeats=1
)

"""
Conclusion:
    Python310:
        - Main conclusion is that the try: part of the try-except is
        pretty much free, the except: part is not.
        
        - Also the strategy of doubling the list size has a problem,
        the relatively large number of doublings necessary to get the
        list to a relatively . 
        
        - Therefore, the best approach is obviously to use a fixed list
        and know ahead of time the number of elements it will hold, however
        the next best is to use a list that scales through exceptions but that
        is initialised with a certain number of Nones, with an estimate of 
        how big the list will be, but probably aiming to be short rather than
        long and probably always > 8 unless you really know its going to be less 
        than 8
        
        When outer_num elements == 100:
        Testing times mean of 1 rounds: 
        Name       Secs     %    
        run_ipl4   2.1441   100  
        run_ipl3   2.1287   99   
        run_ipl    2.1207   99   
        run_ipl2   2.0268   95   
        run_ipl5   0.7899   37   
        run_ipl6   0.6276   28   
        
        When outer_num elements == 1000:
        Testing times mean of 5 rounds: 
        Name       Secs     %    
        run_ipl4   2.1311   100  
        run_ipl3   2.1299   100  
        run_ipl2   2.112    99   
        run_ipl    2.1056   99   
        run_ipl5   0.7279   34   
        run_ipl6   0.6524   31   

"""

