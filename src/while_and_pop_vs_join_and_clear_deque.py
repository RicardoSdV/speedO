import sys
from os.path import join

from src.z_data import data
from src.z_tester import auto_tester_2d

_file = None
try:
    _file = open(join('bin', 'while_and_pop_vs_join_and_clear_deque.txt'), 'w')
    _write = _file.write

    def while_and_pop(outer, _):
        for inner in outer:
            lpop = inner.popleft
            while inner:
                _write(str(lpop()))

    if sys.version.startswith('2'):
        def join_and_clear(outer, _):
            joinE = ''.join
            for inner in outer:
                _write(joinE((str(el) for el in inner)))
                inner.clear()
    else:
        def join_and_clear(outer, _):
            joinE = ''.join
            for inner in outer:
                _write(joinE(inner))
                inner.clear()

    auto_tester_2d(data.faster_3d_deque_names, open_file=_file, make_new=True)

finally:
    if _file:
        _file.close()


"""
Conclusion:
Python27:


Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name             Secs     %    
    while_and_pop    0.7956   100  
    join_and_clear   0.2096   26   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name             Secs     %    
    while_and_pop    0.7718   100  
    join_and_clear   0.0199   3    
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name             Secs     %    
    while_and_pop    0.7938   100  
    join_and_clear   0.0018   0    
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name             Secs     %    
    while_and_pop    0.8229   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name             Secs     %    
    while_and_pop    0.8386   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name             Secs     %    
    while_and_pop    0.8614   100  
    join_and_clear   0.0      0    

Python310:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name             Secs     %    
    while_and_pop    0.7028   100  
    join_and_clear   0.2143   30   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name             Secs     %    
    while_and_pop    0.6747   100  
    join_and_clear   0.0203   3    
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name             Secs     %    
    while_and_pop    0.704    100  
    join_and_clear   0.0022   0    
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name             Secs     %    
    while_and_pop    0.7206   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name             Secs     %    
    while_and_pop    0.7336   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name             Secs     %    
    while_and_pop    0.7525   100  
    join_and_clear   0.0      0    
    
    
Python312:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name             Secs     %    
    while_and_pop    0.5419   100  
    join_and_clear   0.1798   33   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name             Secs     %    
    while_and_pop    0.5147   100  
    join_and_clear   0.0176   3    
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name             Secs     %    
    while_and_pop    0.5438   100  
    join_and_clear   0.0015   0    
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name             Secs     %    
    while_and_pop    0.5695   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name             Secs     %    
    while_and_pop    0.5782   100  
    join_and_clear   0.0      0    
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name             Secs     %    
    while_and_pop    0.5958   100  
    join_and_clear   0.0      0    
"""


