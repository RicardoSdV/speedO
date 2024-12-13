from itertools import repeat

from src.z_data import data
from src.z_tester import autoTester

num = data.M10

_global = 1

def _no_declare1():
    used = _global

def _no_declare2():
    used1 = _global
    used2 = _global

def _no_declare4():
    used1 = _global
    used2 = _global
    used3 = _global
    used4 = _global

def _no_declare8():
    used1 = _global
    used2 = _global
    used3 = _global
    used4 = _global
    used5 = _global
    used6 = _global
    used7 = _global
    used8 = _global

def _no_declare16():
    used1 = _global
    used2 = _global
    used3 = _global
    used4 = _global
    used5 = _global
    used6 = _global
    used7 = _global
    used8 = _global
    used9 = _global
    used10 = _global
    used11 = _global
    used12 = _global
    used13 = _global
    used14 = _global
    used15 = _global
    used16 = _global


def _do_declare1():
    _local = _global
    used = _local

def _do_declare2():
    _local = _global
    used1 = _local
    used2 = _local

def _do_declare4():
    _local = _global
    used1 = _local
    used2 = _local
    used3 = _local
    used4 = _local

def _do_declare8():
    _local = _global
    used1 = _local
    used2 = _local
    used3 = _local
    used4 = _local
    used5 = _local
    used6 = _local
    used7 = _local
    used8 = _local

def _do_declare16():
    _local = _global
    used1  = _local
    used2  = _local
    used3  = _local
    used4  = _local
    used5  = _local
    used6  = _local
    used7  = _local
    used8  = _local
    used9  = _local
    used10 = _local
    used11 = _local
    used12 = _local
    used13 = _local
    used14 = _local
    used15 = _local
    used16 = _local


def _default_declare1(_local=_global):
    used = _local

def _default_declare2(_local=_global):
    used1 = _local
    used2 = _local

def _default_declare4(_local=_global):
    used1 = _local
    used2 = _local
    used3 = _local
    used4 = _local

def _default_declare8(_local=_global):
    used1 = _local
    used2 = _local
    used3 = _local
    used4 = _local
    used5 = _local
    used6 = _local
    used7 = _local
    used8 = _local

def _default_declare16(_local=_global):
    used1  = _local
    used2  = _local
    used3  = _local
    used4  = _local
    used5  = _local
    used6  = _local
    used7  = _local
    used8  = _local
    used9  = _local
    used10 = _local
    used11 = _local
    used12 = _local
    used13 = _local
    used14 = _local
    used15 = _local
    used16 = _local


def no_declare_1():
    _callable = _no_declare1
    for _ in repeat(None, num):
        _callable()

def no_declare_2():
    _callable = _no_declare2
    for _ in repeat(None, num):
        _callable()

def no_declare_4():
    _callable = _no_declare4
    for _ in repeat(None, num):
        _callable()

def no_declare_8():
    _callable = _no_declare8
    for _ in repeat(None, num):
        _callable()

def no_declare_16():
    _callable = _no_declare16
    for _ in repeat(None, num):
        _callable()


def do_declare_1():
    _callable = _do_declare1
    for _ in repeat(None, num):
        _callable()

def do_declare_2():
    _callable = _do_declare2
    for _ in repeat(None, num):
        _callable()

def do_declare_4():
    _callable = _do_declare4
    for _ in repeat(None, num):
        _callable()

def do_declare_8():
    _callable = _do_declare8
    for _ in repeat(None, num):
        _callable()

def do_declare_16():
    _callable = _do_declare16
    for _ in repeat(None, num):
        _callable()


def default_declare_1():
    _callable = _default_declare1
    for _ in repeat(None, num):
        _callable()

def default_declare_2():
    _callable = _default_declare2
    for _ in repeat(None, num):
        _callable()

def default_declare_4():
    _callable = _default_declare4
    for _ in repeat(None, num):
        _callable()

def default_declare_8():
    _callable = _default_declare8
    for _ in repeat(None, num):
        _callable()

def default_declare_16():
    _callable = _default_declare16
    for _ in repeat(None, num):
        _callable()

autoTester(segregator='end', print_rounds=False)


"""
Conclusion:
    - 1 usage: Use global
    - 2+ usages: Use default
    
    Caveat: since the default is processed when the file is loaded for the first time, 
    if for some reason file loading times are important, in this case it might be more 
    worth it to use normal local declares, for example a file which contains many utils 
    where most of them wont be used and some will be used sparingly.
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.355    100  
        default_declare_1   0.334    94   
        no_declare_1        0.3112   88   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.7056   100  
        do_declare_8        0.636    90   
        default_declare_8   0.5784   82   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.3856   100  
        no_declare_2        0.3746   97   
        default_declare_2   0.3684   96   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.4814   100  
        do_declare_4        0.4552   95   
        default_declare_4   0.4434   92   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        1.2472   100  
        do_declare_16        0.8712   70   
        default_declare_16   0.8648   69   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.2678   100  
        no_declare_1        0.2444   91   
        default_declare_1   0.2435   91   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.2908   100  
        no_declare_2        0.2826   97   
        default_declare_2   0.2656   91   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.3579   100  
        do_declare_4        0.3375   94   
        default_declare_4   0.3166   88   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.5806   100  
        do_declare_8        0.4502   78   
        default_declare_8   0.4276   74   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        0.9265   100  
        do_declare_16        0.713    77   
        default_declare_16   0.706    76   

    Python310:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.313    100  
        default_declare_1   0.2923   93   
        no_declare_1        0.2863   91   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.342    100  
        no_declare_2        0.32     94   
        default_declare_2   0.3181   93   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.4186   100  
        do_declare_4        0.3949   94   
        default_declare_4   0.3724   89   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.6514   100  
        do_declare_8        0.582    89   
        default_declare_8   0.534    82   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        0.9858   100  
        do_declare_16        0.8176   83   
        default_declare_16   0.7751   79   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.2148   100  
        default_declare_1   0.2045   95   
        no_declare_1        0.1964   91   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.2481   100  
        no_declare_2        0.2297   93   
        default_declare_2   0.2297   93   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.3159   100  
        do_declare_4        0.3013   95   
        default_declare_4   0.2815   89   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.5146   100  
        do_declare_8        0.3867   75   
        default_declare_8   0.3722   72   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        0.8023   100  
        default_declare_16   0.6064   76   
        do_declare_16        0.6013   75   

"""
