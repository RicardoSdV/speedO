""" if you need to extend a list & have the choice what is fastest? """
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M
my_range = data.hun_ints

def with_list(r=my_range):
    for _ in repeat(None, num):
        _list = []
        ext = [i for i in r]
        _list.extend(ext)

def with_gen(r=my_range):
    for _ in repeat(None, num):
        _list = []
        ext = (i for i in r)
        _list.extend(ext)

def with_tuple(r=my_range):
    for _ in repeat(None, num):
        _list = []
        ext = tuple((i for i in r))
        _list.extend(ext)

def with_set(r=my_range):
    for _ in repeat(None, num):
        _list = []
        ext = {i for i in r}
        _list.extend(ext)

def with_append(r=my_range):
    for _ in repeat(None, num):
        _list = []
        for i in r:
            _list.append(i)

def with_appendTo(r=my_range):
    for _ in repeat(None, num):
        _list = []
        list_app = _list.append
        for i in r:
            list_app(i)


auto_tester()


"""
Conclusion:
    Python27:
        - For very few elements append, for more extend list with list. 
        r = 1
        Name            Secs     %    
        with_tuple      0.3802   100  
        with_gen        0.3572   94   
        with_set        0.2356   62   
        with_list       0.1162   31   
        with_appendTo   0.0852   22   
        with_append     0.0838   22   
        
        r = 10
        Name            Secs     %    
        with_tuple      0.5286   100  
        with_gen        0.4454   84   
        with_append     0.3964   75   
        with_set        0.3868   73   
        with_appendTo   0.2836   54   
        with_list       0.2696   51   
        
        r = 100
        Name            Secs     %    
        with_append     2.9478   100  
        with_tuple      2.4836   84   
        with_gen        2.3282   79   
        with_set        2.144    73   
        with_appendTo   1.9452   66   
        with_list       1.4528   49   
        
    Python38:
        r = 1
        Name            Secs     %    
        with_tuple      0.3201   100  
        with_gen        0.2792   87   
        with_set        0.2739   86   
        with_append     0.203    63   
        with_list       0.1905   60   
        with_appendTo   0.1705   53   
        
    Python310:
        r = 10
        Name            Secs     %    
        with_tuple      0.3393   100  
        with_set        0.3248   96   
        with_gen        0.313    92   
        with_list       0.2272   67   
        with_append     0.219    65   
        with_appendTo   0.2045   60    
        
    Python312:
        r = 100
        Name            Secs     %    
        with_tuple      0.3271   100  
        with_gen        0.3178   97   
        with_set        0.2241   69   
        with_appendTo   0.209    64   
        with_append     0.1597   49   
        with_list       0.1499   46   

"""

