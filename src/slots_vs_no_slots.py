from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Slots(object):
    __slots__ = ('a1', )
    def __init__(self):
        self.a1 = 1

    def meth(self): return


class NoSlots(object):
    def __init__(self):
        self.a1 = 1

    def meth(self): return


slots = Slots()
no_slots = NoSlots()

num = data.M100

def call_slots_attr():
    _slots = slots
    for _ in repeat(None, num):
        _slots.a1

def call_no_slots_attr():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.a1

def call_slots_meth():
    _slots = slots
    for _ in repeat(None, num):
        _slots.meth()

def call_no_slots_meth():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.meth()


tester(
    (
        call_slots_attr,
        call_no_slots_attr,
    )
)

tester(
    (
        call_slots_meth,
        call_no_slots_meth,
    )
)

"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_attr   1.6502   100  
        call_slots_attr      1.6016   97   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_meth   4.2954   100  
        call_slots_meth      3.5694   83   

    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_attr   1.0686   100  
        call_slots_attr      1.0097   94   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_meth   2.6497   100  
        call_slots_meth      2.5042   95   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_attr   1.2925   100  
        call_slots_attr      1.2192   94   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_meth   3.0057   100  
        call_slots_meth      2.9217   97   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_slots_attr      0.7007   100  
        call_no_slots_attr   0.6821   97   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_no_slots_meth   1.635    100  
        call_slots_meth      1.6172   99   
"""
