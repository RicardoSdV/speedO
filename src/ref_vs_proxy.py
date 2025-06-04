import weakref
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester


num = data.M10

class _Class(object): __slots__ = ('attr', '__weakref__')
_obj = _Class()
_obj.attr = 1


_ref = weakref.ref(_obj)
_proxy = weakref.proxy(_obj)

def call_ref(ref = _ref):
    for _ in repeat(None, num):
        ref().attr

def call_proxy(proxy = _proxy):
    for _ in repeat(None, num):
        proxy.attr

def call_obj(obj=_obj):
    for _ in repeat(None, num):
        obj.attr


def safe_ref(ref = _ref):
    for _ in repeat(None, num):
        obj = ref()
        if obj is not None:
            obj.attr

def safe_proxy(proxy = _proxy):
    for _ in repeat(None, num):
        try:
            proxy.attr
        except:
            pass

auto_tester(segregator='start')


"""
Conclusion:
Proxies not half bad, in all versions except 312 they are faster than references,
even when checking for existence of the object. The only exception there probably is to this
is when a significant % of the time the object has been destroyed, the it probably is 
better to just use ref.

Python27:
    Name         Secs     %    
    call_ref     0.3124   100  
    call_proxy   0.1896   61   
    call_obj     0.165    53   
    
    Name         Secs     %    
    safe_ref     0.405    100  
    safe_proxy   0.2452   61   
    
Python38:
    Name         Secs     %    
    call_ref     0.2174   100  
    call_proxy   0.1407   65   
    call_obj     0.1099   51   
    
    Name         Secs     %    
    safe_ref     0.2799   100  
    safe_proxy   0.1552   55   
    
Python310:
    Name         Secs     %    
    call_ref     0.2438   100  
    call_proxy   0.165    68   
    call_obj     0.1349   55   
    
    Name         Secs     %    
    safe_ref     0.3148   100  
    safe_proxy   0.2093   66   

Python312:
    Name         Secs     %    
    call_proxy   0.1649   100  
    call_ref     0.15     91   
    call_obj     0.0763   46   
    
    Name         Secs     %    
    safe_ref     0.2234   100  
    safe_proxy   0.1768   79   

"""


