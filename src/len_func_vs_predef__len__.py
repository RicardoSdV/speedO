from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10
hun_ints = data.hun_ints


def len_fun(_len=len, _hun_ints=hun_ints):
    for _ in repeat(None, num):
        _len(_hun_ints)

def partial_len_fun():
    _len = partial(len, hun_ints)
    for _ in repeat(None, num):
        _len()

def predef___len__():
    _len = hun_ints.__len__
    for _ in repeat(None, num):
        _len()

auto_tester()


"""
Conclusion:
Yeah, just use len()

Python27:
Name              Secs     %    
partial_len_fun   0.2338   100  
predef___len__    0.1928   82   
len_fun           0.1438   62   

Python38:
Name              Secs     %    
partial_len_fun   0.1844   100  
predef___len__    0.13     70   
len_fun           0.1119   61   

Python310:
Name              Secs     %    
partial_len_fun   0.161    100  
predef___len__    0.1516   94   
len_fun           0.1314   82   

Python312:
Name              Secs     %    
partial_len_fun   0.1773   100  
predef___len__    0.1612   91   
len_fun           0.1063   60   

"""
