""" Sometimes one might choose to return something just in case it might be needed in the future,
is this any less efficient that not returning anything? """
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M10

def just_pass(): pass
def return_none_implicit(): return
def return_none_explicit(): return None
def return_bool(): return True
def return_int(): return 55
def return_str(): return 'lsdkjfzl'


def call_just_pass():
    for _ in repeat(None, num):
        just_pass()

def call_return_none_implicit():
    for _ in repeat(None, num):
        return_none_implicit()

def call_return_none_explicit():
    for _ in repeat(None, num):
        return_none_explicit()

def call_return_bool():
    for _ in repeat(None, num):
        return_bool()

def call_return_int():
    for _ in repeat(None, num):
        return_bool()

def call_return_str():
    for _ in repeat(None, num):
        return_bool()

tester(
    (
        call_just_pass,
        call_return_none_implicit,
        call_return_none_explicit,
        call_return_bool,
        call_return_int,
        call_return_str,
    )
)

"""
Conclusion:
    Surprisingly returning anything other than None is more efficient in
    Python27 which seems crazy, in every other version theres no real difference
    except to say that func calls in general are 100 times faster in PyPy 
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_return_bool            0.3584   100  
        call_return_int             0.3562   99   
        call_return_str             0.3556   99   
        call_just_pass              0.2874   80   
        call_return_none_implicit   0.27     75   
        call_return_none_explicit   0.2618   73   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_return_bool            0.2328   100  
        call_return_str             0.2319   100  
        call_return_int             0.2311   99   
        call_return_none_implicit   0.2295   99   
        call_return_none_explicit   0.2291   98   
        call_just_pass              0.2289   98   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_return_bool            0.2694   100  
        call_return_int             0.2689   100  
        call_just_pass              0.2682   100  
        call_return_none_implicit   0.2679   99   
        call_return_str             0.2677   99   
        call_return_none_explicit   0.2669   99   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_return_str             0.1619   100  
        call_return_none_implicit   0.1584   98   
        call_just_pass              0.1583   98   
        call_return_none_explicit   0.1582   98   
        call_return_bool            0.1581   98   
        call_return_int             0.1578   98   
    
    PyPy313:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_return_str             0.006    100  
        call_return_int             0.0058   97   
        call_return_none_explicit   0.0058   97   
        call_return_none_implicit   0.0058   96   
        call_just_pass              0.0058   96   
        call_return_bool            0.0056   93   

"""
