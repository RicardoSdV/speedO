""" How much faster is it to call the default implementation of a partial? & can I inherit from partial
without destroying its performance? All of this is to see if I can give names to partials."""

from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

class InHousePartial(object):
    __slots__ = ('__name__', 'handler', 'args', 'kwargs')

    def __init__(self, name, handler, *args, **kwargs):
        self.__name__ = name
        self.handler  = handler
        self.args     = args
        self.kwargs   = kwargs

    def __call__(self):
        self.handler(*(self.args or ()), **(self.kwargs or {}))

class InheritFromPartial(partial):
    __slots__ = ('__name__', )

    def __new__(cls, name, handler, *args, **kwargs):
        self = super(InheritFromPartial, cls).__new__(cls, handler, *args, **kwargs)
        self.__name__ = name
        return self


def func(a, b, c, d, e, f):
    _a, _b, _c, _d, _e, _f = a, b, c, d, e, f

_partial = partial(func, 1, 2, 3, 4, 5, 6)
inherit_from_partial = InheritFromPartial('name', func, 1, 2, 3, 4, 5, 6)
in_house_partial = InHousePartial('name', func, 1, 2, 3, 4, 5, 6)


num = data.M10

def call_partial():
    for _ in repeat(None, num):
        _partial()

def call_inherit_from_partial():
    for _ in repeat(None, num):
        inherit_from_partial()

def call_in_house_partial():
    for _ in repeat(None, num):
        in_house_partial()

tester(
    (
        call_partial,
        call_inherit_from_partial,
        call_in_house_partial,
    ),
)

"""
Conclusion:
    - Yeah, re-implementing a partial is a terrible idea
    
    - Inheriting from partial is pretty much as fast as partial
    (probably as long as you're not messing with the operation of partial)
    
    Python27:
        Name                        Secs     %    
        call_in_house_partial       2.058    100  
        call_partial                0.7916   38   
        call_inherit_from_partial   0.7852   38   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_in_house_partial       1.1048   100  
        call_inherit_from_partial   0.5862   53   
        call_partial                0.5707   52   

    Python310:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_in_house_partial       1.3365   100  
        call_inherit_from_partial   0.6953   52   
        call_partial                0.6601   49   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                        Secs     %    
        call_in_house_partial       1.2485   100  
        call_partial                0.6263   50   
        call_inherit_from_partial   0.6229   50   

"""

