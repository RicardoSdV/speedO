"""
What is faster? to use an intermediate method or a functools partial?
Why the crazy setup? bc I had it already setup for elifs_vs_dict_of_callables.py
"""
from functools import partial
from itertools import repeat
from random import shuffle

from src.z_data import data
from src.z_tester import tester

arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16 = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

def _callable(arg): return
def intermediate_callable1() : _callable(arg1)
def intermediate_callable2() : _callable(arg2)
def intermediate_callable3() : _callable(arg3)
def intermediate_callable4() : _callable(arg4)
def intermediate_callable5() : _callable(arg5)
def intermediate_callable6() : _callable(arg6)
def intermediate_callable7() : _callable(arg7)
def intermediate_callable8() : _callable(arg8)
def intermediate_callable9() : _callable(arg9)
def intermediate_callable10(): _callable(arg10)
def intermediate_callable11(): _callable(arg11)
def intermediate_callable12(): _callable(arg12)
def intermediate_callable13(): _callable(arg13)
def intermediate_callable14(): _callable(arg14)
def intermediate_callable15(): _callable(arg15)
def intermediate_callable16(): _callable(arg16)

_dict_of_intermediate_callables = {
    1:intermediate_callable1,
    2:intermediate_callable2,
    3:intermediate_callable3,
    4:intermediate_callable4,
    5:intermediate_callable5,
    6:intermediate_callable6,
    7:intermediate_callable7,
    8:intermediate_callable8,
    9:intermediate_callable9,
    10:intermediate_callable10,
    11:intermediate_callable11,
    12:intermediate_callable12,
    13:intermediate_callable13,
    14:intermediate_callable14,
    15:intermediate_callable15,
    16:intermediate_callable16,
}

_dict_of_partials = {
    1:partial(_callable, arg1),
    2:partial(_callable, arg2),
    3:partial(_callable, arg3),
    4:partial(_callable, arg4),
    5:partial(_callable, arg5),
    6:partial(_callable, arg6),
    7:partial(_callable, arg7),
    8:partial(_callable, arg8),
    9:partial(_callable, arg9),
    10:partial(_callable, arg10),
    11:partial(_callable, arg11),
    12:partial(_callable, arg12),
    13:partial(_callable, arg13),
    14:partial(_callable, arg14),
    15:partial(_callable, arg15),
    16:partial(_callable, arg16),
}

num = data.M
shuffled_range_16 = list(range(1,17)); shuffle(shuffled_range_16)


def call_intermediates():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            _dict_of_intermediate_callables[key]()

def call_partials():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            _dict_of_partials[key]()

tester(
    (
        call_intermediates,
        call_partials,
    )
)


"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_intermediates   1.0552   100  
        call_partials        0.8088   77   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_intermediates   0.8739   100  
        call_partials        0.5878   67   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_intermediates   0.9908   100  
        call_partials        0.6605   67   

    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_intermediates   0.6762   100  
        call_partials        0.6027   89   
"""


