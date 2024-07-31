from collections import namedtuple
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

NamedTuple = namedtuple('SomeConstants', ('c1', 'c2', 'c3', 'c4'))
_namedtuple = NamedTuple(c1=1, c2=2, c3=3, c4=4)

_dict = {'c1': 1, 'c2': 2, 'c3': 3, 'c4': 4}

_tuple = (1, 2, 3, 4)

# just names
c1, c2, c3, c4 = 1, 2, 3, 4

class Class:
    c1, c2, c3, c4 = 1, 2, 3, 4

class ClassForInstantiating:
    __slots__ = ('c1', 'c2', 'c3', 'c4')
    def __init__(self):
        self.c1 = 1
        self.c2 = 2
        self.c3 = 3
        self.c4 = 4

obj = ClassForInstantiating()

num = data.M10

def access_named_tuple():
    for _ in repeat(None, num):
        _c1 = _namedtuple.c1
        _c2 = _namedtuple.c2
        _c3 = _namedtuple.c3
        _c4 = _namedtuple.c4
def access_local_named_tuple():
    __namedtuple = _namedtuple
    for _ in repeat(None, num):
        _c1 = __namedtuple.c1
        _c2 = __namedtuple.c2
        _c3 = __namedtuple.c3
        _c4 = __namedtuple.c4
def make_local_and_access_named_tuple():
    for _ in repeat(None, num):
        __namedtuple = _namedtuple
        _c1 = __namedtuple.c1
        _c2 = __namedtuple.c2
        _c3 = __namedtuple.c3
        _c4 = __namedtuple.c4
def access_dict():
    for _ in repeat(None, num):
        _c1 = _dict['c1']
        _c2 = _dict['c2']
        _c3 = _dict['c3']
        _c4 = _dict['c4']
def access_local_dict():
    __dict = _dict
    for _ in repeat(None, num):
        _c1 = __dict['c1']
        _c2 = __dict['c2']
        _c3 = __dict['c3']
        _c4 = __dict['c4']
def make_local_access_dict():
    for _ in repeat(None, num):
        __dict = _dict
        _c1 = __dict['c1']
        _c2 = __dict['c2']
        _c3 = __dict['c3']
        _c4 = __dict['c4']
def access_tuple():
    for _ in repeat(None, num):
        _c1 = _tuple[0]
        _c2 = _tuple[1]
        _c3 = _tuple[2]
        _c4 = _tuple[3]
def access_local_tuple():
    __tuple = _tuple
    for _ in repeat(None, num):
        _c1 = __tuple[0]
        _c2 = __tuple[1]
        _c3 = __tuple[2]
        _c4 = __tuple[3]
def make_local_and_access_tuple():
    for _ in repeat(None, num):
        __tuple = _tuple
        _c1 = __tuple[0]
        _c2 = __tuple[1]
        _c3 = __tuple[2]
        _c4 = __tuple[3]
def access_class_attrs():
    for _ in repeat(None, num):
        _c1 = Class.c1
        _c2 = Class.c2
        _c3 = Class.c3
        _c4 = Class.c4
def access_local_class_attrs():
    _Class = Class
    for _ in repeat(None, num):
        _c1 = _Class.c1
        _c2 = _Class.c2
        _c3 = _Class.c3
        _c4 = _Class.c4
def make_local_and_access_class_attrs():
    for _ in repeat(None, num):
        _Class = Class
        _c1 = _Class.c1
        _c2 = _Class.c2
        _c3 = _Class.c3
        _c4 = _Class.c4
def access_instance_attrs():
    for _ in repeat(None, num):
        _c1 = obj.c1
        _c2 = obj.c2
        _c3 = obj.c3
        _c4 = obj.c4
def access_local_instance_attrs():
    _obj = obj
    for _ in repeat(None, num):
        _c1 = _obj.c1
        _c2 = _obj.c2
        _c3 = _obj.c3
        _c4 = _obj.c4
def make_local_and_access_instance_attrs():
    for _ in repeat(None, num):
        _obj = obj
        _c1 = _obj.c1
        _c2 = _obj.c2
        _c3 = _obj.c3
        _c4 = _obj.c4
def access_names():
    for _ in repeat(None, num):
        _c1 = c1
        _c2 = c2
        _c3 = c3
        _c4 = c4
def access_local_names():
    _c1 = c1
    _c2 = c2
    _c3 = c3
    _c4 = c4
    for _ in repeat(None, num):
        __c1 = _c1
        __c2 = _c2
        __c3 = _c3
        __c4 = _c4

tester(
    (
        access_named_tuple,
        access_dict,
        access_tuple,
        access_class_attrs,
        access_instance_attrs,
        access_names,
    ),
    print_rounds=False
)

tester(
    (
        access_local_named_tuple,
        access_local_dict,
        access_local_tuple,
        access_local_class_attrs,
        access_local_instance_attrs,
        access_local_names,
    ),
    print_rounds=False
)

tester(
    (
        make_local_and_access_named_tuple,
        make_local_access_dict,
        make_local_and_access_tuple,
        make_local_and_access_class_attrs,
        make_local_and_access_instance_attrs,
        access_names,
    ),
    print_rounds=False
)

"""
Conclusion:
    - Basically names almost always fastest, I suppose that at some point making 
    one class local and getting stuff from there is more efficient than importing
    like 1000 names one by one and making them all local to be used in some loop.
    
    - Otherwise named tuple almost never worth it, specially in Python27
    
    - Also dicts underwhelming, kinda strange since classes work with dicts no?
    
    - In Python312 specifically instance attrs better optimized
    
    Python27:
        - Named tuples super slow, use class attrs
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        access_named_tuple      1.6542   100  
        access_tuple            0.5634   34   
        access_dict             0.5358   32   
        access_instance_attrs   0.5006   30   
        access_class_attrs      0.4834   28   
        access_names            0.2166   13   
        
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        access_local_named_tuple      1.594    100  
        access_local_tuple            0.4902   31   
        access_local_dict             0.4498   28   
        access_local_instance_attrs   0.432    27   
        access_local_class_attrs      0.401    25   
        access_local_names            0.1332   8    
        
        Testing times mean of 5 rounds: 
        Name                                   Secs     %    
        make_local_and_access_named_tuple      1.6362   100  
        make_local_and_access_tuple            0.5456   33   
        make_local_access_dict                 0.4966   30   
        make_local_and_access_instance_attrs   0.4866   30   
        make_local_and_access_class_attrs      0.4626   28   
        access_names                           0.2132   13   
    
    Python38:
        - Dict slowest, use class attr
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        access_instance_attrs   0.4195   100  
        access_dict             0.4141   99   
        access_named_tuple      0.3978   95   
        access_tuple            0.3687   88   
        access_class_attrs      0.348    83   
        access_names            0.1952   47   
        
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        access_local_dict             0.3469   100  
        access_local_named_tuple      0.3371   97   
        access_local_instance_attrs   0.3053   88   
        access_local_tuple            0.3005   87   
        access_local_class_attrs      0.2844   82   
        access_local_names            0.1163   34   
        
        Testing times mean of 5 rounds: 
        Name                                   Secs     %    
        make_local_access_dict                 0.3836   100  
        make_local_and_access_named_tuple      0.3703   97   
        make_local_and_access_instance_attrs   0.3601   94   
        make_local_and_access_tuple            0.3436   90   
        make_local_and_access_class_attrs      0.3238   84   
        access_names                           0.1958   51   

    Python310:
        - Pretty much all tied except dict slow
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        access_dict             0.5917   100  
        access_tuple            0.5247   89   
        access_class_attrs      0.523    88   
        access_named_tuple      0.5119   87   
        access_instance_attrs   0.5098   86   
        access_names            0.3061   52   
        
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        access_local_dict             0.4265   100  
        access_local_instance_attrs   0.3703   87   
        access_local_tuple            0.3617   85   
        access_local_class_attrs      0.3607   85   
        access_local_named_tuple      0.3603   84   
        access_local_names            0.133    31   
        
        Testing times mean of 5 rounds: 
        Name                                   Secs     %    
        make_local_access_dict                 0.4976   100  
        make_local_and_access_instance_attrs   0.4326   87   
        make_local_and_access_tuple            0.4295   86   
        make_local_and_access_class_attrs      0.427    86   
        make_local_and_access_named_tuple      0.4247   85   
        access_names                           0.3095   62   
        
    Python312:
        - Instance attr fastest, otherwise cls attrs pretty tied
    
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        access_named_tuple      0.3731   100  
        access_dict             0.3443   92   
        access_tuple            0.2964   79   
        access_instance_attrs   0.2742   73   
        access_class_attrs      0.2606   70   
        access_names            0.1618   43   
        
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        access_local_named_tuple      0.3168   100  
        access_local_dict             0.289    91   
        access_local_tuple            0.2776   88   
        access_local_class_attrs      0.1913   60   
        access_local_instance_attrs   0.1814   56   
        access_local_names            0.0997   31   
        
        Testing times mean of 5 rounds: 
        Name                                   Secs     %    
        make_local_and_access_named_tuple      0.361    100  
        make_local_access_dict                 0.3178   88   
        make_local_and_access_tuple            0.273    76   
        make_local_and_access_class_attrs      0.2476   69   
        make_local_and_access_instance_attrs   0.2435   67   
        access_names                           0.1622   45   
"""

