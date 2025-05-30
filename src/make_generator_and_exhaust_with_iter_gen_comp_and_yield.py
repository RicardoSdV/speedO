from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester


num = data.M
seq = [1] * 30

def _use_iter(seq):
    return iter(seq)

def _use_gen_comp(seq):
    return (el for el in seq)

def _use_yield_gen(seq):
    for el in seq:
        yield el

def make_and_exhaust_with_iter(_seq=seq, make_gen=_use_iter):
    for _ in repeat(None, num):
        for el in make_gen(_seq):
            continue

def make_and_exhaust_with_gen_comp(_seq=seq, make_gen=_use_gen_comp):
    for _ in repeat(None, num):
        for el in make_gen(_seq):
            continue

def make_and_exhaust_with_yield(_seq=seq, make_gen=_use_yield_gen):
    for _ in repeat(None, num):
        for el in make_gen(_seq):
            continue


auto_tester()


"""
Python27:
    Name                             Secs     %    
    make_and_exhaust_with_gen_comp   0.6886   100  
    make_and_exhaust_with_yield      0.622    90   
    make_and_exhaust_with_iter       0.1968   28   
    
Python38:
    Name                             Secs     %    
    make_and_exhaust_with_gen_comp   0.6046   100  
    make_and_exhaust_with_yield      0.5944   98   
    make_and_exhaust_with_iter       0.1457   24    

Python310:
    Name                             Secs     %    
    make_and_exhaust_with_gen_comp   0.7031   100  
    make_and_exhaust_with_yield      0.6425   91   
    make_and_exhaust_with_iter       0.1631   23   
    
Python312:
    Name                             Secs     %    
    make_and_exhaust_with_gen_comp   0.5373   100  
    make_and_exhaust_with_yield      0.4796   89   
    make_and_exhaust_with_iter       0.1556   28   
"""
