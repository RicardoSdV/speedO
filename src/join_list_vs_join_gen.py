from src.z_data import data
from src.z_tester import auto_tester_2d


def join_list(outer, _join=''.join):
    for inner in outer:
        _join([el for el in inner])

def join_gen(outer, _join=''.join):
    for inner in outer:
        _join((el for el in inner))

auto_tester_2d(list_3d=data.faster_3d_list_of_strings)

"""
Conclusion:
Making a list before joining is faster. Looks like at some number of elements > 1 000 000 it might be faster to use a generator by the trend.

Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name        Secs     %    
    join_gen    0.4833   100  
    join_list   0.2377   49   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name        Secs     %    
    join_gen    0.259    100  
    join_list   0.1577   61   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name        Secs     %    
    join_gen    0.2023   100  
    join_list   0.1247   62   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name        Secs     %    
    join_gen    0.2077   100  
    join_list   0.134    65   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name        Secs     %    
    join_gen    0.2257   100  
    join_list   0.1513   67   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name        Secs    %    
    join_gen    0.325   100  
    join_list   0.259   80   
    
Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name        Secs     %    
    join_gen    0.3204   100  
    join_list   0.1891   59   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name        Secs     %    
    join_gen    0.2252   100  
    join_list   0.1199   53   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name        Secs     %    
    join_gen    0.208    100  
    join_list   0.1164   56   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name        Secs     %    
    join_gen    0.1985   100  
    join_list   0.1134   56   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name        Secs     %    
    join_gen    0.2253   100  
    join_list   0.1381   61   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name        Secs     %    
    join_gen    0.3371   100  
    join_list   0.2582   77   
    
Python314:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name        Secs     %    
    join_gen    0.375    100  
    join_list   0.1602   43   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name        Secs     %    
    join_gen    0.2576   100  
    join_list   0.1469   56   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name        Secs     %    
    join_gen    0.202    100  
    join_list   0.1179   57   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name        Secs     %    
    join_gen    0.1957   100  
    join_list   0.1129   57   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name        Secs     %    
    join_gen    0.2069   100  
    join_list   0.1255   61   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name        Secs     %    
    join_gen    0.3221   100  
    join_list   0.2472   77   
"""
