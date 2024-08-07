"""
Probably more pertinent for python27 since dicts are unordered, but
in theory I think you're supposed to act as if they weren't ordered
in python3 too
"""
from itertools import repeat
from operator import itemgetter

from src.z_data import data
from src.z_tester import tester

num = data.M

_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}

def by_keys():
    __dict = _dict
    for _ in repeat(None, num):
        a = __dict['a']
        b = __dict['b']
        c = __dict['c']
        d = __dict['d']
        e = __dict['e']

def get_by_keys():
    __dict = _dict
    for _ in repeat(None, num):
        a = __dict.get('a')
        b = __dict.get('b')
        c = __dict.get('c')
        d = __dict.get('d')
        e = __dict.get('e')

_itemgetter = itemgetter('a', 'b', 'c', 'd', 'e')
def use_itemgetter():
    __dict = _dict
    for _ in repeat(None, num):
        a, b, c, d, e = _itemgetter(__dict)

keys = ('a', 'b', 'c', 'd', 'e')
def gen_with_tuple_of_keys():
    __dict = _dict
    for _ in repeat(None, num):
        a, b, c, d, e = (__dict[key] for key in keys)

def unpack_values():
    """ Only valid for "ordered" dicts """
    __dict = _dict
    for _ in repeat(None, num):
        a, b, c, d, e = __dict.values()

tester(
    (
        by_keys,
        get_by_keys,
        use_itemgetter,
        gen_with_tuple_of_keys,
        unpack_values,
    )
)

"""
Conclusion:
    - Seems like getting the values by keys is the way to go
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        gen_with_tuple_of_keys   0.2568   100  
        get_by_keys              0.1616   63   
        use_itemgetter           0.0658   26   
        by_keys                  0.0586   23   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        gen_with_tuple_of_keys   0.2157   100  
        get_by_keys              0.0762   35   
        use_itemgetter           0.0552   26   
        unpack_values            0.0533   25   
        by_keys                  0.0451   21   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        gen_with_tuple_of_keys   0.2586   100  
        get_by_keys              0.09     35   
        use_itemgetter           0.0623   24   
        unpack_values            0.0563   22   
        by_keys                  0.0557   22   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        gen_with_tuple_of_keys   0.2501   100  
        get_by_keys              0.0622   25   
        use_itemgetter           0.0541   22   
        unpack_values            0.054    22   
        by_keys                  0.0381   15   
"""
