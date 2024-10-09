from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M
size = data.hun
zipped_kv_pairs = list(zip(range(size), range(size)))

def len_of_dict():
    _size = size
    _zipped_kv_pairs = zipped_kv_pairs
    for _ in repeat(None, num):
        _dict = {}
        for k, v in _zipped_kv_pairs:
            _dict[k] = v
        _len = len(_dict)

def count_on_add():
    _size = size
    _zipped_kv_pairs = zipped_kv_pairs
    for _ in repeat(None, num):
        _cnt = 0
        _dict = {}
        for k, v in _zipped_kv_pairs:
            _dict[k] = v
            _cnt += 1

tester(
    (
        len_of_dict,
        count_on_add,
    )
)

"""
Conclusion:
    - This test has quite a bit of overhead, so len() even better
    Python27:
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        count_on_add   3.7306   100  
        len_of_dict    2.923    78   

    Python38:
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        count_on_add   2.9889   100  
        len_of_dict    2.2559   75   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        count_on_add   3.5235   100  
        len_of_dict    2.7769   79   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        count_on_add   2.8275   100  
        len_of_dict    2.2289   79   
"""

