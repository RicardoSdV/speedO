"""
How much slower is it to declare a class that inherits from partial or even an in-house partial
than the real thing??
"""

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

num = data.k100

def declare_partial():
    result = [
        partial(func, 1, 2, 3, 4, 5, 6)
        for _ in repeat(None, num)
    ]

def declare_inherits_from_partial():
    result = [
        InheritFromPartial('name', func, 1, 2, 3, 4, 5, 6)
        for _ in repeat(None, num)
    ]

def declare_in_house_partial():
    result = [
        InHousePartial('name', func, 1, 2, 3, 4, 5, 6)
        for _ in repeat(None, num)
    ]

if __name__ == '__main__':
    tester(
        (
            declare_partial,
            declare_inherits_from_partial,
            declare_in_house_partial,
        ),
    )

    tester(
        (
            declare_partial,
            declare_inherits_from_partial,
            declare_in_house_partial,
        ),
        testing_what='memories',
    )

"""
Conclusion:
    - For speed, partial seems to be twice as fast, inheriting from partial slowest & 
    the in house partial in the middle
    
    - For memory, there is a lot of variance with the version but in general, the
    in house performs surprisingly well
        
    Python27:
        Testing times mean of 5 rounds: 
        Name                            Secs     %    
        declare_inherits_from_partial   0.071    100  
        declare_in_house_partial        0.052    73   
        declare_partial                 0.0354   50   
        
        Testing memories mean of 5 rounds: 
        Name                            Mibs      %    
        declare_inherits_from_partial   37.9727   100  
        declare_in_house_partial        34.4766   91   
        declare_partial                 23.8906   63   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                            Secs     %    
        declare_inherits_from_partial   0.0516   100  
        declare_in_house_partial        0.0354   69   
        declare_partial                 0.0238   46   
        
        Testing memories mean of 5 rounds: 
        Name                            Mibs      %    
        declare_partial                 17.2109   100  
        declare_inherits_from_partial   16.9844   99   
        declare_in_house_partial        14.3008   83   

    Python310:
        Testing times mean of 5 rounds: 
        Name                            Secs     %    
        declare_inherits_from_partial   0.0533   100  
        declare_in_house_partial        0.0332   62   
        declare_partial                 0.025    47   
        
        Testing memories mean of 5 rounds: 
        Name                            Mibs      %    
        declare_partial                 10.0234   100  
        declare_inherits_from_partial   5.8008    57   
        declare_in_house_partial        2.8711    28   

    Python312:
        Testing times mean of 5 rounds: 
        Name                            Secs     %    
        declare_inherits_from_partial   0.0521   100  
        declare_in_house_partial        0.0358   69   
        declare_partial                 0.0284   55   
        
        Testing memories mean of 5 rounds: 
        Name                            Mibs     %    
        declare_inherits_from_partial   9.5742   100  
        declare_partial                 4.5352   47   
        declare_in_house_partial        3.707    39   

"""

