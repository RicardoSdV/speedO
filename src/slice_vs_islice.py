from itertools import islice

from src.z_tester import tester_2d


def _slice(outer):
    half_len_inner = len(outer[0])//2
    for inner in outer:
        for el in inner[half_len_inner:]:
            continue

def _islice(outer):
    half_len_inner = len(outer[0])//2
    for inner in outer:
        for el in islice(inner, half_len_inner):
            continue


tester_2d(
    (_slice, _islice)
)


"""
Conclusion:
    - islice becomes worth it at about 1000 elements, although some tests 
    need to be done on how the size of the slice affects this.

    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name      Secs     %    
        _islice   0.1087   100  
        _slice    0.0957   88   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name      Secs     %    
        _islice   0.0377   100  
        _slice    0.0367   97   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name      Secs    %    
        _slice    0.034   100  
        _islice   0.031   91   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name      Secs     %    
        _slice    0.0307   100  
        _islice   0.0293   96   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name      Secs     %    
        _slice    0.0317   100  
        _islice   0.0277   87   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name      Secs    %    
        _slice    0.041   100  
        _islice   0.028   68   
        
    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name      Secs     %    
        _islice   0.0877   100  
        _slice    0.0698   80   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name      Secs     %    
        _islice   0.0359   100  
        _slice    0.0288   80   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name      Secs     %    
        _slice    0.0331   100  
        _islice   0.0268   81   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name      Secs     %    
        _slice    0.0283   100  
        _islice   0.0251   89   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name      Secs     %    
        _slice    0.0289   100  
        _islice   0.0257   89   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name      Secs     %    
        _slice    0.0384   100  
        _islice   0.025    65   
        
    Python310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name      Secs     %    
        _islice   0.0926   100  
        _slice    0.0753   81   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name      Secs     %    
        _islice   0.0391   100  
        _slice    0.0342   87   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name      Secs     %    
        _slice    0.0345   100  
        _islice   0.0335   97   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name      Secs     %    
        _slice    0.036    100  
        _islice   0.0351   98   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name      Secs     %    
        _slice    0.0352   100  
        _islice   0.032    91   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name      Secs     %    
        _slice    0.0437   100  
        _islice   0.033    76   
        
    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        
        Name      Secs     %    
        _islice   0.0882   100  
        _slice    0.0716   81   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        
        Name      Secs     %    
        _islice   0.0369   100  
        _slice    0.0333   90   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        
        Name      Secs     %    
        _slice    0.033    100  
        _islice   0.0308   93   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        
        Name      Secs     %    
        _slice    0.0321   100  
        _islice   0.0277   86   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        
        Name      Secs     %    
        _slice    0.0325   100  
        _islice   0.0275   85   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        
        Name      Secs     %    
        _slice    0.0432   100  
        _islice   0.0279   65   
"""

