from itertools import chain

from src.z_data import data
from src.z_tester import auto_tester_2d

def use_concat(outer):
    lastInner = outer.pop()
    for inner in outer:
        for el in inner + lastInner:
            continue
        lastInner = inner

def use_chain(outer, chain=chain):
    lastInner = outer.pop()
    for inner in outer:
        for el in chain(inner, lastInner):
            continue
        lastInner = inner

def use_extend(outer):
    lastInner = outer.pop()
    for inner in outer:
        lastInner.extend(inner)
        for el in lastInner:
            continue
        lastInner = inner

def use_nested_for(outer):
    lastInner = outer.pop()
    for inner in outer:
        for _list in (inner, lastInner):
            for el in _list:
                continue
        lastInner = inner


auto_tester_2d(list_3d=data.faster_3d_list_names, make_new=True)

"""
Conclusion:
- The makeNew is kind of broken, test must be redone when im sure its working well,
but, for 27, as expected nested for loops is fastest. Otherwise concat for small
lists, and chain for longer lists. 

Python27:
    Average of 3 rounds, len(outer) = 11, len(inner) = 1:  
    Name             Secs     %    
    use_chain        0.2133   100  
    use_extend       0.209    98   
    use_nested_for   0.181    85   
    use_concat       0.1797   84   
    
    Average of 3 rounds, len(outer) = 14, len(inner) = 1:  
    Name             Secs     %    
    use_chain        0.1243   100  
    use_concat       0.1153   93   
    use_extend       0.114    92   
    use_nested_for   0.093    75   
    
    Average of 3 rounds, len(outer) = 11, len(inner) = 1:  
    Name             Secs     %    
    use_extend       0.125    100  
    use_concat       0.1153   92   
    use_chain        0.1123   90   
    use_nested_for   0.0823   66   
    
    Average of 3 rounds, len(outer) = 11, len(inner) = 1:  
    Name             Secs     %    
    use_concat       0.1297   100  
    use_extend       0.126    97   
    use_chain        0.1083   84   
    use_nested_for   0.0797   61   
    
    Average of 3 rounds, len(outer) = 14, len(inner) = 1:  
    Name             Secs     %    
    use_concat       0.1403   100  
    use_extend       0.1203   86   
    use_chain        0.1073   76   
    use_nested_for   0.0817   57   
    
    Average of 3 rounds, len(outer) = 11, len(inner) = 1:  
    Name             Secs     %    
    use_concat       0.152    100  
    use_extend       0.1093   72   
    use_chain        0.0983   65   
    use_nested_for   0.078    51   

"""

