from itertools import repeat

from src.z_data import data
from src.z_tester import tester

outer_num = data.k100
inner_num = data.hun

def repeat_None():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = [None for _ in repeat(None, num)]

def repeat_none():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = [none for none in repeat(None, num)]

def times_none():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = [None] * num

def repeat_gen():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = list(repeat(None, num))

def range_None():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = [None for _ in range(num)]

def predef_append_None():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = []
        append_to_list = _list.append
        for _ in repeat(None, num):
            append_to_list(None)

def predef_append_none():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = []
        append_to_list = _list.append
        for none in repeat(None, num):
            append_to_list(none)

def append_None():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = []
        for _ in repeat(None, num):
            _list.append(None)

def append_none():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = []
        for none in repeat(None, num):
            _list.append(none)

def gen_repeat_None():
    num = inner_num
    for _ in repeat(None, outer_num):
        _list = list(None for _ in repeat(None, num))

tester(
    (
        repeat_None,
        repeat_none,
        times_none,
        repeat_gen,
        range_None,
        predef_append_None,
        predef_append_none,
        append_None,
        append_none,
        gen_repeat_None,
    )
)

"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        append_none          0.3218   100  
        append_None          0.3132   97   
        gen_repeat_None      0.2492   77   
        predef_append_None   0.22     68   
        predef_append_none   0.2164   67   
        range_None           0.1686   52   
        repeat_none          0.1404   44   
        repeat_None          0.1378   43   
        repeat_gen           0.0496   15   
        times_none           0.0252   8    
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        append_none          0.2091   100  
        append_None          0.2075   99   
        gen_repeat_None      0.1977   95   
        predef_append_None   0.1627   78   
        predef_append_none   0.1606   77   
        range_None           0.0976   47   
        repeat_none          0.0939   45   
        repeat_None          0.0936   45   
        repeat_gen           0.0321   15   
        times_none           0.0239   11   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        append_None          0.2989   100  
        append_none          0.2983   100  
        gen_repeat_None      0.2945   99   
        predef_append_None   0.2601   87   
        predef_append_none   0.2595   87   
        range_None           0.2003   67   
        repeat_none          0.1949   65   
        repeat_None          0.1921   64   
        repeat_gen           0.0314   10   
        times_none           0.0183   6    
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        predef_append_none   0.2514   100  
        predef_append_None   0.2499   99   
        gen_repeat_None      0.2441   97   
        append_None          0.2223   88   
        append_none          0.2174   86   
        range_None           0.1085   43   
        repeat_None          0.1012   40   
        repeat_none          0.0913   36   
        repeat_gen           0.0294   12   
        times_none           0.0114   5    
"""
