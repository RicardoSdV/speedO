""" So if you have to pass a tuple or a list to a callable only
to then unpack it is it better to pass it as *tuple? """
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10
_tuple = (1, 2, 3, 4, 5)

def _pass_and_unpack(__tuple):
    a, b, c, d, e = __tuple

def _pass_as_star(a, b, c, d, e):
    return


def call_pass_and_unpack(__tuple=_tuple):
    for _ in repeat(None, num):
        _pass_and_unpack(__tuple)

def call_pass_as_star(__tuple=_tuple):
    for _ in repeat(None, num):
        _pass_as_star(*__tuple)


auto_tester()

"""
Conclusion:
- Star is always slower, but not so bad in python312

Python27:
Name                   Secs     %    
call_pass_as_star      0.5466   100  
call_pass_and_unpack   0.4676   86  

Python38:
Name                   Secs     %    
call_pass_and_unpack   0.3709   100  
call_pass_as_star      0.3146   85   

Python310:
Name                   Secs     %    
call_pass_and_unpack   0.4423   100  
call_pass_as_star      0.3532   80   

Python312:
Name                   Secs     %    
call_pass_and_unpack   0.3199   100  
call_pass_as_star      0.2938   92   

"""

