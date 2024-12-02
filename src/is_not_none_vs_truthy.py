from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Class(object):
    __slots__ = ()


obj = Class()
num = data.M100


def is_not_none():
    _obj = obj
    for _ in repeat(None, num):
        if _obj is not None: continue

def truthy():
    _obj = obj
    for _ in repeat(None, num):
        if _obj: continue

tester(
    (
        is_not_none,
        truthy,
    ),
)


"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        is_not_none   0.9646   100  
        truthy        0.9008   93   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        is_not_none   0.8031   100  
        truthy        0.7256   90   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        truthy        0.9639   100  
        is_not_none   0.9532   99   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        truthy        0.7116   100  
        is_not_none   0.5601   79   
"""



