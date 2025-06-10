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



def _new():
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
    }


num = data.M10

def call_copy(_copy = _dict.copy):
    for _ in repeat(None, num):
        _copy()

def call_new(__new=_new):
    for _ in repeat(None, num):
        __new()


auto_tester()


"""
Conclusion:
Predef copy 2-3x faster.

Python27:
    Name        Secs     %    
    call_new    1.8938   100  
    call_copy   0.9964   53  
    
Python38:
    Name        Secs     %    
    call_new    0.9002   100  
    call_copy   0.3147   35  
    
Python310:
    Name        Secs     %    
    call_new    0.9888   100  
    call_copy   0.3344   34   
    
Python312:
    Name        Secs     %    
    call_new    0.8894   100  
    call_copy   0.3523   40   
"""

