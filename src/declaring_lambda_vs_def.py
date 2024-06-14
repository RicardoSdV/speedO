"""

What is faster? Declaring a normal function or a lambda function

"""
from src.z_data import data
from src.z_tester import tester


def declaring_lambda():
    for _ in data.M100_repeat:
        lmbd = lambda x: None


def declaring_func():
    for _ in data.M100_repeat:
        def func(): return


tester(
    (
        declaring_lambda,
        declaring_func
    )
)

"""
Conclusion:
    
    - No difference

    Python27:
        Name               Time     %    
        declaring_lambda   2.1062   100  
        declaring_func     2.1002   100  

    Python38:
        Name               Time     %    
        declaring_lambda   2.0384   100  
        declaring_func     2.033    100  
        
    Python312:
        Name               Time     %    
        declaring_func     3.0209   100  
        declaring_lambda   3.0192   100  


"""
