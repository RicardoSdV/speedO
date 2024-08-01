"""
The costs of accessing the attributes of certain data structures were tested
& as a complement to that the cost of instantiating said structures will now
be tested too
"""
from collections import namedtuple
from itertools import repeat
from random import randint

from src.z_data import data
from src.z_tester import tester

rnd_rep_cnt = data.k100
rep_cnt = data.M
attr_cnt = 6
rand_range = (0, data.k100)

rand_ints = [[randint(*rand_range) for _ in repeat(None, attr_cnt)] for _ in repeat(None, rep_cnt)]

def instantiate_named_tuples():
    named_tuple = namedtuple('NamedTuple', ('a', 'b', 'c', 'd', 'e', 'f'))
    named_tuples = [named_tuple(a, b, c, d, e, f) for a, b, c, d, e, f in rand_ints]

def instantiate_tuples():
    named_tuples = [(a, b, c, d, e, f) for a, b, c, d, e, f in rand_ints]

def instantiate_dicts():
    dicts = [{'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f} for a, b, c, d, e, f in rand_ints]

def instantiate_lists():
    lists = [[a, b, c, d, e, f] for a, b, c, d, e, f in rand_ints]

def instantiate_object_slots():
    class ClassSlots(object):
        __slots__ = ('a', 'b', 'c', 'd', 'e', 'f')
        def __init__(self, _a, _b, _c, _d, _e, _f):
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
            self.e = _e
            self.f = _f

    objs = [ClassSlots(a, b, c, d, e, f) for a, b, c, d, e, f in rand_ints]

def instantiate_object_no_slots():
    class ClassNoSlots(object):
        def __init__(self, _a, _b, _c, _d, _e, _f):
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
            self.e = _e
            self.f = _f

    objs = [ClassNoSlots(a, b, c, d, e, f) for a, b, c, d, e, f in rand_ints]

def instantiate_object_old_style():
    """ Should perform the same as ClassNoSlots except in python27 """
    class OldStyleClass:
        def __init__(self, _a, _b, _c, _d, _e, _f):
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
            self.e = _e
            self.f = _f

    objs = [OldStyleClass(a, b, c, d, e, f) for a, b, c, d, e, f in rand_ints]

if __name__ == '__main__':
    tester(
        (
            instantiate_named_tuples,
            instantiate_tuples,
            instantiate_dicts,
            instantiate_lists,
            instantiate_object_slots,
            instantiate_object_no_slots,
            # instantiate_object_old_style,
        ),
    )
    tester(
        (
            instantiate_named_tuples,
            instantiate_tuples,
            instantiate_dicts,
            instantiate_lists,
            instantiate_object_slots,
            instantiate_object_no_slots,
            # instantiate_object_old_style,
        ),
        testing_what='memories'
    )

"""
Conclusion:
    - To be fair, I picked 6 attrs on purpose bc these are the object sizes:
           Python 2.7             Python 3.6
    attrs  __slots__  __dict__    __slots__  __dict__
    none   16         56 + 272    16         56 + 112
    one    48         56 + 272    48         56 + 112
    two    56         56 + 272    56         56 + 112
    six    88         56 + 1040   88         56 + 152
    11     128        56 + 1040   128        56 + 240
    22     216        56 + 3344   216        56 + 408     
    43     384        56 + 3344   384        56 + 752
    
    - But also to be fair, the size of __dict__ specially in python27 is crazy big

    Python27:
        - Most time & memory efficient is tuple
         
        - If you need attr names, fastest is dict, although, very close to object with __slots__ 
        & namedtuple. However, most memory efficient is namedtuple, although very close to 
        object with __slots__, dict is memory hungry though. Best middle ground is between 
        namedtuple & object with __slots__, although do check attr access costs!
        
        Testing times mean of 5 rounds: 
        Name                           Secs     %    
        instantiate_object_old_style   0.9216   100  
        instantiate_object_no_slots    0.8964   97   
        instantiate_named_tuples       0.6104   66   
        instantiate_object_slots       0.5074   55   
        instantiate_dicts              0.4862   53   
        instantiate_lists              0.3768   41   
        instantiate_tuples             0.104    11   
    
        Testing memories mean of 5 rounds: 
        Name                           Mibs       %    
        instantiate_object_old_style   930.5547   100  
        instantiate_dicts              875.543    94   
        instantiate_object_no_slots    853.6445   92   
        instantiate_object_slots       18.2617    2    
        instantiate_lists              13.0938    1    
        instantiate_named_tuples       12.3711    1    
        instantiate_tuples             7.6328     1    
    
    Python38:
        - Fastest no attr names tuple
        - Fastest with attr names dict
        
        - Least mem is object with slots
        - A balance is complicated
    
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        instantiate_object_no_slots   0.5389   100  
        instantiate_named_tuples      0.4976   92   
        instantiate_object_slots      0.4911   91   
        instantiate_lists             0.3769   70   
        instantiate_dicts             0.1856   34   
        instantiate_tuples            0.0896   17   
        
        Testing memories mean of 5 rounds: 
        Name                          Mibs       %    
        instantiate_dicts             345.418    100  
        instantiate_object_no_slots   145.7812   42   
        instantiate_tuples            84.8516    25   
        instantiate_named_tuples      72.3477    21   
        instantiate_lists             71.5273    21   
        instantiate_object_slots      56.9805    16   

    Python310:
        - Fastest is tuple
        - Fastest with attr names is dict
        
        - Least mem is object with slots
        - A balance is complicated
    
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        instantiate_named_tuples      0.4997   100  
        instantiate_object_no_slots   0.4929   99   
        instantiate_object_slots      0.4494   90   
        instantiate_lists             0.3353   67   
        instantiate_dicts             0.1924   39   
        instantiate_tuples            0.0901   18   
        
        Testing memories mean of 5 rounds: 
        Name                          Mibs       %    
        instantiate_dicts             294.9414   100  
        instantiate_object_no_slots   119.8867   41   
        instantiate_tuples            74.6484    25   
        instantiate_named_tuples      74.5586    25   
        instantiate_lists             72.1523    24   
        instantiate_object_slots      54.2383    18   
        
    Python312:
        - Fastest is tuple
        - Fastest with attr names is dict
        
        - Least mem is object with __slots__
        - Most mem by far is dict
        
        - Balance difficult but maybe object with slots?
    
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        instantiate_named_tuples      0.4907   100  
        instantiate_object_no_slots   0.4253   87   
        instantiate_object_slots      0.4141   84   
        instantiate_lists             0.3631   74   
        instantiate_dicts             0.1703   35   
        instantiate_tuples            0.0883   18   
        
        Testing memories mean of 5 rounds: 
        Name                          Mibs       %    
        instantiate_dicts             241.7383   100  
        instantiate_object_no_slots   98.1289    41   
        instantiate_tuples            75.1914    31   
        instantiate_named_tuples      61.2109    25   
        instantiate_lists             60.5547    25   
        instantiate_object_slots      56.4648    23   

"""
