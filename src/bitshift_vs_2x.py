from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M100

def bit_shift():
    for _ in repeat(None, num):
        sixteen = 8 << 1

def mult_by_two():
    for _ in repeat(None, num):
        sixteen = 8 * 2

tester(
    (
        bit_shift,
        mult_by_two,
    )
)

"""
Conclusion:
    - Yes, bit shifting is just as slow :(

    Python27:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        mult_by_two   0.7173   100  
        bit_shift     0.7118   99   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        bit_shift     0.5841   100  
        mult_by_two   0.5832   100  
    
    Python310:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        bit_shift     0.6072   100  
        mult_by_two   0.6053   100  
        
    Python312:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        mult_by_two   0.7173   100  
        bit_shift     0.7118   99   
"""
