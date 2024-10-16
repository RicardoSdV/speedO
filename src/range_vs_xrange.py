from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M

def _range():
    for _ in repeat(None, num):
        for i in range(5):
            continue

def _xrange():
    for _ in repeat(None, num):
        for i in xrange(5):
            continue

def _RevXrange():
    for _ in repeat(None, num):
        for i in reversed(xrange(5)):
            continue

def _RevXrange2():
    for _ in repeat(None, num):
        for i in reversed(xrange(1, 5+1)):
            continue

def _RevRange():
    for _ in repeat(None, num):
        for i in reversed(range(1, 5+1)):
            continue

def _InvXrange():
    for _ in repeat(None, num):
        for i in xrange(5, 1-1, -1):
            continue


tester(
    (
        _range,
        _xrange,
        _RevXrange,
    )
)

tester(
    (
        _RevRange,
        _InvXrange,
        _RevXrange2,
    )
)

"""
Conclusion:
    Python27:
    Testing times mean of 5 rounds: 
    Name              Secs     %    
    _Reversedxrange   0.1356   100  
    _range            0.128    94   
    _xrange           0.0906   67   
    
    
    Testing times mean of 5 rounds: 
    Name          Secs     %    
    _RevRange     0.1956   100  
    _RevXrange2   0.1474   75   
    _InvXrange    0.1146   59   

"""


