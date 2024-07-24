"""
What is the fastest way to pass args to a callable?
"""

from itertools import repeat

from src.z_data import data
from src.z_tester import tester

def func(arg): pass
def func2(): pass

num = data.M100
arg_to_pass = 1

def pass_by_order():
    for _ in repeat(None, num):
        func(arg_to_pass)

def pass_by_kw():
    for _ in repeat(None, num):
        func(arg=arg_to_pass)

def pass_no_args1():
    for _ in repeat(None, num):
        func2()


def func_many(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10): pass

num2 = data.M10
pass_arg1, pass_arg2, pass_arg3, pass_arg4, pass_arg5, pass_arg6, pass_arg7, pass_arg8, pass_arg9, pass_arg10 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

def pass_by_order_many():
    for _ in repeat(None, num2):
        func_many(pass_arg1, pass_arg2, pass_arg3, pass_arg4, pass_arg5, pass_arg6, pass_arg7, pass_arg8, pass_arg9, pass_arg10)

def pass_mix_many():
    for _ in repeat(None, num2):
        func_many(pass_arg1, pass_arg2, pass_arg3, pass_arg4, pass_arg5, arg6=pass_arg6, arg7=pass_arg7, arg8=pass_arg8, arg9=pass_arg9, arg10=pass_arg10)

def pass_by_kw_many():
    for _ in repeat(None, num2):
        func_many(arg1=pass_arg1, arg2=pass_arg2, arg3=pass_arg3, arg4=pass_arg4, arg5=pass_arg5, arg6=pass_arg6, arg7=pass_arg7, arg8=pass_arg8, arg9=pass_arg9, arg10=pass_arg10)

def pass_no_args2():
    for _ in repeat(None, num2):
        func2()

tester(
    (
        pass_by_order,
        pass_by_kw,
        pass_no_args1,
    )
)

tester(
    (
        pass_by_order_many,
        pass_mix_many,
        pass_by_kw_many,
        pass_no_args2,
    )
)


"""
Conclusion:
    Makes sense, passing by order is faster, the more args passed by kw the slower, 
    also, the more args passed in general the slower

    Python312:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        pass_by_kw      2.3763   100  
        pass_by_order   1.7857   75   
        pass_no_args1   1.5807   67   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        pass_by_kw_many      0.7187   100  
        pass_mix_many        0.6547   91   
        pass_by_order_many   0.4546   63   
        pass_no_args2        0.158    22   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        pass_by_kw      3.5503   100  
        pass_by_order   3.2061   90   
        pass_no_args1   2.6879   76   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        pass_by_kw_many      1.2211   100  
        pass_mix_many        1.0901   89   
        pass_by_order_many   0.8351   68   
        pass_no_args2        0.281    23   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        pass_by_kw      5.004    100  
        pass_by_order   4.047    81   
        pass_no_args1   3.4338   69   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        pass_by_kw_many      0.9379   100  
        pass_mix_many        0.8228   88   
        pass_by_order_many   0.6915   74   
        pass_no_args2        0.2294   24  
    
    Python27:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        pass_by_kw      3.7266   100  
        pass_by_order   3.1588   85   
        pass_no_args1   2.6038   70   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        pass_by_kw_many      1.1696   100  
        pass_mix_many        1.0032   86   
        pass_by_order_many   0.7462   64   
        pass_no_args2        0.2596   22   
        
"""

