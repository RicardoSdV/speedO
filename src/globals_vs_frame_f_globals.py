from itertools import repeat
from sys import _getframe

from src.z_data import data
from src.z_tester import auto_tester


num = data.M10

def get_globals():
    for _ in repeat(None, num):
        globals()


def get_f_globals(get_frame=_getframe):
    for _ in repeat(None, num):
        get_frame().f_globals


auto_tester()


"""
Conclusion:
    I was told, globals() uses the frame to get the globals, which is crazy, and might well be true,
    but its still faster to call globals()

    Python27:
        Name            Secs     %    
        get_f_globals   0.3468   100  
        get_globals     0.1916   55   
        
    Python38:
        Name            Secs     %    
        get_f_globals   0.1651   100  
        get_globals     0.1626   98   
        
    Python310:
        Name            Secs     %    
        get_f_globals   0.2154   100  
        get_globals     0.1949   90   
        
    Python312:
        Name            Secs     %    
        get_f_globals   0.1936   100  
        get_globals     0.1353   70   
    
"""

