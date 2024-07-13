"""
How much slower is popping back than popping front?
"""
from src.z_data import data
from z_tester import tester_2d


def pop_front(outer):
    for inner in outer:
        inner.pop(0)


def pop_back(outer):
    for inner in outer:
        inner.pop()


tester_2d(
    (
        pop_front,
        pop_back,
    ),
    list_3d=data.slower_3d_list
)

"""
Conclusion:
    - Must take into account that popping is a relatively fast operation so all the peripherals of the
    testing drive the numbers up quite a bit, so even though popping front doesnt seem that bad an idea
    for short lists it is an undefined amount worse than it seems.
    
    - Also, at about 10k elements it stops making sense to pop front, even, occasionally, also, if ur 
    popping front from a 10M long list, wtf?
    
    Python312:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name        Time     %    
        pop_front   0.2158   100  
        pop_back    0.1722   80   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name        Time     %    
        pop_front   0.0762   100  
        pop_back    0.0294   39   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name        Time     %    
        pop_front   0.0502   100  
        pop_back    0.0218   43   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name        Time     %    
        pop_front   0.1686   100  
        pop_back    0.0023   1    
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name        Time     %    
        pop_front   0.1819   100  
        pop_back    0.0008   0    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name        Time     %    
        pop_front   0.0583   100  
        pop_back    0.0      0    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name        Time     %    
        pop_front   0.0603   100  
        pop_back    0.0      0    
        
    
    Python38:
        - Everything slightly faster, but pattern remains
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name        Time     %    
        pop_front   0.3159   100  
        pop_back    0.2034   64   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name        Time     %    
        pop_front   0.0899   100  
        pop_back    0.0408   45   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name        Time     %    
        pop_front   0.052    100  
        pop_back    0.0197   38   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name        Time     %    
        pop_front   0.17     100  
        pop_back    0.0027   2    
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name        Time     %    
        pop_front   0.1699   100  
        pop_back    0.0003   0    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name        Time     %    
        pop_front   0.0595   100  
        pop_back    0.0      0    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name        Time     %    
        pop_front   0.0591   100  
        pop_back    0.0      0    
    
    
    Python27:
        - For short lists its not that bad.
    
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name        Time     %    
        pop_front   1.1173   100  
        pop_back    0.6507   57   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name        Time     %    
        pop_front   0.1197   100  
        pop_back    0.0523   44   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name        Time     %    
        pop_front   0.0727   100  
        pop_back    0.023    32   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name        Time     %    
        pop_front   0.0557   100  
        pop_back    0.0037   7    
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name        Time     %    
        pop_front   0.0537   100  
        pop_back    0.0003   1    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name        Time    %    
        pop_front   0.054   100  
        pop_back    0.0     0    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name        Time     %    
        pop_front   0.0533   100  
        pop_back    0.0      0  

"""

