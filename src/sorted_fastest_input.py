""" Lets' say we have the choice to either pass an iterable to sorted or a
list or do list().sort(), what is the fastest? """
from copy import deepcopy
from time import time

from src.z_data import data, inner_to_iter_of_2d
from src.z_tester import tester_2d


def sorted_list(outer):
    start = time()
    for inner in outer:
        _sorted = sorted(inner)
    return time() - start

def sort_list(outer):
    _outer = deepcopy(outer)

    start = time()
    for inner in _outer:
        inner.sort()
    return time() - start

def copy_and_sort_list(outer):
    # For when you need both the sorted and unsorted
    start = time()
    for inner in outer:
        _copy = list(inner)
        _copy.sort()
    return time() - start

def sorted_iter(outer):
    _outer = inner_to_iter_of_2d(outer)

    start = time()
    for inner in _outer:
        _sorted = sorted(inner)
    return time() - start


tester_2d(
    (
        sorted_list,
        sort_list,
        sorted_iter,
        copy_and_sort_list,
    ),
    list_3d=data.faster_3d_list_rev_inner,
    return_time=True,
)


"""
Conclusion:
        - list().sort() always better, copy and sort surprisingly good
        specially because I used the generic fastest method for copying which
        is list() but there is a best way of copying a list for each expected
        length and python version. See .fastest_way_of_doing_shallow_copy_of_list.py
        
    Python27:
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name                 Secs     %    
        sorted_iter          0.3637   100  
        sorted_list          0.217    60   
        copy_and_sort_list   0.2087   56   
        sort_list            0.0887   24   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                 Secs     %    
        sorted_iter          0.1077   100  
        sorted_list          0.0843   78   
        copy_and_sort_list   0.0823   76   
        sort_list            0.0513   48   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0827   100  
        sorted_list          0.0757   92   
        copy_and_sort_list   0.0737   89   
        sort_list            0.0503   61   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0813   100  
        copy_and_sort_list   0.072    89   
        sorted_list          0.0707   87   
        sort_list            0.0517   64   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0857   100  
        copy_and_sort_list   0.077    90   
        sorted_list          0.0767   89   
        sort_list            0.0497   57   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0983   100  
        copy_and_sort_list   0.092    94   
        sorted_list          0.0913   93   
        sort_list            0.0503   51   
        
    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                 Secs     %    
        sorted_iter          0.1031   100  
        copy_and_sort_list   0.0853   83   
        sorted_list          0.0785   76   
        sort_list            0.0405   39   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                 Secs     %    
        sorted_iter          0.0594   100  
        copy_and_sort_list   0.047    79   
        sorted_list          0.0445   75   
        sort_list            0.0284   48   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0533   100  
        sorted_list          0.0472   89   
        copy_and_sort_list   0.0468   88   
        sort_list            0.0343   64   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                 Secs     %    
        copy_and_sort_list   0.0559   100  
        sorted_iter          0.0559   100  
        sorted_list          0.0484   87   
        sort_list            0.035    63   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                 Secs     %    
        copy_and_sort_list   0.0649   100  
        sorted_iter          0.0609   94   
        sorted_list          0.0566   87   
        sort_list            0.0368   56   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0924   100  
        sorted_list          0.089    96   
        copy_and_sort_list   0.0845   92   
        sort_list            0.0421   46   
        
    Python 310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                 Secs     %    
        sorted_iter          0.1144   100  
        sorted_list          0.0857   75   
        copy_and_sort_list   0.0817   71   
        sort_list            0.041    36   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                 Secs     %    
        sorted_iter          0.0549   100  
        sorted_list          0.046    84   
        copy_and_sort_list   0.0416   76   
        sort_list            0.0262   48   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0498   100  
        sorted_list          0.044    88   
        copy_and_sort_list   0.0431   87   
        sort_list            0.0307   62   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0499   100  
        sorted_list          0.0446   89   
        copy_and_sort_list   0.0433   87   
        sort_list            0.0316   63   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                 Secs     %    
        sorted_iter          0.06     100  
        copy_and_sort_list   0.0567   95   
        sorted_list          0.052    87   
        sort_list            0.0326   54   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0864   100  
        sorted_list          0.0826   96   
        copy_and_sort_list   0.0803   93   
        sort_list            0.0395   46   
        
    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                 Secs     %    
        sorted_iter          0.1046   100  
        sorted_list          0.0749   72   
        copy_and_sort_list   0.0648   62   
        sort_list            0.0357   34   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                 Secs     %    
        sorted_iter          0.0501   100  
        sorted_list          0.039    78   
        copy_and_sort_list   0.0378   76   
        sort_list            0.0256   51   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0494   100  
        sorted_list          0.0434   88   
        copy_and_sort_list   0.0434   88   
        sort_list            0.032    65   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0515   100  
        copy_and_sort_list   0.0447   87   
        sorted_list          0.0439   85   
        sort_list            0.0338   66   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                 Secs     %    
        sorted_iter          0.0621   100  
        copy_and_sort_list   0.0543   87   
        sorted_list          0.0518   83   
        sort_list            0.0362   57   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                 Secs     %    
        sorted_iter          0.091    100  
        copy_and_sort_list   0.0882   97   
        sorted_list          0.0825   91   
        sort_list            0.0397   44   
    
"""


