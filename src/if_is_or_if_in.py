from itertools import repeat

from src.z_data import data
from src.z_tester import tester

repeat_cnt = data.M10

a = 1
b = None

def if_is(__=None):
    for _ in repeat(None, repeat_cnt):
        if a is not None and b is not None:
            continue

def if_in(__=None):
    for _ in repeat(None, repeat_cnt):
        if None in (a, b):
            continue

if __name__ =='__main__':
    tester(
        (
            if_is,
            if_in,
        ),
        testing_what='times'
    )

    tester(
        (
            if_is,
            if_in,
        ),
        testing_what='memories'
    )

