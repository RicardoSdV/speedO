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

def outer():
    _A, _B, _C, _D, _E, _F = 1, 2, 3, 4, 5, 6
    def inner():
        _a, _b, _c, _d, _e, _f = _A, _B, _C, _D, _E, _F

    return inner

closure = outer()



num = data.k100

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

def call_closure():
    _closure = closure
    for _ in repeat(None, num):
        _closure()


tester(
    (
        call_func_with_ref_to_glob,
        call_func_with_defaults,
        call_func_pass_args,
        call_partial_with_args,
        call_closure,
    ),
    num_repeats = 100,
    print_rounds = False,
)

"""
Conclusion:
    - Python38 is the sweet spot for calling partials with 6 args
    
    - Closure, from tied to slightly faster than partial
    
    Python27:
        - Defaults fastest, globals surprisingly bad, partial & passing args
        not that different to matter.
         
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_closure                 0.0078   100  
        call_partial_with_args       0.0078   100  
        call_func_pass_args          0.0076   97   
        call_func_with_ref_to_glob   0.0075   96   
        call_func_with_defaults      0.0071   91   
        
    Python38:
        - Partial better than passing args, defaults still better, globals
        about as good as partial
        
        Name                         Secs     %    
        call_func_pass_args          0.0058   100  
        call_func_with_ref_to_glob   0.0055   95   
        call_partial_with_args       0.0055   95   
        call_closure                 0.0053   92   
        call_func_with_defaults      0.0053   92   
    
    Python310:
        - Partials & defaults slowest, globals & passing args fastest
    
        Testing times mean of 100 rounds: 
        Name                         Secs     %    
        call_func_pass_args          0.0069   100  
        call_func_with_ref_to_glob   0.0067   97   
        call_func_with_defaults      0.0063   91   
        call_partial_with_args       0.0061   88   
        call_closure                 0.0058   84   
    
    Python312:
        - Globals, defaults & passing args in the same category of fast
        partials slowest 
    
        Testing times mean of 100 rounds: 
        Name                         Secs     %    
        call_partial_with_args       0.0066   100  
        call_closure                 0.006    91   
        call_func_pass_args          0.0056   85   
        call_func_with_defaults      0.0055   84   
        call_func_with_ref_to_glob   0.0051   79   

"""

