from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

_str = 'something.py'
suffix = '.py'
suffixLen = len(suffix)
num = data.M10

def endswith(_str=_str, suffix=suffix):
    for _ in repeat(None, num):
        _str.endswith(suffix)

def slice_and_comp(_str=_str, suffix=suffix, suffixLen=suffixLen):
    for _ in repeat(None, num):
        _str[-suffixLen:] == suffix


auto_tester()


"""
Conclusion:
So, this test kind of bad, but definitely slice in 27, and maybe in 312.

Python27:
    Name             Secs     %    
    endswith         0.618    100  
    slice_and_comp   0.3832   62  

Python38:
    Name             Secs     %    
    slice_and_comp   0.431    100  
    endswith         0.3844   89   
   
Python310:
    Name             Secs     %    
    slice_and_comp   0.4434   100  
    endswith         0.4166   94   

Python312:
    Name             Secs     %    
    endswith         0.3838   100  
    slice_and_comp   0.3623   94  
"""
