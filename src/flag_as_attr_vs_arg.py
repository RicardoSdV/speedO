"""
Lets' say I have a method that receives a flag as an arg, and this method uses a for loop which calls another
method in the same class, and this other method uses the flag passed to the first method. Is it better to set
this flag as an attr of the class and access it from the nested method or to pass it as an arg to it.
"""
from itertools import repeat, cycle

from src.z_data import data
from src.z_tester import tester

k = data.k
k10 = data.k100

class Cls(object):
    def __init__(self):
        self.flag = False

    def nested_meth_with_attr_flag(self):
        if self.flag is True:
            return False
        else: return True

    def nested_meth_with_arg_flag(self, flag):
        if flag is True:
            return False
        else: return True

    def caller_of_attr_flag_meth(self):
        self.nested_meth_with_attr_flag()

    def caller_of_arg_flag_meth(self, flag):
        self.nested_meth_with_arg_flag(flag)

    def meth_that_sets_attr_flag(self, flag):
        self.flag = flag
        for _ in repeat(None, k):
            self.nested_meth_with_attr_flag()

    def meth_that_calls_with_arg_flag(self, flag):
        for _ in repeat(None, k):
            self.nested_meth_with_arg_flag(flag)

    def meth_that_sets_attr_flag2(self, flag):
        self.flag = flag
        for _ in repeat(None, k):
            self.caller_of_attr_flag_meth()

    def meth_that_calls_with_arg_flag2(self, flag):
        for _ in repeat(None, k):
            self.caller_of_arg_flag_meth(flag)


obj = Cls()

def attr_flag():
    alternating = cycle((True, False))
    for flag, _ in zip(alternating, repeat(None, k10)):
        obj.meth_that_sets_attr_flag(flag)


def arg_flag():
    alternating = cycle((True, False))
    for flag, _ in zip(alternating, repeat(None, k10)):
        obj.meth_that_calls_with_arg_flag(flag)


def attr_flag2():
    alternating = cycle((True, False))
    for flag, _ in zip(alternating, repeat(None, k10)):
        obj.meth_that_sets_attr_flag2(flag)


def arg_flag2():
    alternating = cycle((True, False))
    for flag, _ in zip(alternating, repeat(None, k10)):
        obj.meth_that_calls_with_arg_flag2(flag)


if __name__ == '__main__':
    tester(
        (
            attr_flag,
            arg_flag,
            attr_flag2,
            arg_flag2,
        ),
        testing_what='times'
    )
    tester(
        (
            attr_flag,
            arg_flag,
            attr_flag2,
            arg_flag2,
        ),
        testing_what='memories'
    )