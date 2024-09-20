""" How much faster is it to use izip in python27 ??"""
from itertools import repeat, izip

from src.z_data import data
from src.z_tester import tester

tuple1  = (1, )
tuple2  = (1, 2)
tuple4  = (1, 2, 3, 4)
tuple8  = (1, 2, 3, 4, 5, 6, 7, 8)
tuple16 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

num = data.M

def zipTuple1():
    for _ in repeat(None, num):
        for a, b in zip(tuple1, tuple1):
            _a = a
            _b = b

def zipTuple2():
    for _ in repeat(None, num):
        for a, b in zip(tuple2, tuple2):
            _a = a
            _b = b

def zipTuple4():
    for _ in repeat(None, num):
        for a, b in zip(tuple4, tuple4):
            _a = a
            _b = b

def zipTuple8():
    for _ in repeat(None, num):
        for a, b in zip(tuple8, tuple8):
            _a = a
            _b = b

def zipTuple16():
    for _ in repeat(None, num):
        for a, b in zip(tuple16, tuple16):
            _a = a
            _b = b

def izipTuple1():
    for _ in repeat(None, num):
        for a, b in izip(tuple1, tuple1):
            _a = a
            _b = b

def izipTuple2():
    for _ in repeat(None, num):
        for a, b in izip(tuple2, tuple2):
            _a = a
            _b = b

def izipTuple4():
    for _ in repeat(None, num):
        for a, b in izip(tuple4, tuple4):
            _a = a
            _b = b

def izipTuple8():
    for _ in repeat(None, num):
        for a, b in izip(tuple8, tuple8):
            _a = a
            _b = b

def izipTuple16():
    for _ in repeat(None, num):
        for a, b in izip(tuple16, tuple16):
            _a = a
            _b = b


class Class(object):
    from itertools import izip as __izip

    @staticmethod
    def zipTuple1():
        for _ in repeat(None, num):
            for a, b in zip(tuple1, tuple1):
                _a = a
                _b = b

    @staticmethod
    def zipTuple2():
        for _ in repeat(None, num):
            for a, b in zip(tuple2, tuple2):
                _a = a
                _b = b

    @staticmethod
    def zipTuple4():
        for _ in repeat(None, num):
            for a, b in zip(tuple4, tuple4):
                _a = a
                _b = b

    @staticmethod
    def zipTuple8():
        for _ in repeat(None, num):
            for a, b in zip(tuple8, tuple8):
                _a = a
                _b = b

    @staticmethod
    def zipTuple16():
        for _ in repeat(None, num):
            for a, b in zip(tuple16, tuple16):
                _a = a
                _b = b

    @staticmethod
    def izipTuple1():
        for _ in repeat(None, num):
            for a, b in Class.__izip(tuple1, tuple1):
                _a = a
                _b = b

    @staticmethod
    def izipTuple2():
        for _ in repeat(None, num):
            for a, b in Class.__izip(tuple2, tuple2):
                _a = a
                _b = b

    @staticmethod
    def izipTuple4():
        for _ in repeat(None, num):
            for a, b in Class.__izip(tuple4, tuple4):
                _a = a
                _b = b

    @staticmethod
    def izipTuple8():
        for _ in repeat(None, num):
            for a, b in Class.__izip(tuple8, tuple8):
                _a = a
                _b = b

    @staticmethod
    def izipTuple16():
        for _ in repeat(None, num):
            for a, b in Class.__izip(tuple16, tuple16):
                _a = a
                _b = b

tester(
    (
        zipTuple1,
        zipTuple2,
        zipTuple4,
        zipTuple8,
        zipTuple16,
        izipTuple1,
        izipTuple2,
        izipTuple4,
        izipTuple8,
        izipTuple16,
    ),
)

tester(
    (
        Class.zipTuple1,
        Class.zipTuple2,
        Class.zipTuple4,
        Class.zipTuple8,
        Class.zipTuple16,
        Class.izipTuple1,
        Class.izipTuple2,
        Class.izipTuple4,
        Class.izipTuple8,
        Class.izipTuple16,
    ),
)

"""
Conclusion:
    - izip just better, I suppose it might have an impact to import an additional 
    name into the namespace to use it only once, maybe?
    
    - Even in the worst case scenario, were you have to access a class attribute
    every time izip is called still stomps normal zip()
    
    Python27:
        Testing times mean of 5 rounds: (Testing Funcs)
        Name          Secs     %    
        zipTuple16    0.5232   100  
        izipTuple16   0.3746   72   
        zipTuple8     0.3336   64   
        izipTuple8    0.2426   46   
        zipTuple4     0.2294   44   
        zipTuple2     0.1798   34   
        izipTuple4    0.1682   32   
        zipTuple1     0.155    30   
        izipTuple2    0.1336   26   
        izipTuple1    0.118    23   
        
        Testing times mean of 5 rounds:  (Testing static meths)
        Name          Secs     %    
        zipTuple16    0.527    100  
        izipTuple16   0.3918   74   
        zipTuple8     0.3374   64   
        izipTuple8    0.2564   49   
        zipTuple4     0.2322   44   
        izipTuple4    0.1838   35   
        zipTuple2     0.1832   35   
        zipTuple1     0.1564   30   
        izipTuple2    0.1464   28   
        izipTuple1    0.1286   24   
"""



