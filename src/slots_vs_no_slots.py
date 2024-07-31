from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Slots(object):
    __slots__ = ('a1', )
    def __init__(self):
        self.a1 = 1


class NoSlots(object):
    def __init__(self):
        self.a1 = 1


slots = Slots()
no_slots = NoSlots()

num = data.M100

def call_slots():
    _slots = slots
    for _ in repeat(None, num):
        _local1 = _slots.a1


def call_no_slots():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _local1 = _no_slots.a1


tester(
    (
        call_slots,
        call_no_slots,
    )
)

"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_no_slots   1.481    100  
        call_slots      1.4564   98   

    Python38:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_no_slots   1.0591   100  
        call_slots      1.0035   95   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_no_slots   1.2256   100  
        call_slots      1.1669   95   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_slots      0.7153   100  
        call_no_slots   0.7019   98   
        
"""

