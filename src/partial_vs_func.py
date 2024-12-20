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

num = data.M10

def call_func_with_ref_to_glob():
    _glob_ref_func = glob_ref_func
    for _ in repeat(None, num):
        _glob_ref_func()

def call_func_with_defaults():
    _defaults_func = defaults_func
    for _ in repeat(None, num):
        _defaults_func()

def call_func_pass_args():
    _args_func = args_func
    for _ in repeat(None, num):
        _args_func(1, 2, 3, 4, 5, 6)

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
    print_rounds = False,
)

"""
Conclusion:
    - Defaults is fastest until 312 otherwise just pass args
    
    Python27:
        Name                         Secs     %    
        call_closure                 0.8034   100  
        call_partial_with_args       0.7958   99   
        call_func_with_ref_to_glob   0.7684   96   
        call_func_pass_args          0.7464   93   
        call_func_with_defaults      0.7008   87   
        
    Python38:
        Name                         Secs     %    
        call_func_pass_args          0.5739   100  
        call_partial_with_args       0.5628   98   
        call_func_with_ref_to_glob   0.5483   96   
        call_closure                 0.5473   95   
        call_func_with_defaults      0.4916   86   
    
    Python310:
        Name                         Secs     %    
        call_func_with_ref_to_glob   0.693    100  
        call_func_pass_args          0.6696   97   
        call_partial_with_args       0.6323   91   
        call_closure                 0.5987   86   
        call_func_with_defaults      0.5973   86   
    
    Python312:
        Name                         Secs     %    
        call_partial_with_args       0.6566   100  
        call_closure                 0.6115   93   
        call_func_pass_args          0.5664   86   
        call_func_with_defaults      0.5595   85   
        call_func_with_ref_to_glob   0.5252   80   

"""

