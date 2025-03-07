import sys

from src.z_data import data
from src.z_tester import tester_2d


num = data.M10

if sys.version.startswith('2'):
    def iter_values(outer):
        for inner in outer:
            for v in inner.itervalues():
                continue
else:
    def iter_values(outer):
        for inner in outer:
            for v in inner.values():
                continue


def iter_list(outer):
    for inner in outer:
        for v in inner:
            continue

tester_2d(
    (
        iter_values,
        iter_list,
    ),
    list_3d=(
        data.faster_3d_list_of_dicts,
        data.faster_3d_list,
    )
)

"""
Conclusion:
    Python27:
        - Iterating over a list is always faster
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name          Secs     %    
        iter_values   0.0997   100  
        iter_list     0.045    45   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name          Secs     %    
        iter_values   0.0657   100  
        iter_list     0.047    72   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name          Secs    %    
        iter_values   0.089   100  
        iter_list     0.045   51   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name          Secs     %    
        iter_values   0.1037   100  
        iter_list     0.0437   42   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name          Secs     %    
        iter_values   0.1263   100  
        iter_list     0.046    36   
        
    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name          Secs     %    
        iter_values   0.0882   100  
        iter_list     0.0534   61   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name          Secs     %    
        iter_values   0.0632   100  
        iter_list     0.0368   57   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name          Secs     %    
        iter_values   0.0505   100  
        iter_list     0.035    69   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name          Secs     %    
        iter_values   0.0494   100  
        iter_list     0.0382   77   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name          Secs     %    
        iter_values   0.0531   100  
        iter_list     0.0374   70   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name          Secs     %    
        iter_values   0.0529   100  
        iter_list     0.0362   68   
        
    Python310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name          Secs     %    
        iter_values   0.0873   100  
        iter_list     0.0599   69   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name          Secs     %    
        iter_values   0.0687   100  
        iter_list     0.0394   56   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name          Secs     %    
        iter_values   0.0522   100  
        iter_list     0.0388   74   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name          Secs     %    
        iter_values   0.0521   100  
        iter_list     0.0376   72   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name          Secs     %    
        iter_values   0.0534   100  
        iter_list     0.0396   74   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name          Secs     %    
        iter_values   0.05     100  
        iter_list     0.0383   77   
        
    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name          Secs     %    
        iter_values   0.0844   100  
        iter_list     0.0586   69   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name          Secs     %    
        iter_values   0.0599   100  
        iter_list     0.0405   68   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name          Secs     %    
        iter_values   0.0551   100  
        iter_list     0.0427   78   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name          Secs     %    
        iter_values   0.0555   100  
        iter_list     0.0436   79   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name          Secs     %    
        iter_values   0.0543   100  
        iter_list     0.0425   78   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name          Secs     %    
        iter_values   0.0544   100  
        iter_list     0.044    81   
"""
