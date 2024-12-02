from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M100

bestCase = [True]
worstCase = [False, False, False]

def any_best_case():
    _bestCase = bestCase
    for _ in repeat(None, num):
        any(_bestCase)

def any_worst_case():
    _worstCase = worstCase
    for _ in repeat(None, num):
        any(_worstCase)

def for_best_case():
    _bestCase = bestCase
    for _ in repeat(None, num):
        for el in _bestCase:
            if el: break

def for_worst_case():
    _worstCase = worstCase
    for _ in repeat(None, num):
        for el in _worstCase:
            if el: break

tester(
    (
        any_best_case,
        for_best_case,
    ),
)

tester(
    (
        any_worst_case,
        for_worst_case,
    ),
)

"""
Conclusion:
    Python27:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   3.0738   100  
        for_best_case   2.498    81   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        for_worst_case   3.9644   100  
        any_worst_case   3.6356   92   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   2.4527   100  
        for_best_case   1.6876   69   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        any_worst_case   3.2234   100  
        for_worst_case   2.7824   86   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   2.7453   100  
        for_best_case   1.8616   68   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        for_worst_case   3.8939   100  
        any_worst_case   3.5042   90   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   2.7453   100  
        for_best_case   1.8616   68   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        for_worst_case   3.8939   100  
        any_worst_case   3.5042   90   
"""
