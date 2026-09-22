from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

cnt = data.M

def append_1():
    for _ in repeat(None, cnt):
        l = []
        l.append(1)

def extend_1():
    for _ in repeat(None, cnt):
        l = []
        l.extend((1, ))

def append_2():
    for _ in repeat(None, cnt):
        l = []
        l.append(1)
        l.append(2)

def extend_2():
    for _ in repeat(None, cnt):
        l = []
        l.extend((1, 2))

def append_4():
    for _ in repeat(None, cnt):
        l = []
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

def extend_4():
    for _ in repeat(None, cnt):
        l = []
        l.extend((1, 2, 3, 4))

def append_8():
    for _ in repeat(None, cnt):
        l = []
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        l.append(8)

def extend_8():
    for _ in repeat(None, cnt):
        l = []
        l.extend((1, 2, 3, 4, 5, 6, 7, 8))

auto_tester(segregator='end')

"""
Conclusion:
Extend surprisingly good, or, append surprisingly bad.
Please see: extend_vs_append_to_large_list.py

Python27: 
    Name       Secs     %    
    extend_1   0.0632   100  
    append_1   0.0616   97   
    
    Name       Secs     %    
    append_2   0.0796   100  
    extend_2   0.0638   80   
    
    Name       Secs     %    
    append_4   0.1216   100  
    extend_4   0.062    51   
    
    Name       Secs     %    
    append_8   0.238    100  
    extend_8   0.0664   28   

Python38:
    Name       Secs     %    
    extend_1   0.0294   100  
    append_1   0.0268   91   
    
    Name       Secs     %    
    append_2   0.0414   100  
    extend_2   0.0311   75   
    
    Name       Secs     %    
    append_4   0.069    100  
    extend_4   0.0307   45   
    
    Name       Secs     %    
    append_8   0.1307   100  
    extend_8   0.0363   28   

Python310:
    Name       Secs     %    
    extend_1   0.0316   100  
    append_1   0.0296   94   
    
    Name       Secs     %    
    append_2   0.0452   100  
    extend_2   0.0321   71   
    
    Name       Secs     %    
    append_4   0.0753   100  
    extend_4   0.0328   44   
    
    Name       Secs     %    
    append_8   0.1469   100  
    extend_8   0.0377   26   

Python312:
    Name       Secs     %    
    extend_1   0.0263   100  
    append_1   0.0238   90   
    
    Name       Secs     %    
    append_2   0.0305   100  
    extend_2   0.0253   83   
    
    Name       Secs     %    
    append_4   0.0449   100  
    extend_4   0.0303   68   
    
    Name       Secs     %    
    append_8   0.0821   100  
    extend_8   0.0282   34   
    
Python314:
    Name       Secs     %    
    extend_1   0.0267   100  
    append_1   0.0232   87   
    
    Name       Secs     %    
    extend_2   0.0308   100  
    append_2   0.0304   99   
    
    Name       Secs     %    
    append_4   0.0426   100  
    extend_4   0.0298   70   
    
    Name       Secs     %    
    append_8   0.0792   100  
    extend_8   0.0324   41   
"""
