import sys
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

_dict = {i: i for i in range(10)}

if sys.version.startswith('2'):
    _iter_dict = _dict.iteritems
else:
    _iter_dict = _dict.items

reps = data.M

def mod_dict(d=_dict, i_d=_iter_dict):
    for _ in repeat(None, reps):
        for k, v in i_d():
            d[k] = v

def make_new(i_d=_iter_dict):
    for _ in repeat(None, reps):
        {k: v for k, v in i_d()}


auto_tester()

"""
Conclusion:
    - Modding the dict is best, maybe more sizes have to be tried

    Python27:
        Name       Secs     %    
        make_new   0.4654   100  
        mod_dict   0.354    76   
        
    Python38:
        Name       Secs     %    
        make_new   0.2973   100  
        mod_dict   0.2478   83   
        
    Python310:
        Name       Secs     %    
        make_new   0.3621   100  
        mod_dict   0.2752   76   
    
    Python312:
        Name       Secs     %    
        make_new   0.2558   100  
        mod_dict   0.2326   91 

"""
