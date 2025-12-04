""" So I want this for bin flags, so theres no point in going very high with the squares """
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

smallNum = data.ten
bigNum = data.k100
numPowers = 15

# Max size of python int is 32 bits signed int.

def use_cached_precompute():
    for _ in repeat(None, bigNum):
        TWO_POWERS = [2 ** i for i in range(numPowers)]
        for _ in repeat(None, smallNum):
            for el in TWO_POWERS:
                continue


def use_cached_injected():
    TWO_POWERS = [2 ** i for i in range(numPowers)]
    for _ in repeat(None, bigNum):
        for _ in repeat(None, smallNum):
            for el in TWO_POWERS:
                continue


def use_compute():
    for _ in repeat(None, bigNum):
        for _ in repeat(None, smallNum):
            pow2 = 1
            for _ in repeat(None, numPowers -1):
                pow2 *= 2



auto_tester()


"""
Conclusion:

So, in this simple example, when you only need to iterate over the powers of two 10 times 
it is definitely worth it to cache the values, specially if you can inject the values instead
of computing them.

When num powers is 31
    Python27:
        Name                    Secs     %    
        use_compute             0.5976   100  
        use_cached_precompute   0.2804   47   
        use_cached_injected     0.1842   31   
        
    Python38:
        Name                    Secs     %    
        use_compute             0.5724   100  
        use_cached_precompute   0.5262   92   
        use_cached_injected     0.1432   25  
        
    Python310:
        Name                    Secs     %    
        use_cached_precompute   0.6822   100  
        use_compute             0.6128   90   
        use_cached_injected     0.1554   23   
        
    Python312:
        Name                    Secs     %    
        use_compute             0.4868   100  
        use_cached_precompute   0.2976   61   
        use_cached_injected     0.1773   36 
        
When num powers is 15
    Python27:
        Name                    Secs     %    
        use_compute             0.334    100  
        use_cached_precompute   0.162    49   
        use_cached_injected     0.0982   28   
    
    Python38:
        Name                    Secs     %    
        use_compute             0.2903   100  
        use_cached_precompute   0.2671   92   
        use_cached_injected     0.0795   27  
        
    Python310:
        Name                    Secs     %    
        use_compute             0.3248   100  
        use_cached_precompute   0.3123   96   
        use_cached_injected     0.0864   27 
        
    Python312:
        Name                    Secs     %    
        use_compute             0.2506   100  
        use_cached_precompute   0.1552   62   
        use_cached_injected     0.1037   41   
"""



