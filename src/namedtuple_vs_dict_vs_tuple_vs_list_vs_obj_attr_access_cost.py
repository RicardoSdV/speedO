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

class ClassWithSlotsCommaDec(object):
    __slots__ = ('a', 'b', 'c', 'd', 'e', 'f')
    def __init__(self):
        self.a, self.b, self.c, self.d, self.e, self.f = 1, 2, 3, 4, 5, 6

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

def access_namedtuple_by_name():
    __namedtuple = _namedtuple
    for _ in repeat(None, num):
        a = __namedtuple.a
        b = __namedtuple.b
        c = __namedtuple.c
        d = __namedtuple.d
        e = __namedtuple.e
        f = __namedtuple.f

def access_namedtuple_by_index():
    __namedtuple = _namedtuple
    for _ in repeat(None, num):
        a = __namedtuple[0]
        b = __namedtuple[1]
        c = __namedtuple[2]
        d = __namedtuple[3]
        e = __namedtuple[4]
        f = __namedtuple[5]

def access_namedtuple_by_unpacking():
    __namedtuple = _namedtuple
    for _ in repeat(None, num):
        a, b, c, d, e, f = __namedtuple

def access_tuple_by_index():
    __tuple = _tuple
    for _ in repeat(None, num):
        a = __tuple[0]
        b = __tuple[1]
        c = __tuple[2]
        d = __tuple[3]
        e = __tuple[4]
        f = __tuple[5]

def access_tuple_by_unpacking():
    __tuple = _tuple
    for _ in repeat(None, num):
        a, b, c, d, e, f = __tuple

def access_dict_by_key():
    __dict = _dict
    for _ in repeat(None, num):
        a = __dict['a']
        b = __dict['b']
        c = __dict['c']
        d = __dict['d']
        e = __dict['e']
        f = __dict['f']

def access_dict_by_values_unpack():
    __dict = _dict
    for _ in repeat(None, num):
        a, b, c, d, e, f = __dict.values()

def access_list_by_index():
    __list = _list
    for _ in repeat(None, num):
        a = __list[0]
        b = __list[1]
        c = __list[2]
        d = __list[3]
        e = __list[4]
        f = __list[5]

def access_list_by_unpack():
    __list = _list
    for _ in repeat(None, num):
        a, b, c, d, e, f = __list

def access_obj_with_slots_by_attr_name():
    _obj = obj_with_slots
    for _ in repeat(None, num):
        a = _obj.a
        b = _obj.b
        c = _obj.c
        d = _obj.d
        e = _obj.e
        f = _obj.f

def access_obj_no_slots_by_attr_name():
    _obj = obj_no_slots
    for _ in repeat(None, num):
        a = _obj.a
        b = _obj.b
        c = _obj.c
        d = _obj.d
        e = _obj.e
        f = _obj.f

def access_obj_old_by_attr_name():
    _obj = obj_old
    for _ in repeat(None, num):
        a = _obj.a
        b = _obj.b
        c = _obj.c
        d = _obj.d
        e = _obj.e
        f = _obj.f

tester(
    (
        access_obj_with_slots_by_attr_name,
        access_namedtuple_by_name,
        access_namedtuple_by_index,
        access_tuple_by_index,
        access_dict_by_key,
        access_list_by_index,
        access_obj_no_slots_by_attr_name,
        # access_obj_old_by_attr_name,
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
        
        Testing times mean of 5 rounds: 
        Name                                 Secs     %    
        access_namedtuple_by_name            2.3524   100  
        access_namedtuple_by_index           0.7092   30   
        access_tuple_by_index                0.7054   30   
        access_obj_no_slots_by_attr_name     0.6756   28   
        access_obj_with_slots_by_attr_name   0.6736   28   
        access_dict_by_key                   0.6462   27   
        access_obj_old_by_attr_name          0.6208   26   
        access_list_by_index                 0.5168   22    
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        access_dict_by_values_unpack     0.8128   100  
        access_namedtuple_by_unpacking   0.2928   36   
        access_list_by_unpack            0.1558   19   
        access_tuple_by_unpacking        0.148    18   
    
    Python38:
        - Accessing by index, list fastest tuple & namedtuple closing the gap
        - Accessing by attr, object with slots fastest
        - Unpacking, tuple fastest, list closing the gap

        Testing times mean of 5 rounds: 
        Name                                 Secs     %    
        access_dict_by_key                   0.5206   100  
        access_obj_no_slots_by_attr_name     0.5018   96   
        access_namedtuple_by_name            0.4912   94   
        access_obj_with_slots_by_attr_name   0.4424   85   
        access_namedtuple_by_index           0.4342   83   
        access_tuple_by_index                0.4317   83   
        access_list_by_index                 0.3874   74   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        access_dict_by_values_unpack     0.5198   100  
        access_namedtuple_by_unpacking   0.31     60   
        access_list_by_unpack            0.1505   28   
        access_tuple_by_unpacking        0.1376   26   

    Python310:
        - By index tuple fastest, namedtuple close
        - By attr, namedtuple fastest, obj with __slots__ close
        - Unpacking tuple fastest 
        
        Testing times mean of 5 rounds: 
        Name                                 Secs     %    
        access_dict_by_key                   0.6      100  
        access_obj_no_slots_by_attr_name     0.5792   97   
        access_list_by_index                 0.5464   91   
        access_obj_with_slots_by_attr_name   0.5419   90   
        access_namedtuple_by_name            0.5323   89   
        access_namedtuple_by_index           0.5254   88   
        access_tuple_by_index                0.524    87   
        
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        access_dict_by_values_unpack     0.5302   100  
        access_namedtuple_by_unpacking   0.3483   66   
        access_list_by_unpack            0.1875   35   
        access_tuple_by_unpacking        0.1718   32   
        
    Python312:
        - By index list fastest
        - By attr obj with __slots__
        - Unpacking tuple
        
        Testing times mean of 5 rounds: 
        Name                                 Secs     %    
        access_namedtuple_by_index           0.5507   100  
        access_namedtuple_by_name            0.4616   84   
        access_dict_by_key                   0.3921   71   
        access_tuple_by_index                0.3696   67   
        access_list_by_index                 0.338    61   
        access_obj_no_slots_by_attr_name     0.2779   50   
        access_obj_with_slots_by_attr_name   0.2626   48   
             
        Testing times mean of 5 rounds: 
        Name                             Secs     %    
        access_dict_by_values_unpack     0.4863   100  
        access_namedtuple_by_unpacking   0.3079   63   
        access_list_by_unpack            0.1609   33   
        access_tuple_by_unpacking        0.1529   31   
"""
