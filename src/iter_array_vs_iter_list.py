from array import array
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester
from src.zz_import import clock

num = data.M10

_list = [clock() for _ in repeat(None, num)]
_array = array('d', _list)

def iter_list():
    for el in _list:
        continue

def iter_array():
    for el in _array:
        continue

auto_tester()

"""
Python27:
    Name         Secs     %    
    iter_array   0.0544   100  
    iter_list    0.0428   79   
    
Python38:
    Name         Secs     %    
    iter_array   0.0608   100  
    iter_list    0.037    61   

Python310:
    Name         Secs     %    
    iter_array   0.0654   100  
    iter_list    0.0394   60  

Python312:
    Name         Secs     %    
    iter_array   0.0692   100  
    iter_list    0.0436   63   
    
Python314:
    Name         Secs     %    
    iter_array   0.0699   100  
    iter_list    0.0346   49   
"""
