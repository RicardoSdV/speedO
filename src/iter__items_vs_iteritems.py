from src.z_data import data
from src.z_tester import tester_2d


num = data.M10

def iter_with_items(outer):
    for inner in outer:
        for k, v in inner.items():
            _k, _v = k, v

def iter_with_iteritems(outer):
    for inner in outer:
        for k, v in inner.iteritems():
            _k, _v = k, v

tester_2d(
    (
        iter_with_items,
        iter_with_iteritems
    ),
    list_3d=data.faster_3d_list_of_dicts
)

"""
Conclusion:
    Python27:
        - Iteritems just always better
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 2: 

        Name                  Secs     %    
        iter_with_items       0.117    100  
        iter_with_iteritems   0.0827   71   
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 5: 
        
        Name                  Secs     %    
        iter_with_items       0.18     100  
        iter_with_iteritems   0.1303   72   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 

        Name                  Secs    %    
        iter_with_items       0.347   100  
        iter_with_iteritems   0.255   73   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        
        Name                  Secs     %    
        iter_with_items       0.313    100  
        iter_with_iteritems   0.2333   75   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        
        Name                  Secs     %    
        iter_with_items       0.2687   100  
        iter_with_iteritems   0.2017   75   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        
        Name                  Secs     %    
        iter_with_items       7.5027   100  
        iter_with_iteritems   0.2057   3    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        
        Name                  Secs     %    
        iter_with_items       9.5117   100  
        iter_with_iteritems   0.2437   3    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        
        Name                  Secs     %    
        iter_with_items       7.877    100  
        iter_with_iteritems   0.2823   4    

"""


