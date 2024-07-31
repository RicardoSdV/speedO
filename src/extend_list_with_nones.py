"""
Note: there are many more ways of extending a list but they are all dog slow
"""

from itertools import repeat

from src.z_data import data
from src.z_tester import tester

outer_num = data.M
inner_num = data.ten
extend_num = data.hun

outer_list1 = [[None] * inner_num for _ in repeat(None, outer_num)]
outer_list2 = [[None] * inner_num for _ in repeat(None, outer_num)]
outer_list3 = [[None] * inner_num for _ in repeat(None, outer_num)]
outer_list4 = [[None] * inner_num for _ in repeat(None, outer_num)]

def extend_with_times_None():
    num = extend_num
    for inner in outer_list1:
        inner.extend([None] * num)

def concat_with_times_None():
    num = extend_num
    for inner in outer_list2:
        inner += [None] * num

def extend_with_repeat():
    num = extend_num
    for inner in outer_list3:
        inner.extend(repeat(None, num))

def concat_with_repeat():
    num = extend_num
    for inner in outer_list4:
        inner += repeat(None, num)

tester(
    (
        extend_with_times_None,
        concat_with_times_None,
        extend_with_repeat,
        concat_with_repeat,
    )
)

"""
Conclusion:
    - In python27 it seems that either concat or extend with repeat it preferable
    
    - In Python38-310 it seems that extend with repeat is better
    
    - In Python312 it seems that for extending small amounts it is faster extend
    with times None but for larger amounts extend with repeat still better
    
    - Note: It does seem this test does not include the costs of garbage collection
    i.e. is a bunch of small lists are created they are never deleted, only accumulated
    Which means that approaches that use iterators have hidden benefits, that is to say
    probably use extend with repeat always.
    
    Python27:
        outer_num=1 000 000, extend_num=100
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        extend_with_repeat       0.7346   100  
        concat_with_times_None   0.7208   98   
        concat_with_repeat       0.718    98   
        extend_with_times_None   0.7164   98   

        outer_num=100, extend_num=1 000 000
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        extend_with_times_None   0.6294   100  
        concat_with_times_None   0.615    98   
        extend_with_repeat       0.4596   73   
        concat_with_repeat       0.4546   72   
        
    Python38:
        outer_num=1 000 000, extend_num=100
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        extend_with_times_None   0.7415   100  
        concat_with_times_None   0.705    95   
        concat_with_repeat       0.5942   80   
        extend_with_repeat       0.5939   80   

        outer_num=100, extend_num=1 000 000
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        concat_with_times_None   0.6045   100  
        extend_with_times_None   0.5819   96   
        concat_with_repeat       0.4702   78   
        extend_with_repeat       0.4563   75   
        
    Python310:
        outer_num=1 000 000, extend_num=100
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        concat_with_times_None   0.641    100  
        extend_with_times_None   0.6374   99   
        extend_with_repeat       0.5518   86   
        concat_with_repeat       0.5461   85   
        
        outer_num=100, extend_num=1 000 000
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        concat_with_times_None   0.5745   100  
        extend_with_times_None   0.5666   99   
        concat_with_repeat       0.4284   75   
        extend_with_repeat       0.4159   72   

    Python312:
        outer_num=1 000 000, extend_num=100
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        concat_with_repeat       0.5344   100  
        extend_with_repeat       0.5232   98   
        concat_with_times_None   0.4705   88   
        extend_with_times_None   0.4566   85   

        outer_num=100, extend_num=1 000 000
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        concat_with_times_None   0.5387   100  
        extend_with_times_None   0.5282   98   
        extend_with_repeat       0.4249   79   
        concat_with_repeat       0.4207   78   
"""
