from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester
_dict = {'myKey': 1}

class _Slots(object):
    __slots__ = ('myKey', )

slots = _Slots()
slots.myKey = 1

class _NoSlots(object):
    pass

no_slots = _NoSlots()
no_slots.myKey = 1

num = data.M100


def access_dict(__dict=_dict):
    for _ in repeat(None, num):
        __dict['myKey']

def access_slots(_slots=slots):
    for _ in repeat(None, num):
        _slots.myKey

def access_noSlots(_no_slots=no_slots):
    for _ in repeat(None, num):
        _no_slots.myKey


auto_tester()

"""
Conclusion:
- Dict in 27, noSlots in 312, normal instance all else.

Python27:
    Name             Secs     %    
    access_noSlots   1.6244   100  
    access_slots     1.5824   97   
    access_dict      1.4638   90 

Python38:
    Name             Secs     %    
    access_dict      1.0865   100  
    access_noSlots   1.0637   98   
    access_slots     0.9982   92   

Python310:
    Name             Secs     %    
    access_dict      1.4123   100  
    access_noSlots   1.3139   93   
    access_slots     1.257    89  

Python312:
    Name             Secs     %    
    access_dict      1.0006   100  
    access_slots     0.7147   71   
    access_noSlots   0.6918   69   
"""



