""" Are class methods worth it? """
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

class Cls(object):
    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    num5 = 5
    num6 = 6
    num7 = 7
    num8 = 8
    num9 = 9
    num10 = 10

    def __init__(self):
        self._num1 = 1
        self._num2 = 2
        self._num3 = 3
        self._num4 = 4
        self._num5 = 5
        self._num6 = 6
        self._num7 = 7
        self._num8 = 8
        self._num9 = 9
        self._num10 = 10

    @classmethod
    def cls_meth_load_1_cls_attr(cls):
        num1 = cls.num1

    @classmethod
    def cls_meth_load_5_cls_attr(cls):
        num1, num2, num3, num4, num5 = cls.num1, cls.num2, cls.num3, cls.num4, cls.num5

    @classmethod
    def cls_meth_load_10_cls_attr(cls):
        num1, num2, num3, num4, num5 = cls.num1, cls.num2, cls.num3, cls.num4, cls.num5
        num6, num7, num8, num9, num10 = cls.num6, cls.num7, cls.num8, cls.num9, cls.num10

    @staticmethod
    def stat_meth_load_1_cls_attr():
        num1 = Cls.num1

    @staticmethod
    def stat_meth_load_5_cls_attr():
        num1, num2, num3, num4, num5 = Cls.num1, Cls.num2, Cls.num3, Cls.num4, Cls.num5

    @staticmethod
    def stat_meth_load_10_cls_attr():
        num1, num2, num3, num4, num5 = Cls.num1, Cls.num2, Cls.num3, Cls.num4, Cls.num5
        num6, num7, num8, num9, num10 = Cls.num6, Cls.num7, Cls.num8, Cls.num9, Cls.num10

    def ins_meth_load_1_ins_attr(self):
        num1 = self._num1

    def ins_meth_load_5_ins_attr(self):
        num1, num2, num3, num4, num5 = self._num1, self._num2, self._num3, self._num4, self._num5

    def ins_meth_load_10_ins_attr(self):
        num1, num2, num3, num4, num5 = self._num1, self._num2, self._num3, self._num4, self._num5
        num6, num7, num8, num9, num10 = self._num6, self._num7, self._num8, self._num9, self._num10


num = data.M10
obj = Cls()


def call_cls_meth_load_1_cls_attr():
    for _ in repeat(None, num):
        obj.cls_meth_load_1_cls_attr()

def call_cls_meth_load_5_cls_attr():
    for _ in repeat(None, num):
        obj.cls_meth_load_5_cls_attr()

def call_cls_meth_load_10_cls_attr():
    for _ in repeat(None, num):
        obj.cls_meth_load_10_cls_attr()

def call_stat_meth_load_1_cls_attr():
    for _ in repeat(None, num):
        obj.stat_meth_load_1_cls_attr()

def call_stat_meth_load_5_cls_attr():
    for _ in repeat(None, num):
        obj.stat_meth_load_5_cls_attr()

def call_stat_meth_load_10_cls_attr():
    for _ in repeat(None, num):
        obj.stat_meth_load_10_cls_attr()

def call_ins_meth_load_1_ins_attr():
    for _ in repeat(None, num):
        obj.ins_meth_load_1_ins_attr()

def call_ins_meth_load_5_ins_attr():
    for _ in repeat(None, num):
        obj.ins_meth_load_5_ins_attr()

def call_ins_meth_load_10_ins_attr():
    for _ in repeat(None, num):
        obj.ins_meth_load_10_ins_attr()


tester(
    (
        call_cls_meth_load_1_cls_attr,
        call_stat_meth_load_1_cls_attr,
        call_ins_meth_load_1_ins_attr,
    ),
    print_rounds=False
)
tester(
    (
        call_cls_meth_load_5_cls_attr,
        call_stat_meth_load_5_cls_attr,
        call_ins_meth_load_5_ins_attr,
    ),
    print_rounds=False
)
tester(
    (
        call_cls_meth_load_10_cls_attr,
        call_stat_meth_load_10_cls_attr,
        call_ins_meth_load_10_ins_attr,
    ),
    print_rounds=False
)

"""
Conclusion:
    - In general if you can make something an instance attr is going to
    be faster in python >= 310, although, might be some hidden costs to 
    passing "self" around redundantly, must investigate how that works
    
    - What might not be getting captured by this test is, for example, 
    if you have three or four methods that call each-other, and they
    are all forced to be class methods just so that one of them can 
    access two or three class attributes, in that case it really might
    be worth it to make them all static in python <= 38

    Python27:
        - Just use class methods
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_ins_meth_load_1_ins_attr    0.646    100  
        call_cls_meth_load_1_cls_attr    0.6082   94   
        call_stat_meth_load_1_cls_attr   0.5816   90   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_ins_meth_load_5_ins_attr    1.3782   100  
        call_stat_meth_load_5_cls_attr   1.249    91   
        call_cls_meth_load_5_cls_attr    1.195    87   
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_ins_meth_load_10_ins_attr    2.2054   100  
        call_stat_meth_load_10_cls_attr   2.1628   98   
        call_cls_meth_load_10_cls_attr    1.8752   85   
        
    Python38:
        - Just use class methods
    
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_cls_meth_load_1_cls_attr    0.433    100  
        call_ins_meth_load_1_ins_attr    0.4176   96   
        call_stat_meth_load_1_cls_attr   0.4087   94   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_stat_meth_load_5_cls_attr   0.8725   100  
        call_ins_meth_load_5_ins_attr    0.8516   98   
        call_cls_meth_load_5_cls_attr    0.8377   96   
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_ins_meth_load_10_ins_attr    1.4397   100  
        call_stat_meth_load_10_cls_attr   1.4097   98   
        call_cls_meth_load_10_cls_attr    1.3706   95   
        
    Python310:
        - Seems that static methods get better an so it might
        be worth it if outer_num self attr accessed between 1 & 5
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_cls_meth_load_1_cls_attr    0.5994   100  
        call_stat_meth_load_1_cls_attr   0.4964   83   
        call_ins_meth_load_1_ins_attr    0.4547   76   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_stat_meth_load_5_cls_attr   1.9873   100  
        call_cls_meth_load_5_cls_attr    1.923    97   
        call_ins_meth_load_5_ins_attr    1.8185   92   
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   2.5458   100  
        call_cls_meth_load_10_cls_attr    2.4722   97   
        call_ins_meth_load_10_ins_attr    1.8182   71   
        
    Python312:
        - Seems that static methods get better an so it might
        be worth it if outer_num self attr accessed between 1 & 5
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_cls_meth_load_1_cls_attr    0.4176   100  
        call_stat_meth_load_1_cls_attr   0.2902   69   
        call_ins_meth_load_1_ins_attr    0.2376   56   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_cls_meth_load_5_cls_attr    0.7735   100  
        call_stat_meth_load_5_cls_attr   0.7549   98   
        call_ins_meth_load_5_ins_attr    0.5825   75   
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   1.2241   100  
        call_cls_meth_load_10_cls_attr    1.1285   92   
        call_ins_meth_load_10_ins_attr    0.8962   73   
        
    PyPy313:
        - I think that since the tests perform no work it might be 
        getting optimized out by pypy, bc its too fast
    
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_cls_meth_load_1_cls_attr    0.007    100  
        call_stat_meth_load_1_cls_attr   0.0068   97   
        call_ins_meth_load_1_ins_attr    0.0064   91   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        call_ins_meth_load_5_ins_attr    0.0072   100  
        call_stat_meth_load_5_cls_attr   0.0062   86   
        call_cls_meth_load_5_cls_attr    0.0062   86   
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_ins_meth_load_10_ins_attr    0.0072   100  
        call_cls_meth_load_10_cls_attr    0.0066   92   
        call_stat_meth_load_10_cls_attr   0.006    83   
"""
