"""
So, what's more efficient? elifs or a dict of callables?
assuming the key could not exist but will exist > 99.99%
& all the keys will receive the same amount of traffic
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
            if key in _dict_of_callables:
                _dict_of_callables[key]()

def dict_of_callables_2():
    _shuffled_range_2 = shuffled_range_2
    for _ in repeat(None, num):
        for key in _shuffled_range_2:
            if key in _dict_of_callables:
                _dict_of_callables[key]()

def dict_of_callables_4():
    _shuffled_range_4 = shuffled_range_4
    for _ in repeat(None, num):
        for key in _shuffled_range_4:
            if key in _dict_of_callables:
                _dict_of_callables[key]()

def dict_of_callables_8():
    _shuffled_range_8 = shuffled_range_8
    for _ in repeat(None, num):
        for key in _shuffled_range_8:
            if key in _dict_of_callables:
                _dict_of_callables[key]()

def dict_of_callables_16():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            if key in _dict_of_callables:
                _dict_of_callables[key]()

def elifs_1():
    _shuffled_range_1 = shuffled_range_1
    for _ in repeat(None, num):
        for key in _shuffled_range_1:
            if key == 1: callable1()

def elifs_2():
    _shuffled_range_2 = shuffled_range_2
    for _ in repeat(None, num):
        for key in _shuffled_range_2:
            if key == 1: callable1()
            elif key == 2: callable2()

def elifs_4():
    _shuffled_range_4 = shuffled_range_4
    for _ in repeat(None, num):
        for key in _shuffled_range_4:
            if key == 1: callable1()
            elif key == 2: callable2()
            elif key == 3: callable3()
            elif key == 4: callable4()

def elifs_8():
    _shuffled_range_8 = shuffled_range_8
    for _ in repeat(None, num):
        for key in _shuffled_range_8:
            if key == 1: callable1()
            elif key == 2: callable2()
            elif key == 3: callable3()
            elif key == 4: callable4()
            elif key == 5: callable5()
            elif key == 6: callable6()
            elif key == 7: callable7()
            elif key == 8: callable8()

def elifs_16():
    _shuffled_range_16 = shuffled_range_16
    for _ in repeat(None, num):
        for key in _shuffled_range_16:
            if key == 1: callable1()
            elif key == 2: callable2()
            elif key == 3: callable3()
            elif key == 4: callable4()
            elif key == 5: callable5()
            elif key == 6: callable6()
            elif key == 7: callable7()
            elif key == 8: callable8()
            elif key == 9: callable9()
            elif key == 10: callable10()
            elif key == 11: callable11()
            elif key == 12: callable12()
            elif key == 13: callable13()
            elif key == 14: callable14()
            elif key == 15: callable15()
            elif key == 16: callable16()

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
    - Across the board at about 8 elements it starts becoming worth it
    to use a dict of callables instead of a bunch of elifs. Of course
    if you dont need to check weather the key exists in the dict it will
    be faster

    Python27:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.3812   100  
        dict_of_callables_16   0.7972   57   
        elifs_8                0.485    35   
        dict_of_callables_8    0.4138   30   
        dict_of_callables_4    0.2214   16   
        elifs_4                0.1862   13   
        dict_of_callables_2    0.119    9    
        elifs_2                0.0978   7    
        dict_of_callables_1    0.0702   5    
        elifs_1                0.055    4    
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.4255   100  
        dict_of_callables_16   0.6566   46   
        elifs_8                0.4679   33   
        dict_of_callables_8    0.3412   24   
        dict_of_callables_4    0.1785   13   
        elifs_4                0.1738   12   
        dict_of_callables_2    0.092    6    
        elifs_2                0.0766   5    
        dict_of_callables_1    0.051    4    
        elifs_1                0.0407   3    
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.6478   100  
        dict_of_callables_16   0.7648   46   
        elifs_8                0.5192   32   
        dict_of_callables_8    0.3942   24   
        dict_of_callables_4    0.213    13   
        elifs_4                0.2038   12   
        dict_of_callables_2    0.1059   6    
        elifs_2                0.0903   5    
        dict_of_callables_1    0.059    4    
        elifs_1                0.0463   3    
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                   Secs     %    
        elifs_16               1.2657   100  
        dict_of_callables_16   0.5545   44   
        elifs_8                0.3726   28   
        dict_of_callables_8    0.292    23   
        dict_of_callables_4    0.1483   12   
        elifs_4                0.1395   11   
        dict_of_callables_2    0.0765   6    
        elifs_2                0.0626   5    
        dict_of_callables_1    0.0448   4    
        elifs_1                0.0353   3    

"""
