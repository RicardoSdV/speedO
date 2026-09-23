"""
We know that list comprehension is faster than appending, and we know using
for and break is faster than any() but what if using any() allows you to use
list comprehension? who wins?
"""
from src.z_tester import auto_tester_2d
from src.z_data import data


def any_and_comprehend(outer):
    checkForMembershipHere = outer[0]
    for inner in outer:
        l = [
            el
            for el in inner
            if any(el == member for member in checkForMembershipHere)
        ]

def for_break_and_append(outer):
    checkForMembershipHere = outer[0]
    for inner in outer:
        l = []; lApp = l.append
        for el in inner:
            for member in checkForMembershipHere:
                if el == member:
                    lApp(el)
                    break


auto_tester_2d(list_3d=data.super_fast_3d_list)

"""
Conclusion:
- Im not sure that this is the best test ever but looks like for and break is the way to go.

Python27:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10:  
    Name                   Secs     %    
    any_and_comprehend     0.376    100  
    for_break_and_append   0.1057   28   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100:  
    Name                   Secs     %    
    any_and_comprehend     1.366    100  
    for_break_and_append   0.4747   35   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000:  
    Name                   Secs     %    
    any_and_comprehend     11.133   100  
    for_break_and_append   4.2557   38   

Python38:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10: 
    Name                   Secs     %    
    any_and_comprehend     0.2772   100  
    for_break_and_append   0.0884   32   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100: 
    Name                   Secs     %    
    any_and_comprehend     1.1879   100  
    for_break_and_append   0.555    47   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000: 
    Name                   Secs     %    
    any_and_comprehend     9.9394   100  
    for_break_and_append   4.8531   49   

Python314:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10: 
    Name                   Secs     %    
    any_and_comprehend     0.2483   100  
    for_break_and_append   0.0822   33   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100: 
    Name                   Secs     %    
    any_and_comprehend     1.0248   100  
    for_break_and_append   0.5132   50   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000: 
    Name                   Secs     %    
    any_and_comprehend     9.4565   100  
    for_break_and_append   5.0568   53   
"""
