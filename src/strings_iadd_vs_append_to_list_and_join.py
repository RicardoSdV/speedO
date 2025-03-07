from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M

ten_strs = ['a'] * 10
hun_strs = ['a'] * 100

def iadd_to_str_ten(strs=ten_strs):
    for _ in repeat(None, num):
        res = ''
        for str in strs:
            res += str

def iadd_to_str_hun(strs=hun_strs):
    for _ in repeat(None, num // 10):
        res = ''
        for str in strs:
            res += str


def append_and_join_ten(strs=ten_strs):
    for _ in repeat(None, num):
        res = []
        app = res.append
        for str in strs:
            app(str)
        ''.join(res)

def append_and_join_hun(strs=hun_strs):
    for _ in repeat(None, num // 10):
        res = []
        app = res.append
        for str in strs:
            app(str)
        ''.join(res)

auto_tester(segregator='end')

"""
Conclusion:
    iadd is faster
    
    Python27:
        Name                  Secs     %    
        append_and_join_hun   0.2174   100  
        iadd_to_str_hun       0.1828   84   
        
        Name                  Secs     %    
        append_and_join_ten   0.3518   100  
        iadd_to_str_ten       0.2132   61   
        
    Python38:
        Name                  Secs     %    
        iadd_to_str_hun       0.2024   100  
        append_and_join_hun   0.1818   90   
        
        Name                  Secs     %    
        append_and_join_ten   0.2479   100  
        iadd_to_str_ten       0.2211   89   
        
    Python310:
        Name                  Secs     %    
        append_and_join_hun   0.2957   100  
        iadd_to_str_hun       0.2277   77   
        
        Name                  Secs     %    
        append_and_join_ten   0.2728   100  
        iadd_to_str_ten       0.2481   91   
        
    Python312:
        Name                  Secs     %    
        append_and_join_hun   0.2648   100  
        iadd_to_str_hun       0.1866   70   
        
        Name                  Secs     %    
        append_and_join_ten   0.262    100  
        iadd_to_str_ten       0.2085   80   
"""
