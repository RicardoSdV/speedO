from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Class(object):
    __slots__ = ('__priv_attr', 'pub_attr')
    cls_attr = 3

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

def call_cls_attr():
    _obj = obj
    for _ in repeat(None, num):
        _local = _obj.cls_attr


tester(
    (
        call_prop,
        call_getter,
        call_pub_attr,
        call_cls_attr,
    )
)

"""
Conclusion:
    - In python27 using properties is SLOW
    - In python38-310 same as calling a method, but public atts way faster still
    - In python312 properties actually faster than methods, but public atts faster

    Python27:
        - 5x for switching from prop to cls attr
        
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       7.1558   100  
        call_getter     4.7414   66   
        call_pub_attr   1.5432   22   
        call_cls_attr   1.256    18   
        
    Python38:
        - 3x for switching from prop to cls attr
    
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       3.2407   100  
        call_getter     3.2076   99   
        call_pub_attr   1.0539   33   
        call_cls_attr   0.9838   30   

    Python310:
        - < 3x, > 2x for switching from prop to cls attr 
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_prop       3.4095   100  
        call_getter     3.3398   98   
        call_pub_attr   1.2277   36   
        call_cls_attr   1.2223   36   
        
    Python312:
        - < 3x, > 2x for switching from prop to ins attr 
        Testing times mean of 5 rounds: 
        Name            Secs     %    
        call_getter     2.026    100  
        call_prop       1.9016   94   
        call_cls_attr   1.1123   55   
        call_pub_attr   0.7615   38   

"""

