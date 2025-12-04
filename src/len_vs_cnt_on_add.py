from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = 1
size = data.M10
elements = list(range(size))
zipped_kv_pairs = list(zip(elements, elements))

def len_of_dict(pairs=zipped_kv_pairs, _len=len):
    for _ in repeat(None, num):
        _dict = {}
        for k, v in pairs:
            _dict[k] = v
        l = _len(_dict)

def count_on_add_dict(pairs=zipped_kv_pairs):
    for _ in repeat(None, num):
        _cnt = 0
        _dict = {}
        for k, v in pairs:
            _dict[k] = v
            _cnt += 1

def len_of_list(els=elements, _len=len):
    for _ in repeat(None, num):
        _list = []; app = _list.append
        for el in els:
            app(el)
            l = _len(_list)

def count_on_add_list(els=elements):
    for _ in repeat(None, num):
        _cnt = 0
        _list = []; app = _list.append
        for el in els:
            app(el)
            _cnt += 1

tester(
    (
        len_of_dict,
        count_on_add_dict,
        len_of_list,
        count_on_add_list,
    )
)

"""
Conclusion:
    - surprisingly len of dict is better than len of list, what is not depicted here is that if len() 
    is a global and _cnt a local, _cnt for a list is way better, but theres no excuse not to make len 
    a default arg.
    
    Python27:
        Name                Secs     %    
        count_on_add_dict   0.4934   100  
        len_of_dict         0.4008   81   
        len_of_list         0.3658   74   
        count_on_add_list   0.3494   71

    Python38:
        Name                Secs     %    
        count_on_add_dict   0.4559   100  
        len_of_dict         0.3549   78   
        len_of_list         0.3503   77   
        count_on_add_list   0.3372   74  
    
    Python310:
        Name                Secs     %    
        count_on_add_dict   0.5494   100  
        len_of_dict         0.4187   76   
        len_of_list         0.3947   72   
        count_on_add_list   0.3784   69  
    
    Python312:
        Name                Secs     %    
        count_on_add_dict   0.443    100  
        len_of_list         0.3776   85   
        count_on_add_list   0.3544   80   
        len_of_dict         0.3504   79   
        
    Python314:
        Name                Secs     %    
        count_on_add_dict   0.4692   100  
        len_of_dict         0.3852   82   
        len_of_list         0.3429   73   
        count_on_add_list   0.3362   72   

"""

