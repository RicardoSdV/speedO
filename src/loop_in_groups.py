import itertools
import sys

from src.z_data import data
from z_tester import tester_2d

""" Small group """


def for_i_next_2(outer):
    for inner in outer:
        for i in range(len(inner) - 2):
            next2 = [inner[i + j] for j in range(2)]


def slice_next_2(outer):
    for inner in outer:
        for i in range(len(inner) - 2):
            next2 = inner[i:i + 2]


if sys.version.startswith('2'):
    def itertools_tee_next_2(outer):
        for inner in outer:
            a, b = itertools.tee(inner)
            for next2 in itertools.izip(a, b):
                list(next2)  # Kind of wierd bc we already have x, y no need to make a list but others do make lists

else:
    def itertools_tee_next_2(outer):
        for inner in outer:
            a, b = itertools.tee(inner)
            for next2 in zip(a, b):
                list(next2)

"""=============================================="""

""" Larger group """


def for_i_next_9(outer):
    for inner in outer:
        for i in range(len(inner) - 9):
            next9 = [inner[i + j] for j in range(9)]


def slice_next_9(outer):
    for inner in outer:
        for i in range(len(inner) - 9):
            next9 = inner[i:i + 9]


if sys.version.startswith('2'):
    def itertools_tee_next_9(outer):
        for inner in outer:
            iterators = itertools.tee(inner, 9)
            for next9 in itertools.izip(*iterators):
                list(next9)

else:
    def itertools_tee_next_9(outer):
        for inner in outer:
            iterators = itertools.tee(inner, 9)
            for next9 in zip(*iterators):
                list(next9)

"""=============================================="""

tester_2d(
    (
        for_i_next_2,
        slice_next_2,
        itertools_tee_next_2,
        for_i_next_9,
        slice_next_9,
        itertools_tee_next_9,
    ),
    list_3d=data.super_fast_3d_list
)

"""
Conclusion:
    - In general itertools.tee gets better the larger the list, also gets better the more modern
    the version of python.

    Python312:
        - for small lists, or, large groups use slicing, for large lists and small groups use
        itertools.tee
    
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 10: 
        Name                   Time     %    
        itertools_tee_next_9   0.0878   100  
        for_i_next_2           0.066    75   
        itertools_tee_next_2   0.0636   72   
        slice_next_2           0.0331   38   
        for_i_next_9           0.0234   27   
        slice_next_9           0.0088   10   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 100: 
        Name                   Time     %    
        for_i_next_9           0.1592   100  
        for_i_next_2           0.0744   47   
        itertools_tee_next_9   0.0591   37   
        itertools_tee_next_2   0.0407   26   
        slice_next_9           0.0351   22   
        slice_next_2           0.0339   21   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 1 000: 
        Name                   Time     %    
        for_i_next_9           0.2061   100  
        for_i_next_2           0.0865   42   
        itertools_tee_next_9   0.0703   34   
        slice_next_9           0.0481   23   
        slice_next_2           0.0424   21   
        itertools_tee_next_2   0.0415   20   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 10 000: 
        Name                   Time     %    
        for_i_next_9           0.2195   100  
        for_i_next_2           0.0894   41   
        itertools_tee_next_9   0.0759   35   
        slice_next_9           0.0514   23   
        slice_next_2           0.0452   21   
        itertools_tee_next_2   0.0433   20   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 100 000: 
        Name                   Time     %    
        for_i_next_9           0.2193   100  
        for_i_next_2           0.09     41   
        itertools_tee_next_9   0.0724   33   
        slice_next_9           0.0516   24   
        slice_next_2           0.0442   20   
        itertools_tee_next_2   0.042    19   

    
    Python38:
        - Slice better
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 10: 
        Name                   Time     %    
        for_i_next_2           0.1565   100  
        itertools_tee_next_9   0.1075   69   
        itertools_tee_next_2   0.068    43   
        for_i_next_9           0.0432   28   
        slice_next_2           0.0383   24   
        slice_next_9           0.0135   9    
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 100: 
        Name                   Time     %    
        for_i_next_9           0.2898   100  
        for_i_next_2           0.1725   60   
        itertools_tee_next_9   0.078    27   
        itertools_tee_next_2   0.0502   17   
        slice_next_9           0.0373   13   
        slice_next_2           0.0351   12   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 1 000: 
        Name                   Time     %    
        for_i_next_9           0.3427   100  
        for_i_next_2           0.1881   55   
        itertools_tee_next_9   0.077    22   
        itertools_tee_next_2   0.0488   14   
        slice_next_9           0.0455   13   
        slice_next_2           0.0403   12   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 10 000: 
        Name                   Time     %    
        for_i_next_9           0.353    100  
        for_i_next_2           0.1891   54   
        itertools_tee_next_9   0.0754   21   
        itertools_tee_next_2   0.0485   14   
        slice_next_9           0.0472   13   
        slice_next_2           0.0422   12   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 100 000: 
        Name                   Time     %    
        for_i_next_9           0.354    100  
        for_i_next_2           0.1895   54   
        itertools_tee_next_9   0.0736   21   
        slice_next_9           0.048    14   
        itertools_tee_next_2   0.0477   13   
        slice_next_2           0.0414   12   
    
    Python27:
        - Slice better
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                   Time     %    
        itertools_tee_next_2   6.5687   100  
        itertools_tee_next_9   2.331    35   
        for_i_next_2           1.5367   23   
        for_i_next_9           1.052    16   
        slice_next_2           0.579    9    
        slice_next_9           0.1877   3    
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                   Time     %    
        for_i_next_9           8.301    100  
        itertools_tee_next_2   6.091    73   
        for_i_next_2           1.7283   21   
        itertools_tee_next_9   1.4597   18   
        slice_next_9           0.5627   7    
        slice_next_2           0.541    7    
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                   Time     %    
        for_i_next_9           8.998    100  
        itertools_tee_next_2   6.0557   67   
        for_i_next_2           1.7517   19   
        itertools_tee_next_9   1.3653   15   
        slice_next_9           0.6227   7    
        slice_next_2           0.5623   6    
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                   Time     %    
        for_i_next_9           9.113    100  
        itertools_tee_next_2   6.0513   66   
        for_i_next_2           1.7777   20   
        itertools_tee_next_9   1.3597   15   
        slice_next_9           0.649    7    
        slice_next_2           0.5873   6    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                   Time     %    
        for_i_next_9           9.1903   100  
        itertools_tee_next_2   6.0613   66   
        for_i_next_2           1.7753   19   
        itertools_tee_next_9   1.3687   15   
        slice_next_9           0.6713   7    
        slice_next_2           0.5913   6    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                   Time     %    
        for_i_next_9           9.2883   100  
        itertools_tee_next_2   6.0967   66   
        for_i_next_2           1.871    20   
        itertools_tee_next_9   1.3947   15   
        slice_next_9           0.6877   7    
        slice_next_2           0.6273   7    

"""
