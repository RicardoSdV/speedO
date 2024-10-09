""" When you receive key value pairs out of order, but need them sorted, what is the fastest way? """
from bisect import insort
from functools import partial
from heapq import heappush, heappop
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.k100
size = data.hun

ints = data.hun_ints
rev_ints = reversed(ints)
key_value_pairs = list(zip(rev_ints, ints))

def add_to_dict_sort_keys():
    _key_value_pairs = key_value_pairs
    for _ in repeat(None, num):
        _dict = {}
        for k, v in _key_value_pairs:
            _dict[k] = v
        for k in sorted(_dict.keys()):
            v = _dict[k]

def append_tuple_to_list():
    _key_value_pairs = key_value_pairs
    for _ in repeat(None, num):
        _list = []
        append_to_list = _list.append
        for k, v in _key_value_pairs:
            append_to_list((k, v))
        _list.sort()
        for k, v in _list:
            continue

def insort_list():
    _key_value_pairs = key_value_pairs
    for _ in repeat(None, num):
        _list = []
        _insort_list = partial(insort, _list)
        for k, v in _key_value_pairs:
            _insort_list((k, v))

        for k, v in _list:
            continue

def insert_into_heapq():
    _key_value_pairs = key_value_pairs
    for _ in repeat(None, num):
        heap = []
        _heappush = partial(heappush, heap)
        _heappop = partial(heappop, heap)
        for k, v in _key_value_pairs:
            _heappush((k, v))
        while heap:
            k, v = _heappop()

tester(
    (
        add_to_dict_sort_keys,
        append_tuple_to_list,
        insort_list,
        insert_into_heapq,
    )
)

"""
Conclusion:
    - dict and sort keys best choice
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        insert_into_heapq       4.0488   100  
        insort_list             2.05     51   
        append_tuple_to_list    0.5808   14   
        add_to_dict_sort_keys   0.5776   14   

    Python38:
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        insert_into_heapq       1.9532   100  
        insort_list             1.2707   65   
        add_to_dict_sort_keys   0.4117   21   
        append_tuple_to_list    0.3912   20   

    Python310:
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        insert_into_heapq       1.8295   100    
        insort_list             1.2286   67   
        append_tuple_to_list    0.5491   30   
        add_to_dict_sort_keys   0.4827   26   

    Python312:
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        insert_into_heapq       1.8126   100  
        insort_list             1.2339   68   
        append_tuple_to_list    0.5262   28   
        add_to_dict_sort_keys   0.4025   22  
"""
