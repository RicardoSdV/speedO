from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10

def do_isinstance(_isinstance=isinstance, _int=int, one=1):
    for _ in repeat(None, num):
        _isinstance(one, _int)

def do_is_type(_type=type, _int=int, one=1):
    for _ in repeat(None, num):
        _type(one) is _int

def do_eq_type(_type=type, _int=int, one=1):
    for _ in repeat(None, num):
        _type(one) == _int

def do_is_class(_int=int, one=1):
    for _ in repeat(None, num):
        one.__class__ is _int

def do_eq_class(_int=int, one=1):
    for _ in repeat(None, num):
        one.__class__ == _int


auto_tester()


"""
Conclusion:
    - is class best in 27 & 312
    - isinstance best in 38 & 310
    - type always slow

Python27:
    Name            Secs     %    
    do_eq_type      0.3096   100  
    do_is_type      0.2772   90   
    do_isinstance   0.2712   88   
    do_eq_class     0.2476   80   
    do_is_class     0.2194   71   
    
Python38:
    Name            Secs     %    
    do_eq_type      0.2173   100  
    do_is_type      0.2018   93   
    do_eq_class     0.1441   66   
    do_is_class     0.1323   61   
    do_isinstance   0.1251   57   

Python310:
    Name            Secs     %    
    do_eq_class     0.1821   100  
    do_eq_type      0.1795   99   
    do_is_class     0.1676   92   
    do_is_type      0.1643   90   
    do_isinstance   0.1356   75   

Python312:
    Name            Secs     %    
    do_eq_type      0.1513   100  
    do_is_type      0.1306   86   
    do_isinstance   0.1237   82   
    do_eq_class     0.122    81   
    do_is_class     0.1017   67   
"""
