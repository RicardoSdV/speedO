from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Class(object):
    __slots__ = ('__priv_attr', 'pub_attr')

    def __init__(self):
        self.__priv_attr = 1
        self.pub_attr = 2

    @property
    def prop(self):
        return self.__priv_attr

    def get_attr(self):
        return self.__priv_attr

obj = Class()
num = data.M100

def call_prop():
    _obj = obj
    for _ in repeat(None, num):
        _local = _obj.prop

def call_getter():
    _obj = obj
    for _ in repeat(None, num):
        _local = _obj.get_attr()

def call_pub_attr():
    _obj = obj
    for _ in repeat(None, num):
        _local = _obj.pub_attr


tester(
    (
        call_prop,
        call_getter,
        call_pub_attr,
    )
)

"""
Conclusion:
    - In python27 using properties is SLOW
    - In python38-310 same as calling a method, but public atts way faster still
    - In python312 properties actually faster than methods, which does not mean 
    that public atts still way faster

    Python27:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       6.597    100  
        call_getter     4.3954   67   
        call_pub_attr   1.4526   22   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       3.0681   100  
        call_getter     3.0227   99   
        call_pub_attr   0.9915   32   

    Python310:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       3.1819   100  
        call_getter     3.0715   97   
        call_pub_attr   1.1632   37   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_getter     1.9374   100  
        call_prop       1.7976   93   
        call_pub_attr   0.7235   37  

"""

