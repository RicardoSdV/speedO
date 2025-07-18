from collections import deque
from functools import partial
from itertools import repeat, cycle
from random import shuffle, randint
from sys import version

if version.startswith('2'):
    from itertools import izip
    verizip = izip
else:
    verizip = zip


def dict_keys(num):
    from itertools import product, islice
    posChars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    def key_generator():
        # Gen infinite unique keys
        length = 1
        while True:
            for combo in product(posChars, repeat=length):
                yield ''.join(combo)
            length += 1

    return islice(key_generator(), num)


def convert_lists_3d_in_place(lists, converter):
    """ Apply the converter function to the innermost list """
    for list_1 in lists:
        for i, list_2 in enumerate(list_1):
            list_1[i] = converter(list_2)
    return lists

def convert_lists_2d_in_place(lists, converter):
    """ Apply the converter function to the innermost list """
    for i, _list in enumerate(lists):
        lists[i] = converter(_list)
    return lists

def reverse_inner_of_3d_in_place(list3d):
    for outer in list3d:
        for inner in outer:
            inner.reverse()

def inner_to_iter_of_2d(outer):
    result = []
    for inner in outer:
        result.append(iter(inner))
    return result


class Data:
    @property
    def zero(self): return 0
    @property
    def one (self): return 1
    @property
    def two (self): return 2
    @property
    def five(self): return 5
    @property
    def six (self): return 6
    @property
    def ten (self): return 10
    @property
    def hun (self): return 100
    @property
    def k   (self): return 1000
    @property
    def k10 (self): return 10000
    @property
    def k100(self): return 100000
    @property
    def M   (self): return 1000000
    @property
    def M10 (self): return 10000000
    @property
    def M100(self): return 100000000
    @property
    def B   (self): return 1000000000

    @property
    def one_range (self): return range(self.one)
    @property
    def two_range (self): return range(self.two)
    @property
    def five_range(self): return range(self.five)
    @property
    def six_range(self):  return range(self.six)
    @property
    def ten_range (self): return range(self.ten)
    @property
    def hun_range (self): return range(self.hun)
    @property
    def k_range   (self): return range(self.k)
    @property
    def k10_range (self): return range(self.k10)
    @property
    def k100_range(self): return range(self.k100)
    @property
    def M_range   (self): return range(self.M)
    @property
    def M10_range (self): return range(self.M10)
    @property
    def M100_range(self): return range(self.M100)

    @property
    def one_ints (self): return list(self.one_range)
    @property
    def two_ints (self): return list(self.two_range)
    @property
    def five_ints(self): return list(self.five_range)
    @property
    def six_ints(self):  return list(self.six_range)
    @property
    def ten_ints (self): return list(self.ten_range)
    @property
    def hun_ints (self): return list(self.hun_range)
    @property
    def k_ints   (self): return list(self.k_range)
    @property
    def k10_ints (self): return list(self.k10_range)
    @property
    def k100_ints(self): return list(self.k100_range)
    @property
    def M_ints   (self): return list(self.M_range)
    @property
    def M10_ints (self): return list(self.M10_range)
    @property
    def M100_ints(self): return list(self.M100_range)

    @property
    def six_ints_tup(self): return tuple(self.six_range)

    @property
    def M10__six_int_lists (self): return [self.six_ints     for _ in repeat(None, self.M10)]
    @property
    def M10__six_int_tuples(self): return [self.six_ints_tup for _ in repeat(None, self.M10)]

    @property
    def two_rnd_ints (self): return [randint(self.zero, self.two-1) for _ in repeat(None, self.two)]
    @property
    def ten_rnd_ints (self): return [randint(self.zero, self.ten-1) for _ in repeat(None, self.ten)]
    @property
    def hun_rnd_ints (self): return [randint(self.zero, self.hun-1) for _ in repeat(None, self.hun)]
    @property
    def k_rnd_ints   (self): sm = self.zero; lg = self.k;    return [randint(sm, lg) for _ in repeat(None, lg)]
    @property
    def k10_rnd_ints (self): sm = self.zero; lg = self.k10;  return [randint(sm, lg) for _ in repeat(None, lg)]
    @property
    def k100_rnd_ints(self): sm = self.zero; lg = self.k100; return [randint(sm, lg) for _ in repeat(None, lg)]
    @property
    def M_rnd_ints   (self): sm = self.zero; lg = self.M;    return [randint(sm, lg) for _ in repeat(None, lg)]

    @property
    def two_Nones (self): return [None] * self.two
    @property
    def five_Nones(self): return [None] * self.five
    @property
    def ten_Nones (self): return [None] * self.ten
    @property
    def hun_Nones (self): return [None] * self.hun
    @property
    def k_Nones   (self): return [None] * self.k
    @property
    def k10_Nones (self): return [None] * self.k10
    @property
    def k100_Nones(self): return [None] * self.k100
    @property
    def M_Nones   (self): return [None] * self.M
    @property
    def M10_Nones (self): return [None] * self.M10
    @property
    def M100_Nones(self): return [None] * self.M100

    @property
    def two_item_dict (self): return {k: v for k, v in verizip(dict_keys(self.two) , self.two_range)}
    @property
    def five_item_dict(self): return {k: v for k, v in verizip(dict_keys(self.five), self.five_range)}
    @property
    def ten_item_dict (self): return {k: v for k, v in verizip(dict_keys(self.ten) , self.ten_range)}
    @property
    def hun_item_dict (self): return {k: v for k, v in verizip(dict_keys(self.hun) , self.hun_range)}
    @property
    def k_item_dict   (self): return {k: v for k, v in verizip(dict_keys(self.k)   , self.k_range)}
    @property
    def k10_item_dict (self): return {k: v for k, v in verizip(dict_keys(self.k10) , self.k10_range)}
    @property
    def k100_item_dict(self): return {k: v for k, v in verizip(dict_keys(self.k100), self.k100_range)}
    @property
    def M_item_dict   (self): return {k: v for k, v in verizip(dict_keys(self.M)   , self.M_range)}
    @property
    def M10_item_dict (self): return {k: v for k, v in verizip(dict_keys(self.M10) , self.M10_range)}
    @property
    def M100_item_dict(self): return {k: v for k, v in verizip(dict_keys(self.M100), self.M100_range)}

    @property
    def M10_shuffled_ints(self): _list = self.M10_ints; shuffle(_list); return _list

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
    def hun_chars_str(self): return 'dlahbflk/dflkhs/dfl/bflshb/qhb/flsdbf/lksbfel/bsfpiwb/fskdbj/vkcxzbviuwgsf/lkubsdkflab/osohfvmaskd/'
    @property
    def hun_chars_intern(self): return 'dlahbflk_dflkhs_dfl_bflshb_qhb_flsdbf_lksbfel_bsfpiwb_fskdbj_vkcxzbviuwgsf_lkubsdkflab_osohfvmaskds'
    @property
    def k_chars_str(self): return self.hun_chars_str * self.k
    @property
    def k__ten_chars(self): return [self.ten_chars_str for _ in repeat(None, self.k)]
    @property
    def k__hun_chars(self): return [self.hun_chars_str for _ in repeat(None, self.k)]
    @property
    def k10_hun_chars(self): return [self.hun_chars_str] * self.k10
    @property
    def k100_hun_chars(self): return [self.hun_chars_str] * self.k100

    def yield_hun_chars(self, num):
        hun_chars = self.hun_chars_str
        return (hun_chars for _ in repeat(None, num))

    ## Slower 3d list elements
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

    # Faster 3d list elements
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

    # Super fast 3d list elements
    @property
    def k100__ten_ints(self): return [self.ten_ints  for _ in repeat(None, self.k100)]
    @property
    def k10__hun_ints (self): return [self.hun_ints  for _ in repeat(None, self.k10)]
    @property
    def k__k_ints     (self): return [self.k_ints    for _ in repeat(None, self.k)]
    @property
    def hun__k10_ints (self): return [self.k10_ints  for _ in repeat(None, self.hun)]
    @property
    def ten__k100_ints(self): return [self.k100_ints for _ in repeat(None, self.ten)]

    @property
    def k100__two_ints(self): return [self.two_ints for _ in repeat(None, self.k100)]

    # Faster 3d list of dicts elements
    @property
    def M__two_item_dict   (self): return [self.two_item_dict  for _ in repeat(None, self.M)]
    @property
    def M__five_item_dict  (self): return [self.five_item_dict for _ in repeat(None, self.M)]
    @property
    def M__ten_item_dict   (self): return [self.ten_item_dict  for _ in repeat(None, self.M)]
    @property
    def k100__hun_item_dict(self): return [self.hun_item_dict  for _ in repeat(None, self.k100)]
    @property
    def k10__k_item_dict   (self): return [self.k_item_dict    for _ in repeat(None, self.k10)]
    @property
    def k__k10_item_dict   (self): return [self.k10_item_dict  for _ in repeat(None, self.k)]
    @property
    def hun__k100_item_dict(self): return [self.k100_item_dict for _ in repeat(None, self.hun)]
    @property
    def ten__M_item_dict   (self): return [self.M_item_dict    for _ in repeat(None, self.ten)]

    @property
    def k100__two_rnd_ints(self): return [self.two_rnd_ints for _ in repeat(None, self.k100)]
    @property
    def k100__ten_rnd_ints(self): return [self.ten_rnd_ints for _ in repeat(None, self.k100)]
    @property
    def k100__hun_rnd_ints(self): return [self.hun_rnd_ints for _ in repeat(None, self.k100)]
    @property
    def k10__hun_rnd_ints (self): return [self.hun_rnd_ints for _ in repeat(None, self.k10)]

    @property
    def M__ten_deque   (self): return convert_lists_2d_in_place(self.M__ten_ints, deque)
    @property
    def k100__hun_deque(self): return convert_lists_2d_in_place(self.k100__hun_ints, deque)
    @property
    def k10__k_deque   (self): return convert_lists_2d_in_place(self.k10__k_ints, deque)
    @property
    def k__k10_deque   (self): return convert_lists_2d_in_place(self.k__k10_ints, deque)
    @property
    def hun__k100_deque(self): return convert_lists_2d_in_place(self.hun__k100_ints, deque)
    @property
    def ten__M_deque   (self): return convert_lists_2d_in_place(self.ten__M_ints, deque)

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
        return self.M__ten_deque, self.k100__hun_deque, self.k10__k_deque, self.k__k10_deque, self.hun__k100_deque, self.ten__M_deque

    @property
    def faster_3d_deque_names(self):
        return 'M__ten_deque', 'k100__hun_deque', 'k10__k_deque', 'k__k10_deque', 'hun__k100_deque', 'ten__M_deque'

    @property
    def faster_3d_list_rev_inner(self):
        _list = self.faster_3d_list
        reverse_inner_of_3d_in_place(_list)
        return _list

    @property
    def faster_3d_list_of_dicts(self):  # returns tuple[list[dict[str, int]]]
        return self.M__ten_item_dict, self.k100__hun_item_dict, self.k10__k_item_dict, self.k__k10_item_dict, self.hun__k100_item_dict, self.ten__M_item_dict

    @property
    def faster_3d_list_of_sets(self):  # returns tuple[list[set[int]]]
        faster_3d_list = self.faster_3d_list
        convert_lists_3d_in_place(faster_3d_list, set)
        return faster_3d_list

    @property
    def faster_3d_list_of_deque(self):  # returns tuple[list[deque[int]]]
        faster_3d_list = self.faster_3d_list
        convert_lists_3d_in_place(faster_3d_list, deque)
        return faster_3d_list

    @property
    def faster_3d_list_of_tuple(self):  # returns tuple[list[tuple[int]]]
        faster_3d_list = self.faster_3d_list
        convert_lists_3d_in_place(faster_3d_list, tuple)
        return faster_3d_list

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


def list_of_tuples_of_two_lens_of_rand_ints(num):
    inputs = [];
    append = inputs.append
    ri = partial(randint, 1, 100000)

    for _ in repeat(None, num):
        append((ri(), ri(), ri(), ri()))
        append((ri(), ri(), ri(), ri(), ri(), ri(), ri(), ri()))

    return inputs


def list_of_tuples_of_rand_ints(num):
    inputs = [];
    append = inputs.append
    ri = partial(randint, 1, 100000)

    for _ in repeat(None, num):
        append((ri(), ri(), ri(), ri(), ri(), ri(), ri(), ri()))

    return inputs


def dyn_list_of_list_of_rand_ints(lenOuter, lenInner, minInt=1, maxInt=1000000):
    inputs = [];
    append = inputs.append
    ri = partial(randint, minInt, maxInt)

    for _ in repeat(None, lenOuter):
        append([ri() for _ in repeat(None, lenInner)])

    return inputs

