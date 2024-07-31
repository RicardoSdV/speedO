""" Real world example, technically they are different since the get_func, provides with defaults,
whereas the update one does not, but for the intended application it shouldn't matter """


from itertools import repeat

from src.z_data import data
from src.z_tester import tester


def update_func(**kwargs):
    d = {'a': 1}
    d.update(kwargs)

def get_func(**kwargs):
    d = {
        'a': 1,
        'b': kwargs.get('b', 0),
        'c': kwargs.get('c', 0),
    }

def if_func(**kwargs):
    d = {
        'a': 1,
    }
    if 'a' in kwargs:
        d['a'] = kwargs['a']
    if 'b' in kwargs:
        d['b'] = kwargs['b']

def for_func(**kwargs):
    d = {
        'a': 1,
    }
    keys = ('b', 'c')
    for key in keys:
        if key in kwargs:
            d[key] = kwargs[key]


num = data.M10

def call_update_func_no_args():
    for _ in repeat(None, num):
        update_func()

def call_update_func_with_args():
    for _ in repeat(None, num):
        update_func(b=1, c=2)

def call_get_func_no_args():
    for _ in repeat(None, num):
        get_func()

def call_get_func_with_args():
    for _ in repeat(None, num):
        get_func(b=1, c=2)

def call_if_func_no_args():
    for _ in repeat(None, num):
        if_func()

def call_if_func_with_args():
    for _ in repeat(None, num):
        if_func(b=1, c=2)

def call_for_func_no_args():
    for _ in repeat(None, num):
        for_func()

def call_for_func_with_args():
    for _ in repeat(None, num):
        for_func(b=1, c=2)


tester(
    (
        call_update_func_no_args,
        call_update_func_with_args,
        call_get_func_no_args,
        call_get_func_with_args,
        call_if_func_no_args,
        call_if_func_with_args,
        call_for_func_no_args,
        call_for_func_with_args,
    )
)

tester(
    (
        call_update_func_no_args,
        call_update_func_with_args,
        call_get_func_no_args,
        call_get_func_with_args,
        call_if_func_no_args,
        call_if_func_with_args,
        call_for_func_no_args,
        call_for_func_with_args,
    )
)


"""
Conclusion:
    - Good old ifs
    Python27:
        
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_for_func_with_args      1.972    100  
        call_get_func_with_args      1.8364   93   
        call_update_func_with_args   1.7284   88   
        call_get_func_no_args        1.5474   78   
        call_if_func_with_args       1.3868   70   
        call_update_func_no_args     1.2732   65   
        call_for_func_no_args        1.175    60   
        call_if_func_no_args         0.8062   41  
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                         Secs     %    
        call_for_func_with_args      1.6011   100  
        call_get_func_with_args      1.2092   76   
        call_update_func_with_args   1.1645   73   
        call_if_func_with_args       1.148    72   
        call_get_func_no_args        1.0165   63   
        call_for_func_no_args        0.945    59   
        call_update_func_no_args     0.7493   47   
        call_if_func_no_args         0.7041   44   
"""
