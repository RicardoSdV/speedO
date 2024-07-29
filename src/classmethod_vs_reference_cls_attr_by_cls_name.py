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


num = data.M10
cls = Cls()


def call_cls_meth_load_1_cls_attr():
    for _ in repeat(None, num):
        cls.cls_meth_load_1_cls_attr()

def call_cls_meth_load_5_cls_attr():
    for _ in repeat(None, num):
        cls.cls_meth_load_5_cls_attr()

def call_cls_meth_load_10_cls_attr():
    for _ in repeat(None, num):
        cls.cls_meth_load_10_cls_attr()

def call_stat_meth_load_1_cls_attr():
    for _ in repeat(None, num):
        cls.stat_meth_load_1_cls_attr()

def call_stat_meth_load_5_cls_attr():
    for _ in repeat(None, num):
        cls.stat_meth_load_5_cls_attr()

def call_stat_meth_load_10_cls_attr():
    for _ in repeat(None, num):
        cls.stat_meth_load_10_cls_attr()


tester(
    (
        call_cls_meth_load_1_cls_attr,
        call_cls_meth_load_5_cls_attr,
        call_cls_meth_load_10_cls_attr,
        call_stat_meth_load_1_cls_attr,
        call_stat_meth_load_5_cls_attr,
        call_stat_meth_load_10_cls_attr,
    )
)

"""
Conclusion:
    - What might not be getting captured by this test is for example, 
    if you have three or four methods that call each-other, and they
    are all forced to be class methods just so that one of them can 
    access two or three class attributes, in that case it really might
    be worth it to make them all static.

    Python27:
        - Just use class methods
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   2.0664   100  
        call_cls_meth_load_10_cls_attr    1.756    85   
        call_stat_meth_load_5_cls_attr    1.161    56   
        call_cls_meth_load_5_cls_attr     1.103    53   
        call_cls_meth_load_1_cls_attr     0.5276   26   
        call_stat_meth_load_1_cls_attr    0.5104   25   
        
    Python38:
        - Just use class methods
    
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   1.4435   100  
        call_cls_meth_load_10_cls_attr    1.2949   90   
        call_stat_meth_load_5_cls_attr    0.8767   61   
        call_cls_meth_load_5_cls_attr     0.8243   56   
        call_cls_meth_load_1_cls_attr     0.4183   28   
        call_stat_meth_load_1_cls_attr    0.3913   27   
        
    Python310:
        - Seems that static methods get better an so it might
        be worth it if num cls attr accessed between 1 & 5
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   1.887    100  
        call_cls_meth_load_10_cls_attr    1.8018   95   
        call_cls_meth_load_5_cls_attr     1.0989   57   
        call_stat_meth_load_5_cls_attr    1.0666   56   
        call_cls_meth_load_1_cls_attr     0.5575   30   
        call_stat_meth_load_1_cls_attr    0.4693   25   
        
    Python312:
        - Seems that static methods get better an so it might
        be worth it if num cls attr accessed between 1 & 5
        
        Testing times mean of 5 rounds: 
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   1.246    100  
        call_cls_meth_load_10_cls_attr    1.1326   91   
        call_stat_meth_load_5_cls_attr    0.7617   61   
        call_cls_meth_load_5_cls_attr     0.7616   61   
        call_cls_meth_load_1_cls_attr     0.4212   34   
        call_stat_meth_load_1_cls_attr    0.2966   24   
        
    PyPy313:
        - I think that since the tests perform no work it might be 
        getting optimized out by pypy, bc its too fast
    
        Name                              Secs     %    
        call_stat_meth_load_10_cls_attr   0.0066   100  
        call_cls_meth_load_10_cls_attr    0.0064   97   
        call_stat_meth_load_1_cls_attr    0.0063   96   
        call_cls_meth_load_1_cls_attr     0.0062   94   
        call_cls_meth_load_5_cls_attr     0.0062   94   
        call_stat_meth_load_5_cls_attr    0.0057   86   
"""