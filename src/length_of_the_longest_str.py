from itertools import repeat

from src.z_data import data
from src.z_tester import tester

strs = ('afawefaewf', 'waefa', 'afewagerg', 'argeer', 'erga', 'streh', 'EWFWE', 'EARGA', 'aergsag', 'agreg', 'GWEGGAG', 'GFSDAGA')
many_strs = strs * 10
num, num2 = data.M, data.k100


def len_max():
    for _ in repeat(None, num):
        maxLen = len(max(strs, key=len))

def max_len():
    for _ in repeat(None, num):
        maxLen = max(len(s) for s in strs)

def many_len_max():
    for _ in repeat(None, num2):
        maxLen = len(max(many_strs, key=len))

def many_max_len():
    for _ in repeat(None, num2):
        maxLen = max(len(s) for s in many_strs)


tester(
    (
        len_max,
        max_len,
    )
)

tester(
    (
        many_len_max,
        many_max_len,
    )
)


""" 
Conclusion:
    Max len way to go always, also, this operation way fast in PyPy

    Python27:
        Testing times mean of 5 rounds: 
        Name      Secs     %    
        max_len   0.5128   100  
        len_max   0.3412   67   
        
        Testing times mean of 5 rounds: 
        Name           Secs    %    
        many_max_len   0.408   100  
        many_len_max   0.243   60   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name      Secs     %    
        max_len   0.4214   100  
        len_max   0.2599   62   

        Testing times mean of 5 rounds: 
        Name           Secs     %    
        many_max_len   0.308    100  
        many_len_max   0.1409   46   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name      Secs     %    
        max_len   0.4766   100  
        len_max   0.2392   50   
        
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        many_max_len   0.343    100  
        many_len_max   0.1207   35   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name      Secs     %    
        max_len   0.4169   100  
        len_max   0.2159   52   
        
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        many_max_len   0.2995   100  
        many_len_max   0.1197   40   

    PyPy313:
        Testing times mean of 5 rounds: 
        Name      Secs    %    
        max_len   0.057   100  
        len_max   0.013   23   
        
        Testing times mean of 5 rounds: 
        Name           Secs     %    
        many_max_len   0.0338   100  
        many_len_max   0.0068   20   
"""

