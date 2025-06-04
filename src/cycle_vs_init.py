""" Is it faster to create and delete or to modify ?
when only a small % of the object changes?
for dataclasses.
"""
from collections import namedtuple
from itertools import cycle

from src.z_data import data, dyn_list_of_list_of_rand_ints
from src.z_tester import auto_tester

ints = data.M_ints
intss = dyn_list_of_list_of_rand_ints(lenOuter=data.M, lenInner=6)


class _Class(object):
    __slots__ = ('a','b','c','d','e','f')
    def __init__(self, a=1, b=2, c=3, d=4, e=5, f=6):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

obj1 = _Class()
obj2 = _Class()


_NT = namedtuple('NT', ('a','b','c','d','e','f'))
_nt1 = _NT(1,2,3,4,5,6)
_nt2 = _NT(1,2,3,4,5,6)

_cycleObj = cycle((obj1, obj2))
_cycleNT = cycle((_nt1, _nt2))


def use_cycle_obj_change_one(_cycle=_cycleObj):
    for _int in ints:
        obj = next(_cycle)
        obj.a = _int

def use_cycle_NT_change_one(_cycle=_cycleNT):
    for _int in ints:
        nt = next(_cycle)
        nt._replace(a=_int)

def make_new_obj_change_one(Class=_Class):
    for _int in ints:
        obj = _Class(_int)

def make_new_NT_change_one(NT=_NT):
    for _int in ints:
        obj = NT(_int, 2, 3, 4, 5, 6)


def use_cycle_obj_change_six(_cycle=_cycleObj):
    for a, b, c, d, e, f in intss:
        obj = next(_cycle)
        obj.a = a
        obj.b = b
        obj.c = c
        obj.d = d
        obj.e = e
        obj.f = f

def use_cycle_NT_change_six(_cycle=_cycleNT):
    for a, b, c, d, e, f in intss:
        nt = next(_cycle)
        nt._replace(a=a, b=b, c=c, d=d, e=e, f=f)

def make_new_obj_change_six(Class=_Class):
    for a, b, c, d, e, f in intss:
        obj = Class(a, b, c, d, e, f)

def make_new_NT_change_six(NT=_NT):
    for a, b, c, d, e, f in intss:
        obj = NT(a, b, c, d, e, f)



auto_tester(segregator='end')


"""
Conclusion:
If you can reuse objects its always faster, named tuples as proven many times
just suck and this is no exception.

I imagine theres a point where if an object has a large large number of attrs
that change every time, making a new one will converge with reuse.

Python27:
    Name                       Secs     %    
    use_cycle_NT_change_one    0.6432   100  
    make_new_NT_change_one     0.2218   34   
    make_new_obj_change_one    0.1862   28   
    use_cycle_obj_change_one   0.0518   8    
    
    Name                       Secs     %    
    use_cycle_NT_change_six    0.8736   100  
    make_new_NT_change_six     0.2434   28   
    make_new_obj_change_six    0.216    25   
    use_cycle_obj_change_six   0.1342   15   

Python38:
    Name                       Secs     %    
    use_cycle_NT_change_one    0.4223   100  
    make_new_NT_change_one     0.1336   32   
    make_new_obj_change_one    0.1197   28   
    use_cycle_obj_change_one   0.0259   6    
    
    Name                       Secs     %    
    use_cycle_NT_change_six    0.5621   100  
    make_new_obj_change_six    0.1506   27   
    make_new_NT_change_six     0.1503   27   
    use_cycle_obj_change_six   0.0867   15

Python310:
    Name                       Secs     %    
    use_cycle_NT_change_one    0.4508   100  
    make_new_NT_change_one     0.1329   28   
    make_new_obj_change_one    0.1223   27   
    use_cycle_obj_change_one   0.0282   6    
    
    Name                       Secs     %    
    use_cycle_NT_change_six    0.5928   100  
    make_new_obj_change_six    0.1481   25   
    make_new_NT_change_six     0.1475   25   
    use_cycle_obj_change_six   0.0911   15   

Python312:
    Name                       Secs     %    
    use_cycle_NT_change_one    0.4314   100  
    make_new_NT_change_one     0.1535   36   
    make_new_obj_change_one    0.098    23   
    use_cycle_obj_change_one   0.0164   4    
    
    Name                       Secs     %    
    use_cycle_NT_change_six    0.6098   100  
    make_new_NT_change_six     0.159    26   
    make_new_obj_change_six    0.1328   22   
    use_cycle_obj_change_six   0.0496   8     

"""
