"""
Is it slower to use a lambda or a function defined somewhere else
"""
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

_list = [0, 1]

num = data.M10

def func(x):
    return x


def lambda_for_condition():
    __list = _list
    for _ in repeat(None, num):
        (lambda x: x)(__list)


def function_for_condition():
    __list = _list
    for _ in repeat(None, num):
        func(__list)


class Class(object):
    __slots__ = ()

    @staticmethod
    def __func(x):
        return x

    def meth_lambda_for_condition(self):
        __list = _list
        for _ in repeat(None, num):
            (lambda x: x)(__list)


    def meth_function_for_condition(self):
        __list = _list
        for _ in repeat(None, num):
            self.__func(__list)

obj = Class()

tester(
    (
        lambda_for_condition,
        function_for_condition,
        obj.meth_function_for_condition,
        obj.meth_lambda_for_condition,
    )
)


""" 
Conclusion:
    - Surprisingly python27 ifs almost as good if not better than python312

    Python27:
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        lambda_for_condition          0.4966   100  
        meth_lambda_for_condition     0.4962   100  
        meth_function_for_condition   0.3356   68   
        function_for_condition        0.282    56   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        meth_lambda_for_condition     0.415    100  
        lambda_for_condition          0.4114   99   
        meth_function_for_condition   0.2694   65   
        function_for_condition        0.2513   61   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        meth_lambda_for_condition     0.5487   100  
        lambda_for_condition          0.5431   99   
        meth_function_for_condition   0.3192   57   
        function_for_condition        0.2972   54   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                          Secs     %    
        lambda_for_condition          0.4392   100  
        meth_lambda_for_condition     0.4285   98   
        meth_function_for_condition   0.234    53   
        function_for_condition        0.2073   47   
    
"""
