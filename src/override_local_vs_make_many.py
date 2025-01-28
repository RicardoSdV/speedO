from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

def _retOne(): return 1

def _override(ret=_retOne):
    ret=ret()

def _make(ret=_retOne):
    ret1=ret()

num = data.M100

def call_override(override=_override):
    for _ in repeat(None, num):
        override()

def call_make(make=_make):
    for _ in repeat(None, num):
        make()


auto_tester()

"""
Conclusion:
    Overriding slightly faster lots of overhead though, so more

    Python27:
        Name            Secs     %    
        call_make       5.161    100  
        call_override   5.0654   98  
        
    Python38:
        Name            Secs     %    
        call_override   3.981    100  
        call_make       3.9536   99   
    
    Python310:
        Name            Secs     %    
        call_make       4.7224   100  
        call_override   4.6908   99   
    
    Python312:
        Name            Secs     %    
        call_make       3.2812   100  
        call_override   3.2375   99   
"""



