from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Example(object):
    def __init__(self):
        self.attr = []
        self.append_to_attr = self.attr.append

    def meth_append_to_attr(self):
        for _ in repeat(None, num):
            self.attr.append(None)

    def meth_append_attr(self):
        for _ in repeat(None, num):
            self.append_to_attr(None)

example = Example()
num = data.M10

def append_to_attr():
    for _ in repeat(None, num):
        example.attr.append(None)

def append_attr():
    for _ in repeat(None, num):
        example.append_to_attr(None)

tester(
    (
        append_attr,
        append_to_attr,
        example.meth_append_to_attr,
        example.meth_append_attr,
    )
)
