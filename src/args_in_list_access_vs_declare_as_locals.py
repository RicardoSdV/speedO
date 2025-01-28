from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

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

auto_tester(segregator='end', print_rounds=False)


"""
Conclusion:
    - 1 usage: Use global
    - 2+ usages: Use default
    
    Caveat: since the default is processed when the file is loaded for the first time, 
    if for some reason file loading times are important, in this case it might be more 
    worth it to use normal local declares, for example a file which contains many utils 
    where most of them wont be used and some will be used sparingly.
    
    Exception: For some reason with 16 usages in python312 using locals declaring is better than defaults.
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.3512   100  
        default_declare_1   0.33     94   
        no_declare_1        0.308    88   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.3854   100  
        no_declare_2        0.3716   96   
        default_declare_2   0.37     96   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.48     100  
        do_declare_4        0.4548   95   
        default_declare_4   0.4416   92   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.6934   100  
        do_declare_8        0.6378   92   
        default_declare_8   0.5772   83   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        1.47     100  
        do_declare_16        0.9884   67   
        default_declare_16   0.9858   67   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.2676   100  
        no_declare_1        0.2459   92   
        default_declare_1   0.2454   92   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.2918   100  
        no_declare_2        0.282    97   
        default_declare_2   0.2657   91   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.3531   100  
        do_declare_4        0.3359   95   
        default_declare_4   0.3129   89   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.5764   100  
        do_declare_8        0.4477   78   
        default_declare_8   0.4272   74   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        0.923    100  
        do_declare_16        0.8925   97   
        default_declare_16   0.7055   76   


    Python310:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.3041   100  
        default_declare_1   0.2804   92   
        no_declare_1        0.2783   92   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.331    100  
        no_declare_2        0.3193   96   
        default_declare_2   0.3049   92   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.4172   100  
        do_declare_4        0.3925   94   
        default_declare_4   0.3521   84   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.651    100  
        do_declare_8        0.5769   89   
        default_declare_8   0.5364   82   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        1.4281   100  
        do_declare_16        1.1741   82   
        default_declare_16   1.1452   80   


    Python312:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_1        0.214    100  
        default_declare_1   0.2077   97   
        no_declare_1        0.1966   92   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare_2        0.2456   100  
        no_declare_2        0.2321   95   
        default_declare_2   0.2277   93   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_4        0.3164   100  
        do_declare_4        0.2989   94   
        default_declare_4   0.2807   89   
        
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        no_declare_8        0.5313   100  
        do_declare_8        0.3854   73   
        default_declare_8   0.3709   70   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        no_declare_16        0.8013   100  
        default_declare_16   0.6002   75   
        do_declare_16        0.5957   74   
"""
