from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M10
numSmaller = data.k10

bestCase = [True]
worstCase = [False, False, False]
very_long_worst_case = [False] * 1000

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

def for_worst_case(_worstCase=worstCase, _num=num):
    for _ in repeat(None, _num):
        for el in _worstCase:
            if el: break

def any_for_and_gen(_worstCase=worstCase):
    for _ in repeat(None, num):
        any((el for el in _worstCase))

def any_for_no_gen(_worstCase=worstCase, _num=num):
    for _ in repeat(None, _num):
        any(el for el in _worstCase)

for_very_long = partial(for_worst_case, very_long_worst_case, numSmaller); for_very_long.__name__ = 'for_very_long'
any_very_long = partial(any_for_no_gen, very_long_worst_case, numSmaller); any_very_long.__name__ = 'any_very_long'

# tester(
#     (
#         any_best_case,
#         for_best_case,
#     ),
# )
#
# tester(
#     (
#         any_worst_case,
#         for_worst_case,
#     ),
# )

# tester(
#     (
#         any_for_and_gen,
#         any_for_no_gen,
#         for_worst_case,
#     ),
# )

tester(
    (
        for_very_long,
        any_very_long,
    ),
)

"""
Conclusion (third test 10x less repeats):
    - In general if you're going to put a for loop inside any()
    its 3x-5x faster to just use a for loop, if no for loop is involved
    just trying to check the truthiness of the elements of an iterable
    using any() is better.
    
    - Also unlike tuple(), passing a generator to any() does not make it faster
    than a bare for loop.
    
    Python27:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   3.0738   100  
        for_best_case   2.498    81   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        for_worst_case   3.9644   100  
        any_worst_case   3.6356   92   
        
        Name              Secs     %    
        any_for_no_gen    1.579    100  
        any_for_and_gen   1.5744   100  
        for_worst_case    0.4014   25   
        
        Name            Secs     %    
        any_very_long   0.1606   100  
        for_very_long   0.0562   35   
        
    Python38:
        Name            Secs     %    
        any_best_case   2.4527   100  
        for_best_case   1.6876   69   
        
        Name             Secs     %    
        any_worst_case   3.2234   100  
        for_worst_case   2.7824   86   
        
        Name              Secs     %    
        any_for_and_gen   1.3244   100  
        any_for_no_gen    1.3239   100  
        for_worst_case    0.2804   21   
        
        Name            Secs     %    
        any_very_long   0.1409   100  
        for_very_long   0.0444   32   
        
    Python310:
        Name            Secs     %    
        any_best_case   2.7453   100  
        for_best_case   1.8616   68   
        
        Name             Secs     %    
        for_worst_case   3.8939   100  
        any_worst_case   3.5042   90   
        
        Name              Secs     %    
        any_for_no_gen    1.5161   100  
        any_for_and_gen   1.5057   99   
        for_worst_case    0.3723   25   
        
        Name            Secs     %    
        any_very_long   0.1628   100  
        for_very_long   0.0742   46   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        any_best_case   2.7453   100  
        for_best_case   1.8616   68   
        
        Testing times mean of 5 rounds: 
        Name             Secs     %    
        for_worst_case   3.8939   100  
        any_worst_case   3.5042   90   
        
        Name              Secs     %    
        any_for_no_gen    1.4934   100  
        any_for_and_gen   1.4908   100  
        for_worst_case    0.3083   21   
        
        Name            Secs     %    
        any_very_long   0.1684   100  
        for_very_long   0.057    34   
"""
