from src.z_tester import auto_tester_2d


def add_to_set(outer):
    for inner in outer:
        _set = set(); add = _set.add
        for el in inner:
            add(el)

def append_and_cast(outer):
    for inner in outer:
        _list = []; append = _list.append
        for el in inner:
            append(el)
        _set = set(_list)

auto_tester_2d()

"""
Conclusion:
Add to set is faster

Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name              Secs     %    
    append_and_cast   0.505    100  
    add_to_set        0.3353   66   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name              Secs     %    
    append_and_cast   0.3277   100  
    add_to_set        0.237    72   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name              Secs     %    
    append_and_cast   0.2533   100  
    add_to_set        0.1993   79   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name              Secs     %    
    add_to_set        0.3213   100  
    append_and_cast   0.3103   97   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name              Secs     %    
    append_and_cast   0.3317   100  
    add_to_set        0.294    89   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name              Secs    %    
    append_and_cast   0.446   100  
    add_to_set        0.29    65   
    
Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name              Secs     %    
    append_and_cast   0.2967   100  
    add_to_set        0.2249   76   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name              Secs     %    
    append_and_cast   0.2396   100  
    add_to_set        0.1754   73   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name              Secs     %    
    append_and_cast   0.2011   100  
    add_to_set        0.1516   75   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name              Secs     %    
    append_and_cast   0.2055   100  
    add_to_set        0.1551   75   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name              Secs     %    
    append_and_cast   0.3412   100  
    add_to_set        0.2975   87   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name              Secs     %    
    append_and_cast   0.5254   100  
    add_to_set        0.3458   66   
    
Python314:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name              Secs     %    
    append_and_cast   0.2919   100  
    add_to_set        0.2144   73   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name              Secs     %    
    append_and_cast   0.2566   100  
    add_to_set        0.1687   66   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name              Secs     %    
    append_and_cast   0.2039   100  
    add_to_set        0.1524   75   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name              Secs     %    
    append_and_cast   0.2069   100  
    add_to_set        0.1546   75   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name              Secs     %    
    append_and_cast   0.3409   100  
    add_to_set        0.3002   88   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name              Secs     %    
    append_and_cast   0.5157   100  
    add_to_set        0.3439   67   
"""
