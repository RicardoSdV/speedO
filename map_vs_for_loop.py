"""
map() makes list in python27, makes map object which is like gen in python 3
"""

from z_tester import tester

many_nums_list = [i for i in range(10000000)]
small_nums_list = [i for i in range(100)]


def add_one_to_small_nums_list_with_map():
    for i in range(100000):
        res = map(lambda n: n + 1, small_nums_list)

    if not isinstance(res, list):
        for r in res:
            a = r


def add_one_to_small_nums_list_with_for_make_list():
    for i in range(100000):
        res = [n + 1 for n in small_nums_list]


def add_one_to_small_nums_list_with_for_make_gen():
    for i in range(100000):
        res = (n + 1 for n in small_nums_list)

    for r in res:
        a = r


def add_one_to_large_nums_list_with_map():
    res = map(lambda n: n + 1, many_nums_list)

    if not isinstance(res, list):
        for r in res:
            a = r


def add_one_to_large_nums_list_with_for_make_list():
    res = [n + 1 for n in many_nums_list]


def add_one_to_large_nums_list_with_for_make_gen():
    res = (n + 1 for n in many_nums_list)
    for v in res:
        a = v


tester(
    [
        add_one_to_small_nums_list_with_map,
        add_one_to_small_nums_list_with_for_make_list,
        add_one_to_small_nums_list_with_for_make_gen,
        add_one_to_large_nums_list_with_map,
        add_one_to_large_nums_list_with_for_make_list,
        add_one_to_large_nums_list_with_for_make_gen
    ])

"""
Conclusion: 

    Python27 - map seems to suck, just use list comprehension
    
    Python38 - Map seems to be great, for small lists, less better for larger ones

"""
