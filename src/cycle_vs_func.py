"""
For small cycles is it faster to just make a function?
"""
from itertools import repeat, cycle

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10

class _Class(object): pass
obj1 = _Class()
obj2 = _Class()

cycle = cycle((obj1, obj2))

def _func(obj):
    if obj is obj1:
        return obj2
    return obj1


def use_cycle(_cycle=cycle):
    for _ in repeat(None, num):
        obj = next(_cycle)

def use_func(func=_func):
    obj = func(obj1)
    for _ in repeat(None, num):
        obj = func(obj)

auto_tester()


"""
Conclusion:

Python27:
    Name        Secs     %    
    use_func    0.4068   100  
    use_cycle   0.3612   89   
    
Python38:
    Name        Secs     %    
    use_func    0.3071   100  
    use_cycle   0.159    52   
    
Python310:
    Name        Secs     %    
    use_func    0.3764   100  
    use_cycle   0.2575   68   

Python312:
    Name        Secs     %    
    use_func    0.2498   100  
    use_cycle   0.1382   55   
"""

