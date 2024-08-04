"""
Does making the condition inverse slow down it down? by how much?
When there's an else, because then it can be not inverse
"""
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M100

def _if_no_jump():
    i = 2
    for _ in repeat(None, num):
        if i == 2:
            j = i
        else:
            j = 2

def _if_not_no_jump():
    i = 1
    for _ in repeat(None, num):
        if not i == 2:
            j = i
        else:
            j = 2

def _if_jump():
    i = 2
    for _ in repeat(None, num):
        if i == 1:
            j = i
        else:
            j = 1

def _if_not_jump():
    i = 2
    for _ in repeat(None, num):
        if not i == 2:
            j = i
        else:
            j = 1

tester(
    (
        _if_no_jump,
        _if_not_no_jump,
        _if_jump,
        _if_not_jump,
    )
)

"""
Conclusion:
    - So, theres some variance but the main takeaway is that not has some cost,
    and jumping to the else also has some cost, therefore the most efficient is
    not using the else and not using "not" 

    Python27:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        _if_jump          1.157    100  
        _if_not_no_jump   1.1044   95   
        _if_not_jump      1.0984   95   
        _if_no_jump       1.0916   94   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        _if_not_no_jump   1.1884   100  
        _if_jump          1.1881   100  
        _if_not_jump      1.1543   97   
        _if_no_jump       1.1111   93   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        _if_not_jump      1.4907   100  
        _if_jump          1.4541   98   
        _if_not_no_jump   1.4455   97   
        _if_no_jump       1.3083   88   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        _if_jump          1.3652   100  
        _if_not_jump      1.3525   99   
        _if_not_no_jump   1.2949   95   
        _if_no_jump       1.2436   91   
"""
