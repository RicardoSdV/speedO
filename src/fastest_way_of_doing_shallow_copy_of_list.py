from sys import version

from src.z_tester import tester_2d

def copy_with_list(outer):
    for inner in outer:
        _list = list(inner)

def copy_with_slicing(outer):
    for inner in outer:
        _list = inner[:]

def copy_with_copy(outer):
    from copy import copy
    for inner in outer:
        _list = copy(inner)

def copy_with_list_comprehension(outer):
    for inner in outer:
        _list = [el for el in inner]

callables = [
    copy_with_list,
    copy_with_slicing,
    copy_with_copy,
    copy_with_list_comprehension,
]

if version.startswith('3'):
    def copy_with_unpacking(outer):
        for inner in outer:
            _list = [*inner]

    def copy_with_dot_copy(outer):
        for inner in outer:
            _list = inner.copy()

    callables.extend((copy_with_unpacking, copy_with_dot_copy))


tester_2d(
    callables
)

"""
Conclusion:
    Python27:
        - Slicing for <= 1000, copy() or list() for > 1000
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                           Secs     %    
        copy_with_copy                 0.2643   100  
        copy_with_list_comprehension   0.21     79   
        copy_with_list                 0.1123   42   
        copy_with_slicing              0.0607   23   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1317   100  
        copy_with_copy                 0.04     30   
        copy_with_list                 0.023    17   
        copy_with_slicing              0.0187   14   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1037   100  
        copy_with_list                 0.0213   21   
        copy_with_copy                 0.0213   21   
        copy_with_slicing              0.0213   21   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0957   100  
        copy_with_slicing              0.023    24   
        copy_with_copy                 0.0213   22   
        copy_with_list                 0.0213   22   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0877   100  
        copy_with_slicing              0.0467   53   
        copy_with_list                 0.027    31   
        copy_with_copy                 0.0267   30   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1903   100  
        copy_with_slicing              0.042    22   
        copy_with_copy                 0.041    22   
        copy_with_list                 0.041    22   
        
    Python38:
        - Unpacking for < 100k elements & list() for > 100k
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                           Secs     %    
        copy_with_list_comprehension   0.1338   100  
        copy_with_copy                 0.0834   62   
        copy_with_list                 0.0703   53   
        copy_with_slicing              0.0327   24   
        copy_with_dot_copy             0.0286   21   
        copy_with_unpacking            0.0277   21   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0833   100  
        copy_with_copy                 0.0217   26   
        copy_with_list                 0.0173   21   
        copy_with_slicing              0.0157   19   
        copy_with_dot_copy             0.0155   19   
        copy_with_unpacking            0.015    18   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0807   100  
        copy_with_copy                 0.0207   26   
        copy_with_dot_copy             0.019    24   
        copy_with_slicing              0.0188   23   
        copy_with_list                 0.0187   23   
        copy_with_unpacking            0.0183   23   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0747   100  
        copy_with_dot_copy             0.0217   28   
        copy_with_list                 0.0213   28   
        copy_with_slicing              0.0212   28   
        copy_with_copy                 0.021    28   
        copy_with_unpacking            0.0203   27   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.075    100  
        copy_with_slicing              0.029    39   
        copy_with_copy                 0.0289   39   
        copy_with_unpacking            0.0286   38   
        copy_with_dot_copy             0.0283   38   
        copy_with_list                 0.028    37   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1813   100  
        copy_with_slicing              0.0558   31   
        copy_with_copy                 0.0524   28   
        copy_with_unpacking            0.0437   24   
        copy_with_dot_copy             0.0432   24   
        copy_with_list                 0.0427   24   
        
    Python310:
        - Probably use .copy(), except for very short lists then unpacking
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1692   100  
        copy_with_copy                 0.081    48   
        copy_with_dot_copy             0.0409   24   
        copy_with_list                 0.039    23   
        copy_with_slicing              0.035    21   
        copy_with_unpacking            0.0267   16   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1873   100  
        copy_with_copy                 0.0223   12   
        copy_with_list                 0.0177   9    
        copy_with_slicing              0.0173   9    
        copy_with_dot_copy             0.0167   9    
        copy_with_unpacking            0.016    9    
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1074   100  
        copy_with_list                 0.027    25   
        copy_with_slicing              0.0193   18   
        copy_with_copy                 0.0193   18   
        copy_with_unpacking            0.019    18   
        copy_with_dot_copy             0.0183   17   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0971   100  
        copy_with_copy                 0.0237   24   
        copy_with_slicing              0.023    24   
        copy_with_unpacking            0.0223   23   
        copy_with_dot_copy             0.021    22   
        copy_with_list                 0.021    22   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.085    100  
        copy_with_dot_copy             0.0306   36   
        copy_with_unpacking            0.0303   36   
        copy_with_slicing              0.029    34   
        copy_with_list                 0.0283   33   
        copy_with_copy                 0.028    33   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1887   100  
        copy_with_slicing              0.057    30   
        copy_with_unpacking            0.0513   27   
        copy_with_copy                 0.0461   24   
        copy_with_list                 0.0438   23   
        copy_with_dot_copy             0.0437   23   
        
    Python312:
        - .copy() always better except at 100k elements for some reason
    
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 

        Name                           Secs     %    
        copy_with_list_comprehension   0.1007   100  
        copy_with_copy                 0.0637   63   
        copy_with_slicing              0.0347   34   
        copy_with_list                 0.0337   33   
        copy_with_dot_copy             0.0263   26   
        copy_with_unpacking            0.0253   25   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0823   100  
        copy_with_copy                 0.0187   23   
        copy_with_slicing              0.015    18   
        copy_with_list                 0.0149   18   
        copy_with_dot_copy             0.0143   17   
        copy_with_unpacking            0.014    17   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0914   100  
        copy_with_copy                 0.0226   25   
        copy_with_list                 0.0224   24   
        copy_with_unpacking            0.022    24   
        copy_with_slicing              0.0218   24   
        copy_with_dot_copy             0.0217   24   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0818   100  
        copy_with_list                 0.0231   28   
        copy_with_slicing              0.0223   27   
        copy_with_unpacking            0.022    27   
        copy_with_copy                 0.0217   26   
        copy_with_dot_copy             0.021    26   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.0833   100  
        copy_with_unpacking            0.0303   36   
        copy_with_dot_copy             0.0302   36   
        copy_with_list                 0.0293   35   
        copy_with_slicing              0.0293   35   
        copy_with_copy                 0.0292   35   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name                           Secs     %    
        copy_with_list_comprehension   0.1827   100  
        copy_with_list                 0.0483   26   
        copy_with_slicing              0.0447   24   
        copy_with_unpacking            0.0437   24   
        copy_with_copy                 0.0433   24   
        copy_with_dot_copy             0.0433   24   




"""
