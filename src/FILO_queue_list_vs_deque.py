from collections import deque
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10

# Because list resize at 9, (deque no resize right?)
_list = [1,2,3,4,5,6,7,8,9,10]
_deque = deque(_list)

def use_deque_1(pop=_deque.pop, app=_deque.append, div=1):
    for _ in repeat(None, num // div):
        pop()
        app(10)

def use_list_1(pop=_list.pop, app=_list.append, div=1):
    for _ in repeat(None, num // div):
        pop()
        app(10)


def use_deque_2(pop=_deque.pop, app=_deque.append, div=2):
    for _ in repeat(None, num // div):
        pop()
        pop()
        app(9)
        app(10)

def use_list_2(pop=_list.pop, app=_list.append, div=2):
    for _ in repeat(None, num // div):
        pop()
        pop()
        app(9)
        app(10)


def use_deque_4(pop=_deque.pop, app=_deque.append, div=4):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        app(7)
        app(8)
        app(9)
        app(10)

def use_list_4(pop=_list.pop, app=_list.append, div=4):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        app(7)
        app(8)
        app(9)
        app(10)

def use_deque_8(pop=_deque.pop, app=_deque.append, div=8):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        app(3)
        app(4)
        app(5)
        app(6)
        app(7)
        app(8)
        app(9)
        app(10)

def use_list_8(pop=_list.pop, app=_list.append, div=8):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        app(3)
        app(4)
        app(5)
        app(6)
        app(7)
        app(8)
        app(9)
        app(10)


def use_deque_10(pop=_deque.pop, app=_deque.append, div=10):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        app(1)
        app(2)
        app(3)
        app(4)
        app(5)
        app(6)
        app(7)
        app(8)
        app(9)
        app(10)

def use_list_10(pop=_list.pop, app=_list.append, div=10):
    for _ in repeat(None, num // div):
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        pop()
        app(1)
        app(2)
        app(3)
        app(4)
        app(5)
        app(6)
        app(7)
        app(8)
        app(9)
        app(10)

auto_tester(segregator='end')

"""
The more you advance in python version the more list catches up to deque,
but if you're going to do any significant amount of popping then deque 
is always the way to go, if its some infrequent back popping then use
a list except in python27.

Python27:
    Name          Secs     %    
    use_list_1    0.3594   100  
    use_deque_1   0.21     57   
    
    Name          Secs     %    
    use_list_2    0.3372   100  
    use_deque_2   0.1892   56   
    
    Name          Secs     %    
    use_list_4    0.3426   100  
    use_deque_4   0.1768   52   
    
    Name          Secs     %    
    use_list_8    0.5652   100  
    use_deque_8   0.1816   32   
    
    Name           Secs     %    
    use_list_10    0.609    100  
    use_deque_10   0.1864   31   

Python38:
    Name          Secs     %    
    use_list_1    0.1912   100  
    use_deque_1   0.186    97   
    
    Name          Secs     %    
    use_list_2    0.175    100  
    use_deque_2   0.1721   98   
    
    Name          Secs     %    
    use_list_4    0.1664   100  
    use_deque_4   0.1621   97   
    
    Name          Secs     %    
    use_list_8    0.2135   100  
    use_deque_8   0.157    74   
    
    Name           Secs     %    
    use_list_10    0.4571   100  
    use_deque_10   0.1562   34   

Python310:
    Name          Secs     %    
    use_list_1    0.2219   100  
    use_deque_1   0.2215   100  
    
    Name          Secs     %    
    use_list_2    0.205    100  
    use_deque_2   0.2016   98   
    
    Name          Secs     %    
    use_list_4    0.1954   100  
    use_deque_4   0.19     97   
    
    Name          Secs     %    
    use_list_8    0.2306   100  
    use_deque_8   0.1934   84   
    
    Name           Secs     %    
    use_list_10    0.5148   100  
    use_deque_10   0.2077   40   

Python312:
    Name          Secs     %    
    use_deque_1   0.2073   100  
    use_list_1    0.1938   93   
    
    Name          Secs     %    
    use_deque_2   0.1888   100  
    use_list_2    0.1756   93   
    
    Name          Secs     %    
    use_deque_4   0.1787   100  
    use_list_4    0.1647   92   
    
    Name          Secs     %    
    use_list_8    0.2013   100  
    use_deque_8   0.1746   87   
    
    Name           Secs     %    
    use_list_10    0.2171   100  
    use_deque_10   0.1933   89   

"""

