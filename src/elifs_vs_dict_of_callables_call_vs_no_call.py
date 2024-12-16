"""
So, what's more efficient? elifs or a dict of callables?
assuming all the keys exist & the dict uses callables,
but the elifs write the simple code directly.
"""
from itertools import repeat
from random import shuffle

from src.z_data import data
from src.z_tester import tester

def callable1(): return
def callable2(): return
def callable3(): return
def callable4(): return
def callable5(): return
def callable6(): return
def callable7(): return
def callable8(): return
def callable9(): return
def callable10(): return
def callable11(): return
def callable12(): return
def callable13(): return
def callable14(): return
def callable15(): return
def callable16(): return

_dict_of_callables = {
    1:callable1,
    2:callable2,
    3:callable3,
    4:callable4,
    5:callable5,
    6:callable6,
    7:callable7,
    8:callable8,
    9:callable9,
    10:callable10,
    11:callable11,
    12:callable12,
    13:callable13,
    14:callable14,
    15:callable15,
    16:callable16,
}

num = data.M

shuffled_range_1  = [1];               shuffle(shuffled_range_1)
shuffled_range_2  = list(range(1,3));  shuffle(shuffled_range_2)
shuffled_range_4  = list(range(1,5));  shuffle(shuffled_range_4)
shuffled_range_8  = list(range(1,9));  shuffle(shuffled_range_8)
shuffled_range_16 = list(range(1,17)); shuffle(shuffled_range_16)


def dict_of_callables_1():
    _shuffled_range_1 = shuffled_range_1
    for _ in repeat(None, num):
        for key in _shuffled_range_1:
            _dict_of_callables[key]()

def dict_of_callables_2():
    _shuffled_range_2 = shuffled_range_2
    for _ in repeat(None, num):
        for key in _shuffled_range_2:
            _dict_of_callables[key]()

def dict_of_callables_4():
    _shuffled_range_4 = shuffled_range_4
    for _ in repeat(None, num):
        for key in _shuffled_range_4:
            _dict_of_callables[key]()

def dict_of_callables_8():
    _shuffled_range_8 = shuffled_range_8
    for _ in repeat(None, num):
        for key in _shuffled_range_8:
            _dict_of_callables[key]()

def dict_of_callables_16():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            _dict_of_callables[key]()

def elifs_1():
    _shuffled_range_1 = shuffled_range_1
    for _ in repeat(None, num):
        for key in _shuffled_range_1:
            if key == 1: continue

def elifs_2():
    _shuffled_range_2 = shuffled_range_2
    for _ in repeat(None, num):
        for key in _shuffled_range_2:
            if key == 1: continue
            elif key == 2: continue

def elifs_4():
    _shuffled_range_4 = shuffled_range_4
    for _ in repeat(None, num):
        for key in _shuffled_range_4:
            if key == 1: continue
            elif key == 2: continue
            elif key == 3: continue
            elif key == 4: continue

def elifs_8():
    _shuffled_range_8 = shuffled_range_8
    for _ in repeat(None, num):
        for key in _shuffled_range_8:
            if key == 1: continue
            elif key == 2: continue
            elif key == 3: continue
            elif key == 4: continue
            elif key == 5: continue
            elif key == 6: continue
            elif key == 7: continue
            elif key == 8: continue

def elifs_16():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            if key == 1: continue
            elif key == 2: continue
            elif key == 3: continue
            elif key == 4: continue
            elif key == 5: continue
            elif key == 6: continue
            elif key == 7: continue
            elif key == 8: continue
            elif key == 9: continue
            elif key == 10: continue
            elif key == 11: continue
            elif key == 12: continue
            elif key == 13: continue
            elif key == 14: continue
            elif key == 15: continue
            elif key == 16: continue

tester(
    (
        dict_of_callables_1,
        dict_of_callables_2,
        dict_of_callables_4,
        dict_of_callables_8,
        dict_of_callables_16,
        elifs_1,
        elifs_2,
        elifs_4,
        elifs_8,
        elifs_16,
    )
)

"""
Conclusion: 
    - Event when the elifs do no work and the dict has to call a function it still is faster 
    to use a dict across the versions when more than 16 elements. Although this may be more 
    exaggerated if the dict had to call methods which are considerably slower than funcs.

    Python27:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               0.9996   100  
        dict_of_callables_16   0.603    60   
        dict_of_callables_8    0.3192   32   
        elifs_8                0.283    28   
        dict_of_callables_4    0.1746   17   
        elifs_4                0.1002   10   
        dict_of_callables_2    0.096    10   
        dict_of_callables_1    0.06     6    
        elifs_2                0.0472   5    
        elifs_1                0.0314   3    
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.0103   100  
        dict_of_callables_16   0.5033   50   
        elifs_8                0.2751   27   
        dict_of_callables_8    0.2633   26   
        dict_of_callables_4    0.1353   13   
        elifs_4                0.0875   9    
        dict_of_callables_2    0.074    7    
        dict_of_callables_1    0.0436   4    
        elifs_2                0.0369   4    
        elifs_1                0.0212   2    
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.318    100  
        dict_of_callables_16   0.5637   43   
        elifs_8                0.3741   28   
        dict_of_callables_8    0.2932   22   
        dict_of_callables_4    0.1624   12   
        elifs_4                0.1157   9    
        dict_of_callables_2    0.0823   6    
        elifs_2                0.0476   4    
        dict_of_callables_1    0.0474   4    
        elifs_1                0.0253   2       
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.1148   100  
        dict_of_callables_16   0.4547   41   
        elifs_8                0.3107   28   
        dict_of_callables_8    0.2415   22   
        dict_of_callables_4    0.123    11   
        elifs_4                0.1023   9    
        dict_of_callables_2    0.0642   6    
        elifs_2                0.0428   4    
        dict_of_callables_1    0.038    3    
        elifs_1                0.0239   2    
 
"""
