""" What is the cost of using a partial vs other ways of getting names local? """
from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


A, B, C, D, E, F = 1, 2, 3, 4, 5, 6

def no_args_func():
    return

def args_func(a, b, c, d, e, f):
    _a, _b, _c, _d, _e, _f = a, b, c, d, e, f

def defaults_func(a=1, b=2, c=3, d=4, e=5, f=6):
    _a, _b, _c, _d, _e, _f = a, b, c, d, e, f

def glob_ref_func():
    _a, _b, _c, _d, _e, _f = A, B, C, D, E, F

_partial = partial(args_func, 1,2,3,4,5,6)


num = data.M10

def call_func_with_ref_to_glob():
    _glob_ref_func = glob_ref_func
    for _ in repeat(None, num):
        _glob_ref_func()

def call_func_with_defaults():
    _defaults_func = defaults_func
    for _ in repeat(None, num):
        defaults_func()

def call_func_pass_args():
    _args_func = args_func
    for _ in repeat(None, num):
        args_func(1, 2, 3, 4, 5, 6)

def call_partial_with_args():
    __partial = _partial
    for _ in repeat(None, num):
        __partial()


tester(
    (
        call_func_with_ref_to_glob,
        call_func_with_defaults,
        call_func_pass_args,
        call_partial_with_args,
    )
)

"""
Conclusion:
    - Python38 is the sweet spot for calling partials with 6 args
    
    Python27:
        - Defaults fastest, globals surprisingly bad, partial & passing args
        not that different to matter.
         
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_func_with_ref_to_glob   0.7782   100  
        call_partial_with_args       0.7742   99   
        call_func_pass_args          0.7542   97   
        call_func_with_defaults      0.703    90   
        
    Python38:
        - Partial better than passing args, defaults still better, globals
        about as good as partial
        
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_func_pass_args          0.5839   100  
        call_func_with_ref_to_glob   0.5577   96   
        call_partial_with_args       0.5574   95   
        call_func_with_defaults      0.5284   90   
    
    Python310:
        - Partials & defaults slowest, globals & passing args fastest
    
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_func_with_ref_to_glob   0.6953   100  
        call_func_pass_args          0.6912   99   
        call_func_with_defaults      0.6305   91   
        call_partial_with_args       0.6206   89   
    
    Python312:
        - Globals, defaults & passing args in the same category of fast
        partials slowest 
    
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_partial_with_args       0.637    100  
        call_func_pass_args          0.5412   85   
        call_func_with_defaults      0.5279   83   
        call_func_with_ref_to_glob   0.5079   80   

"""

