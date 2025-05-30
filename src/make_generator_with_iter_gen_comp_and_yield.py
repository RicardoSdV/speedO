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

def make_with_iter(_seq=seq, make_gen=_use_iter):
    for _ in repeat(None, num):
        make_gen(_seq)

def make_with_gen_comp(_seq=seq, make_gen=_use_gen_comp):
    for _ in repeat(None, num):
        make_gen(_seq)

def make_with_yield(_seq=seq, make_gen=_use_yield_gen):
    for _ in repeat(None, num):
        make_gen(_seq)


auto_tester()


"""
Python27:
    Name                 Secs     %    
    make_with_gen_comp   0.177    100  
    make_with_yield      0.1182   67   
    make_with_iter       0.0552   31  
    
Python38:
    Name                 Secs     %    
    make_with_gen_comp   0.1128   100  
    make_with_yield      0.0648   56   
    make_with_iter       0.0371   33   

Python310:
    Name                 Secs     %    
    make_with_gen_comp   0.125    100  
    make_with_yield      0.0659   53   
    make_with_iter       0.0417   33   
    
Python312:
    Name                 Secs     %    
    make_with_gen_comp   0.0883   100  
    make_with_yield      0.0365   41   
    make_with_iter       0.0353   40   
"""
