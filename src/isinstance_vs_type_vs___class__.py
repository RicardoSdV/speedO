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

class _ID(object):
    __slots__ = ()
    id = 1

idObj = _ID()
myID = 1

def do_is_ID(_myID=myID, _idObj=idObj):
    for _ in repeat(None, num):
        _idObj.id is _myID


def do_eq_ID(_myID=myID, _idObj=idObj):
    for _ in repeat(None, num):
        _idObj.id == _myID

auto_tester()


"""
Conclusion:
    - is class best in 27 & 312
    - isinstance best in 38 & 310
    - type always slow
    - In py27 class level ID is best, holds up pretty well in 38, isinstance best for 310, is class wins at 312

Python27:
    Name            Secs     %    
    do_eq_type      0.3094   100  
    do_is_type      0.2798   90   
    do_isinstance   0.2746   89   
    do_eq_class     0.2478   80   
    do_is_class     0.2196   71   
    do_is_ID        0.1808   57   
    do_eq_ID        0.1798   57   
    
Python38:
    Name            Secs     %    
    do_eq_type      0.2184   100  
    do_is_type      0.2079   95   
    do_eq_class     0.1458   67   
    do_eq_ID        0.1355   62   
    do_is_class     0.133    61   
    do_isinstance   0.1274   57   
    do_is_ID        0.1257   57   

Python310:
    Name            Secs     %    
    do_eq_class     0.1854   100  
    do_eq_type      0.1828   99   
    do_eq_ID        0.174    94   
    do_is_class     0.1714   92   
    do_is_type      0.1661   90   
    do_is_ID        0.1649   89   
    do_isinstance   0.137    74   


Python312:
    Name            Secs     %    
    do_eq_type      0.1547   100  
    do_eq_ID        0.1516   98   
    do_is_type      0.1324   86   
    do_is_ID        0.1318   85   
    do_isinstance   0.127    82   
    do_eq_class     0.1246   81   
    do_is_class     0.1022   66   
"""
