"""
How much faster is repeat than range() when looping and no index required?
"""
from itertools import repeat

from src.z_tester import tester
from z_data import data

M100 = data.M100
M100_range = data.M100_range


def itertools_repeat():
    for _ in repeat(None, M100):
        continue


def for_in_range():
    for _ in range(M100):
        continue


def for_in_pre_calc_range():
    for _ in M100_range:
        continue


tester(
    (
        itertools_repeat,
        for_in_range,
        for_in_pre_calc_range,
    )
)

"""
Conclusion:
    Use repeat were you can, if not use normal range unless python27 and memory not an issue, then use precalc range

    - Python312:
        Name                    Time     %    
        for_in_range            0.8617   100  
        for_in_pre_calc_range   0.8538   99   
        itertools_repeat        0.3586   42   
    
    - Python38:
        Name                    Time     %    
        for_in_pre_calc_range   0.6684   100  
        for_in_range            0.6671   100  
        itertools_repeat        0.3496   52 
        
    - Python27:
        Name                    Time     %    
        for_in_range            1.1602   100  
        for_in_pre_calc_range   0.42     36   
        itertools_repeat        0.4038   35   
"""
