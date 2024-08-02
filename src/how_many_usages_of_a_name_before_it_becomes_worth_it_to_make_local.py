from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M
name = 1

def declare_local_1_use():
    for _ in repeat(None, num):
        _name = name
        for _ in repeat(None, 1):
            __name = name

def no_declare_local_1_use():
    for _ in repeat(None, num):
        for _ in repeat(None, 1):
            __name = name


def declare_local_2_use():
    for _ in repeat(None, num):
        _name = name
        for _ in repeat(None, 2):
            __name = _name

def no_declare_local_2_use():
    for _ in repeat(None, num):
        for _ in repeat(None, 2):
            _name = name


def declare_local_4_use():
    for _ in repeat(None, num):
        _name = name
        for _ in repeat(None, 4):
            __name = _name

def no_declare_local_4_use():
    for _ in repeat(None, num):
        for _ in repeat(None, 4):
            _name = name


def declare_local_8_use():
    for _ in repeat(None, num):
        _name = name
        for _ in repeat(None, 8):
            __name = _name

def no_declare_local_8_use():
    for _ in repeat(None, num):
        for _ in repeat(None, 8):
            _name = name


def declare_local_16_use():
    for _ in repeat(None, num):
        _name = name
        for _ in repeat(None, 16):
            __name = _name

def no_declare_local_16_use():
    for _ in repeat(None, num):
        for _ in repeat(None, 16):
            _name = name


tester(
    (
        declare_local_1_use,
        no_declare_local_1_use,
        declare_local_2_use,
        no_declare_local_2_use,
        declare_local_4_use,
        no_declare_local_4_use,
        declare_local_8_use,
        no_declare_local_8_use,
        declare_local_16_use,
        no_declare_local_16_use,
    )
)

"""
Conclusion:
    - Normally becomes worth it at 4 usages
    
    - To be fair memory & deletion speeds are not being measured, im sure there are
    some hidden costs to declaring locals all over the place    
    
    Python27:
        - Becomes worth it at 4 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.2354   100  
        declare_local_16_use      0.2042   87   
        no_declare_local_8_use    0.16     68   
        declare_local_8_use       0.1434   61   
        no_declare_local_4_use    0.1146   49   
        declare_local_4_use       0.1114   47   
        declare_local_2_use       0.0972   41   
        no_declare_local_2_use    0.0962   41   
        declare_local_1_use       0.091    39   
        no_declare_local_1_use    0.086    37   
    
    Python38:
        - Becomes worth it at 2 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.1908   100  
        declare_local_16_use      0.162    85   
        no_declare_local_8_use    0.1236   65   
        declare_local_8_use       0.1091   56   
        no_declare_local_4_use    0.0863   45   
        declare_local_4_use       0.0844   44   
        no_declare_local_2_use    0.0717   38   
        declare_local_2_use       0.0707   37   
        declare_local_1_use       0.0651   34   
        no_declare_local_1_use    0.0617   32   
    
    Python310:
        - Becomes worth it at 2 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.243    100  
        declare_local_16_use      0.1776   73   
        no_declare_local_8_use    0.1484   61   
        declare_local_8_use       0.1225   50   
        no_declare_local_4_use    0.0986   41   
        declare_local_4_use       0.0899   37   
        no_declare_local_2_use    0.0777   32   
        declare_local_2_use       0.0735   30   
        declare_local_1_use       0.0712   28   
        no_declare_local_1_use    0.0644   26   
    
    Python312:
        - Becomes worth it at 4 usages
    
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.1894   100  
        declare_local_16_use      0.1622   86   
        no_declare_local_8_use    0.1209   64   
        declare_local_8_use       0.1099   57   
        no_declare_local_4_use    0.0877   46   
        declare_local_4_use       0.0835   44   
        no_declare_local_2_use    0.0717   38   
        declare_local_2_use       0.0711   38   
        declare_local_1_use       0.0659   35   
        no_declare_local_1_use    0.0624   33   
"""

