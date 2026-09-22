from array import array
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester
from src.zz_import import clock

num = data.M10


def append_to_list(_clock=clock):
    _list = []
    for _ in repeat(None, num):
        _list.append(_clock())

def append_to_array(_clock=clock):
    _array = array('d')
    for _ in repeat(None, num):
        _array.append(_clock())

def predef_append_to_list(_clock=clock):
    _list = []
    app = _list.append
    for _ in repeat(None, num):
        app(_clock())

def predef_append_to_array(_clock=clock):
    _array = array('d')
    app = _array.append
    for _ in repeat(None, num):
        app(_clock())


auto_tester()

"""
Python27:
    Name                     Secs     %    
    append_to_array          0.9862   100  
    predef_append_to_array   0.8416   85   
    append_to_list           0.5898   60   
    predef_append_to_list    0.5138   52
    
Python38:
    Name                     Secs     %    
    append_to_array          0.7873   100  
    predef_append_to_array   0.7356   93   
    append_to_list           0.6469   82   
    predef_append_to_list    0.5867   75   
    
Python310:
    Name                     Secs     %    
    append_to_array          0.8104   100  
    predef_append_to_array   0.7591   94   
    append_to_list           0.6455   80   
    predef_append_to_list    0.6075   75 
    
Python312:
    Name                     Secs     %    
    predef_append_to_array   0.7883   100  
    append_to_array          0.7748   98   
    predef_append_to_list    0.6575   83   
    append_to_list           0.6269   80  
    
Python314:
    Name                     Secs     %    
    append_to_array          0.7768   100  
    predef_append_to_array   0.7602   98   
    append_to_list           0.5677   73   
    predef_append_to_list    0.5646   73
    
"""

