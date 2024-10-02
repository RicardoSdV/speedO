"""
I need to iterate repeatedly over a number of callables & call them & once in a while
one of those callables might return something that indicates it shouldn't be called
anymore, what is the fastest way of achieving this?
"""
from sys import version
from time import time

from src.z_data import data, convert_lists_2d_in_place
from src.z_tester import tester

if version.startswith('2'):
    from itertools import izip
    verizip = izip
else:
    verizip = zip


k100__two_rnd_ints = data.k100__two_rnd_ints
k100__ten_rnd_ints = data.k100__ten_rnd_ints
k10__hun_rnd_ints = data.k10__hun_rnd_ints


def remove_from_list_2():
    k100__two_ints = data.k100__two_ints

    def inner():
        for struct, els_to_remove in verizip(k100__two_ints, k100__two_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)
                        break

    start = time(); inner(); finish = time()
    return finish - start

def remove_from_list_10():
    k100__ten_ints = data.k100__ten_ints

    def inner():
        for struct, els_to_remove in verizip(k100__ten_ints, k100__ten_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)

    start = time(); inner(); finish = time()
    return finish - start

def remove_from_list_100():
    k10__hun_ints = data.k10__hun_ints

    def inner():
        for struct, els_to_remove in verizip(k10__hun_ints, k10__hun_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)

    start = time(); inner(); finish = time()
    return finish - start


def set_to_none_list_2():
    k100__two_ints = data.k100__two_ints

    def inner():
        for struct, els_to_remove in verizip(k100__two_ints, k100__two_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct[i] = None

    start = time(); inner(); finish = time()
    return finish - start

def set_to_none_list_10():
    k100__ten_ints = data.k100__ten_ints

    def inner():
        for struct, els_to_remove in verizip(k100__ten_ints, k100__ten_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct[i] = None

    start = time(); inner(); finish = time()
    return finish - start

def set_to_none_list_100():
    k10__hun_ints = data.k10__hun_ints

    def inner():
        for struct, els_to_remove in verizip(k10__hun_ints, k10__hun_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct[i] = None

    start = time(); inner(); finish = time()
    return finish - start


def pop_from_list_2():
    k100__two_ints = data.k100__two_ints

    def inner():
        for struct, els_to_remove in verizip(k100__two_ints, k100__two_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct.pop(i)

    start = time(); inner(); finish = time()
    return finish - start

def pop_from_list_10():
    k100__ten_ints = data.k100__ten_ints

    def inner():
        for struct, els_to_remove in verizip(k100__ten_ints, k100__ten_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct.pop(i)

    start = time(); inner(); finish = time()
    return finish - start

def pop_from_list_100():
    k10__hun_ints = data.k10__hun_ints

    def inner():
        for struct, els_to_remove in verizip(k10__hun_ints, k10__hun_rnd_ints):
            for el_to_remove in els_to_remove:
                for i, el in enumerate(struct):
                    if el == el_to_remove:
                        struct.pop(i)

    start = time(); inner(); finish = time()
    return finish - start


def remove_from_set_2():
    k100__two_ints = convert_lists_2d_in_place(data.k100__two_ints, set)

    def inner():
        for struct, els_to_remove in verizip(k100__two_ints, k100__two_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)  # yes, this makes sense, read comment at top of file

    start = time(); inner(); finish = time()
    return finish - start

def remove_from_set_10():
    k100__ten_ints = convert_lists_2d_in_place(data.k100__ten_ints, set)

    def inner():
        for struct, els_to_remove in verizip(k100__ten_ints, k100__ten_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)

    start = time(); inner(); finish = time()
    return finish - start

def remove_from_set_100():
    k10__hun_ints = convert_lists_2d_in_place(data.k10__hun_ints, set)

    def inner():
        for struct, els_to_remove in verizip(k10__hun_ints, k10__hun_rnd_ints):
            for el_to_remove in els_to_remove:
                for el in struct:
                    if el == el_to_remove:
                        struct.remove(el)

    start = time(); inner(); finish = time()
    return finish - start


tester(
    (
        remove_from_list_2,
        set_to_none_list_2,
        pop_from_list_2,
        remove_from_set_2,
    ),
    is_callables_returning_time=True,
)

tester(
    (
        remove_from_list_10,
        set_to_none_list_10,
        pop_from_list_10,
        remove_from_set_10,
    ),
    is_callables_returning_time=True,
)

tester(
    (
        remove_from_list_100,
        set_to_none_list_100,
        pop_from_list_100,
        remove_from_set_100,
    ),
    is_callables_returning_time=True,
)

