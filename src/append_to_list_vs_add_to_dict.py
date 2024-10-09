from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M
size = data.hun
els = data.hun_ints

def append_to_list():
    _size = size
    _els = els
    for _ in repeat(None, num):
        _list = []
        _append_to_list = _list.append
        for el in els:
            _append_to_list(el)

def append_to_lists():
    _size = size
    _els = els
    for _ in repeat(None, num):
        _list = []
        _list2 = []
        _append_to_list = _list.append
        _append_to_list2 = _list2.append
        for el in els:
            _append_to_list(el)
            _append_to_list2(el)

def add_to_dict():
    _size = size
    _els = els
    for _ in repeat(None, num):
        _dict = {}
        for el in els:
            _dict[el] = el

tester(
    (
        append_to_list,
        append_to_lists,
        add_to_dict,
    )
)

"""
Conclusion:
    - For python27 & 38: If you can go without having keys, then appending to one list is faster, if you need keys & values
    a dict is best.
    
    - For python310 & 312: Adding to a dict always faster & way faster respectively
    
    Python27:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        append_to_lists   3.365    100  
        add_to_dict       2.4774   74   
        append_to_list    1.9882   59   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        append_to_lists   2.5428   100  
        add_to_dict       1.9218   76   
        append_to_list    1.5257   60   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        append_to_lists   3.7587   100  
        append_to_list    2.5305   67   
        add_to_dict       2.1929   57   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        append_to_lists   4.3777   100  
        append_to_list    3.3533   77   
        add_to_dict       1.8769   43   
"""
