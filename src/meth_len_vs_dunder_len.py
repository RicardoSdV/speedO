from itertools import repeat

from src.z_data import data
from src.z_tester import tester

_list = [1,2,3,4,5,6,7,8,9,10]
num = data.M10

def dunder_len(outer):
    for inner in outer:
        for el in inner:
            _len = _list.__len__()

def meth_len():
    for _ in repeat(None, num):
        _len = len(_list)

def pre_def_dunder_len():
    len_list = _list.__len__
    for _ in repeat(None, num):
        _len = len_list()


tester(
    (
        dunder_len,
        meth_len,
        pre_def_dunder_len,
    )
)

"""
Conclusion:
    Yes, calling len() is faster, so, no everyone wasn't wrong until now,
    however predefining a local callable assigned to dunder len is actually
    faster if it is going to be used many times 

    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        dunder_len           0.3336   100  
        meth_len             0.1976   59   
        pre_def_dunder_len   0.1754   53   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        dunder_len           0.2614   100  
        meth_len             0.1714   66   
        pre_def_dunder_len   0.131    50   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        dunder_len           0.3425   100  
        meth_len             0.2428   71   
        pre_def_dunder_len   0.1739   51   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        dunder_len           0.2325   100  
        pre_def_dunder_len   0.1655   71   
        meth_len             0.1218   52   
    
"""
