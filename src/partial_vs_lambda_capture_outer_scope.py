""" When you need to make and call something
like a partial once what is faster? """

from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10

def _func(arg):
    return

def make_partial_and_call(func=_func):
    for _ in repeat(None, num):
        c = partial(func, 1)
        c()

def make_partial_only(func=_func):
    for _ in repeat(None, num):
        partial(func, 1)


def make_lambda_and_call(func=_func):
    for _ in repeat(None, num):
        c = lambda: func(1)
        c()

def make_lambda_only(func=_func):
    for _ in repeat(None, num):
        lambda: func(1)


auto_tester(segregator='end')


"""
Conclusion:
In general calling partials is faster but making functions is faster, 
so, when making one for calling once its better to use functions,
by the way lambdas and functions are equally fast to make and call.
Except in python310 for some reason.

Python27:
    Name                    Secs     %    
    make_partial_and_call   1.0186   100  
    make_lambda_and_call    0.8808   86   
    
    Name                Secs     %    
    make_partial_only   0.5898   100  
    make_lambda_only    0.3118   53   

Python38:
    Name                    Secs     %    
    make_partial_and_call   0.7333   100  
    make_lambda_and_call    0.7062   96   
    
    Name                Secs     %    
    make_partial_only   0.4338   100  
    make_lambda_only    0.2787   64   

Python310:
    Name                    Secs     %    
    make_lambda_and_call    0.8812   100  
    make_partial_and_call   0.7693   87   
    
    Name                Secs     %    
    make_partial_only   0.464    100  
    make_lambda_only    0.4146   89   

Python312:
    Name                    Secs     %    
    make_partial_and_call   0.8517   100  
    make_lambda_and_call    0.6768   79   
    
    Name                Secs     %    
    make_partial_only   0.5339   100  
    make_lambda_only    0.3823   72   

"""




