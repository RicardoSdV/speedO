from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester
_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
}


num = data.M10

def call_copy(_copy = _dict.copy):
    __dict = _copy()
    for _ in repeat(None, num):
        __dict = _copy()

def set_defaults():
    __dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
    }
    for _ in repeat(None, num):
        for k in __dict:
            __dict[k] = 1


auto_tester()


"""
Conclusion:
Predef copy faster.

Python27:
    Name           Secs     %    
    set_defaults   1.4014   100  
    call_copy      0.9842   70   
    
Python38:
    Name           Secs     %    
    set_defaults   1.0058   100  
    call_copy      0.343    34   
    
Python310:
    Name           Secs     %    
    set_defaults   1.1544   100  
    call_copy      0.3578   31   
    
Python312:
    Name           Secs     %    
    set_defaults   1.0574   100  
    call_copy      0.3584   34  
"""

