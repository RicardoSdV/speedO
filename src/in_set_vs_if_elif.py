from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M

def in_set_2(s=set(range(2))):
    for _ in repeat(None, num):
        1 in s

def in_set_4(s=set(range(4))):
    for _ in repeat(None, num):
        3 in s

def in_set_8(s=set(range(8))):
    for _ in repeat(None, num):
        7 in s

def if_elif_2():
    for _ in repeat(None, num):
        1 == 0
        1 == 1

def if_elif_4():
    for _ in repeat(None, num):
        3 == 0
        3 == 1
        3 == 2
        3 == 3

def if_elif_8():
    for _ in repeat(None, num):
        7 == 0
        7 == 1
        7 == 2
        7 == 3
        7 == 4
        7 == 5
        7 == 6
        7 == 7


auto_tester(segregator='end')


"""
Conclusion:
In set better.

Python27:
    Name        Secs     %    
    if_elif_2   0.019    100  
    in_set_2    0.0176   93   
    
    Name        Secs     %    
    if_elif_4   0.033    100  
    in_set_4    0.0176   53   
    
    Name        Secs     %    
    if_elif_8   0.0628   100  
    in_set_8    0.0176   28   
    
Python38:
    Name        Secs     %    
    if_elif_2   0.0183   100  
    in_set_2    0.0123   67   
    
    Name        Secs     %    
    if_elif_4   0.0328   100  
    in_set_4    0.0124   38   
    
    Name        Secs     %    
    if_elif_8   0.0615   100  
    in_set_8    0.0124   20  

Python314:
    Name        Secs     %    
    if_elif_2   0.0173   100  
    in_set_2    0.0102   59   
    
    Name        Secs     %    
    if_elif_4   0.033    100  
    in_set_4    0.0103   31   
    
    Name        Secs     %    
    if_elif_8   0.0627   100  
    in_set_8    0.0102   16   
"""
