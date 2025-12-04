from itertools import repeat
from os.path import join

from src.z_data import data
from src.z_tester import auto_tester

num = data.k10
path = join('bin', 'save_to_open_file.log')

def with_open():
    for _ in repeat(None, num):
        with open(path, 'r'):
            continue


def try_finally():
    for _ in repeat(None, num):
        f = None
        try:
            f = open(path, 'r')
        finally:
            if f:
                f.close()


auto_tester()


"""
Conclusion:
    Yeah, just use a with block, I imagine it would be faster to open and close 
    with out the try finally block but, I suspect the main slowdown here is whatever 
    open() is doing because try catch blocks are cheap and it can only do 10k 
    reps in under a second which is mad slow.

    Python27:
        Name          Secs     %    
        with_open     0.144    100  
        try_finally   0.1436   100  
        
    Python38:
        Name          Secs     %    
        with_open     0.1803   100  
        try_finally   0.1793   99   
        
    Python310:
        Name          Secs     %    
        with_open     0.1698   100  
        try_finally   0.1695   100  
        
    Python312:
        Name          Secs     %    
        with_open     0.1913   100  
        try_finally   0.1909   100  
"""

