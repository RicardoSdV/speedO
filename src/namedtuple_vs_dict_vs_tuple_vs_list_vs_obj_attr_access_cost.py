"""
What are the costs of accessing the elements of different data structures in different ways?
Mainly for use as "entities" i.e. they get instantiated & maybe deleted, one or more times
while the program is running. Therefore, for this type of use, cost of instantiation both in
time & memory should be taken into account, which is tested in the:
namedtuple_vs_dict_vs_tuple_vs_list_vs_obj_instantiation_cost.py test.
"""

from collections import namedtuple
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

NamedTuple = namedtuple('SomeConstants', ('a', 'b', 'c', 'd', 'e', 'f'))
_namedtuple = NamedTuple(1, 2, 3, 4, 5, 6)

_tuple = (1, 2, 3, 4, 5, 6)

_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

_list = [1, 2, 3, 4, 5, 6]


class ClassWithSlots(object):
    __slots__ = ('a', 'b', 'c', 'd', 'e', 'f')
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6

class ClassNoSlots(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6

class OldStyleClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6

obj_with_slots = ClassWithSlots()
obj_with_slots_comma_dec = ClassWithSlots()
obj_no_slots = ClassNoSlots()
obj_old = OldStyleClass()

num = data.M10

def access_namedtuple_by_name(_namedtuple=_namedtuple):
    for _ in repeat(None, num):
        _namedtuple.a
        _namedtuple.b
        _namedtuple.c
        _namedtuple.d
        _namedtuple.e
        _namedtuple.f

def access_namedtuple_by_index(_namedtuple=_namedtuple):
    for _ in repeat(None, num):
        _namedtuple[0]
        _namedtuple[1]
        _namedtuple[2]
        _namedtuple[3]
        _namedtuple[4]
        _namedtuple[5]

def access_namedtuple_by_unpacking(_namedtuple=_namedtuple):
    for _ in repeat(None, num):
        a, b, c, d, e, f = _namedtuple

def access_tuple_by_index(_tuple=_tuple):
    for _ in repeat(None, num):
        _tuple[0]
        _tuple[1]
        _tuple[2]
        _tuple[3]
        _tuple[4]
        _tuple[5]

def access_tuple_by_unpacking(_tuple=_tuple):
    for _ in repeat(None, num):
        a, b, c, d, e, f = _tuple

def access_dict_by_key(_dict = _dict):
    for _ in repeat(None, num):
        _dict['a']
        _dict['b']
        _dict['c']
        _dict['d']
        _dict['e']
        _dict['f']

def access_dict_by_values_unpack(_dict = _dict):
    for _ in repeat(None, num):
        a, b, c, d, e, f = _dict.values()

def access_list_by_index(_list = _list):
    for _ in repeat(None, num):
        _list[0]
        _list[1]
        _list[2]
        _list[3]
        _list[4]
        _list[5]

def access_list_by_unpack(_list = _list):
    for _ in repeat(None, num):
        a, b, c, d, e, f = _list

def access_obj_with_slots_by_attr_name(_obj = obj_with_slots):
    for _ in repeat(None, num):
        _obj.a
        _obj.b
        _obj.c
        _obj.d
        _obj.e
        _obj.f

def access_obj_no_slots_by_attr_name(_obj = obj_no_slots):
    for _ in repeat(None, num):
        _obj.a
        _obj.b
        _obj.c
        _obj.d
        _obj.e
        _obj.f

def access_obj_old_by_attr_name(_obj = obj_old):
    for _ in repeat(None, num):
        _obj.a
        _obj.b
        _obj.c
        _obj.d
        _obj.e
        _obj.f

tester(
    (
        access_obj_with_slots_by_attr_name,
        access_namedtuple_by_name,
        access_namedtuple_by_index,
        access_tuple_by_index,
        access_dict_by_key,
        access_list_by_index,
        access_obj_no_slots_by_attr_name,
        access_obj_old_by_attr_name,
    )
)
tester(
    (
        access_namedtuple_by_unpacking,
        access_tuple_by_unpacking,
        access_dict_by_values_unpack,
        access_list_by_unpack,
    )
)


"""
Conclusion:
    - If one can say something across the board is that to access by attr, obj with __slots__, to access by index, list, 
    to unpack, tuple; there's exceptions. Do look at instantiation costs.
    
    - If theres something to really not do is access namedtuple by attr in python27, & to unpack the values of a dict.
    
    - Unexpected is how good object with __slots__ is. Specially if memory instantiation costs is taken into account. 

    Python27:
        - Accessing by index, list fastest.
        - Accessing by attr name pretty much all similar although surprisingly old style class fastest
        - Named tuple is slow for access by attr (probably because implemented with properties)
        - For unpacking tuple & list fastest. access_dict_by_values_unpack does not make sense in python27 
        since dict unordered
        
        Name                                 Secs     %    
        access_namedtuple_by_name            2.4766   100  
        access_namedtuple_by_index           0.7816   32   
        access_obj_no_slots_by_attr_name     0.779    31   
        access_tuple_by_index                0.7702   31   
        access_obj_with_slots_by_attr_name   0.7442   30   
        access_obj_old_by_attr_name          0.7062   28   
        access_dict_by_key                   0.692    28   
        access_list_by_index                 0.5676   23   
        
        Name                             Secs     %    
        access_dict_by_values_unpack     0.8054   100  
        access_namedtuple_by_unpacking   0.3032   38   
        access_list_by_unpack            0.1558   19   
        access_tuple_by_unpacking        0.1516   19   
    
    Python38:
        - Accessing by index, list fastest tuple & namedtuple closing the gap
        - Accessing by attr, object with slots fastest
        - Unpacking, tuple fastest, list closing the gap

        Name                                 Secs     %    
        access_dict_by_key                   0.5115   100  
        access_obj_no_slots_by_attr_name     0.5092   99   
        access_namedtuple_by_name            0.4708   92   
        access_obj_with_slots_by_attr_name   0.4509   88   
        access_namedtuple_by_index           0.4321   84   
        access_tuple_by_index                0.4309   84   
        access_list_by_index                 0.3856   75   
        
        Name                             Secs     %    
        access_dict_by_values_unpack     0.5242   100  
        access_namedtuple_by_unpacking   0.3173   61   
        access_list_by_unpack            0.1508   28   
        access_tuple_by_unpacking        0.1398   27   

    Python310:
        - By index tuple fastest, namedtuple close
        - By attr, namedtuple fastest, obj with __slots__ close
        - Unpacking tuple fastest 
        
        Name                                 Secs     %    
        access_dict_by_key                   0.6375   100  
        access_obj_no_slots_by_attr_name     0.5967   94   
        access_list_by_index                 0.5855   92   
        access_obj_with_slots_by_attr_name   0.5842   92   
        access_namedtuple_by_index           0.5702   89   
        access_tuple_by_index                0.5635   88   
        access_namedtuple_by_name            0.5624   88   
        
        Name                             Secs     %    
        access_dict_by_values_unpack     0.876    100  
        access_namedtuple_by_unpacking   0.4703   54   
        access_list_by_unpack            0.257    28   
        access_tuple_by_unpacking        0.2554   28   

        
    Python312:
        - By index list fastest
        - By attr obj with __slots__
        - Unpacking tuple
        
        Name                                 Secs     %    
        access_namedtuple_by_index           0.5075   100  
        access_namedtuple_by_name            0.4873   96   
        access_dict_by_key                   0.3952   78   
        access_list_by_index                 0.3604   71   
        access_tuple_by_index                0.3224   64   
        access_obj_with_slots_by_attr_name   0.3031   60   
        access_obj_no_slots_by_attr_name     0.2703   53   
        
        Name                             Secs     %    
        access_dict_by_values_unpack     0.4908   100  
        access_namedtuple_by_unpacking   0.3087   63   
        access_list_by_unpack            0.1661   34   
        access_tuple_by_unpacking        0.159    32   
"""
