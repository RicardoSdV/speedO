from collections import deque
from itertools import repeat
from time import time


class Data:
    @property
    def ten(self): return  10
    @property
    def hun(self): return  100
    @property
    def k(self): return    1000
    @property
    def k10(self): return  10000
    @property
    def k100(self): return 100000
    @property
    def M(self): return    1000000
    @property
    def M10(self): return  10000000
    @property
    def M100(self): return 100000000
    @property
    def B(self): return    1000000000

    @property
    def ten_range(self): return  range(self.ten)
    @property
    def hun_range(self): return  range(self.hun)
    @property
    def k_range(self): return    range(self.k)
    @property
    def k10_range(self): return  range(self.k10)
    @property
    def k100_range(self): return range(self.k100)
    @property
    def M_range(self): return    range(self.M)
    @property
    def M10_range(self): return  range(self.M10)
    @property
    def M100_range(self): return range(self.M100)

    @property
    def ten_ints(self): return  list(self.ten_range)
    @property
    def hun_ints(self): return  list(self.hun_range)
    @property
    def k_ints(self): return    list(self.k_range)
    @property
    def k10_ints(self): return  list(self.k10_range)
    @property
    def k100_ints(self): return list(self.k100_range)
    @property
    def M_ints(self): return    list(self.M_range)
    @property
    def M10_ints(self): return  list(self.M10_range)
    @property
    def M100_ints(self): return list(self.M100_range)

    @property
    def ptrn_chars_tup(self): return    ('A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B')
    @property
    def no_ptrn_chars_tup(self): return ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P')
    @property
    def ptrn_chars_lst(self): return    list(self.ptrn_chars_tup)
    @property
    def no_ptrn_chars_lst(self): return list(self.no_ptrn_chars_tup)
    @property
    def ten_chars_str(self): return 'dkdjvns fi'
    @property
    def hun_chars_str(self): return 'dlahbflk dflkhs dfl bflshb qhb flsdbf lksbfel bsfpiwb fskdbj vkcxzbviuwgsf lkubsdkflab osohfvmaskdh'
    @property
    def k_chars_str(self): return self.hun_chars_str * self.k
    @property
    def k__ten_chars(self): return [self.ten_chars_str for _ in repeat(None, self.k)]
    @property
    def k__hun_chars(self): return [self.hun_chars_str for _ in repeat(None, self.k)]

    @property
    def M10__ten_ints(self): return [self.ten_ints for _ in repeat(None, self.M10)]
    @property
    def M__hun_ints(self): return   [self.hun_ints for _ in repeat(None, self.M)]
    @property
    def k100__k_ints(self): return  [self.k_ints for _ in repeat(None, self.k100)]
    @property
    def k10__k10_ints(self): return [self.k10_ints for _ in repeat(None, self.k10)]
    @property
    def k__k100_ints(self): return  [self.k100_ints for _ in repeat(None, self.k)]
    @property
    def hun__M_ints(self): return   [self.M_ints for _ in repeat(None, self.hun)]
    @property
    def ten__M10_ints(self): return [self.M10_ints for _ in repeat(None, self.ten)]

    @property
    def M__ten_ints(self): return    [self.ten_ints for _ in repeat(None, self.M)]
    @property
    def k100__hun_ints(self): return [self.hun_ints for _ in repeat(None, self.k100)]
    @property
    def k10__k_ints(self): return    [self.k_ints for _ in repeat(None, self.k10)]
    @property
    def k__k10_ints(self): return    [self.k10_ints for _ in repeat(None, self.k)]
    @property
    def hun__k100_ints(self): return [self.k100_ints for _ in repeat(None, self.hun)]
    @property
    def ten__M_ints(self): return    [self.M_ints for _ in repeat(None, self.ten)]

    @property
    def k100__ten_ints(self): return [self.ten_ints for _ in repeat(None, self.k100)]
    @property
    def k10__hun_ints(self): return  [self.hun_ints for _ in repeat(None, self.k10)]
    @property
    def k__k_ints(self): return      [self.k_ints for _ in repeat(None, self.k)]
    @property
    def hun__k10_ints(self): return  [self.k10_ints for _ in repeat(None, self.hun)]
    @property
    def ten__k100_ints(self): return [self.k100_ints for _ in repeat(None, self.ten)]

    @property
    def M__ten_ints_deque(self): return    deque(self.M__ten_ints)
    @property
    def k100__hun_ints_deque(self): return deque(self.k100__hun_ints)
    @property
    def k10__k_ints_deque(self): return    deque(self.k10__k_ints)
    @property
    def k__k10_ints_deque(self): return    deque(self.k__k10_ints)
    @property
    def hun__k100_ints_deque(self): return deque(self.hun__k100_ints)
    @property
    def ten__M_ints_deque(self): return    deque(self.ten__M_ints)

    @property
    def slower_3d_list(self):
        return self.M10__ten_ints, self.M__hun_ints, self.k100__k_ints, self.k10__k10_ints, self.k__k100_ints, self.hun__M_ints, self.ten__M10_ints
    @property
    def faster_3d_list(self):
        return self.M__ten_ints, self.k100__hun_ints, self.k10__k_ints, self.k__k10_ints, self.hun__k100_ints, self.ten__M_ints
    @property
    def super_fast_3d_list(self):
        return self.k100__ten_ints, self.k10__hun_ints, self.k__k_ints, self.hun__k10_ints, self.ten__k100_ints

    @property
    def faster_3d_deque(self):
        return self.M__ten_ints_deque, self.k100__hun_ints_deque, self.k10__k_ints_deque, self.k__k10_ints_deque, self.hun__k100_ints_deque, self.ten__M_ints_deque

    @property
    def shuffled_faster_3d_list(self):
        from random import shuffle

        shufflee = self.faster_3d_list
        for outer in shufflee:
            for inner in outer:
                shuffle(inner)

        return shufflee

    @property
    def M_ptrn_chars_lsts(self): return self.ptrn_chars_lst * self.M
    @property
    def M_no_ptrn_chars_lsts(self): return self.no_ptrn_chars_lst * self.M


data = Data()
