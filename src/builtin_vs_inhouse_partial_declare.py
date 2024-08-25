from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


def callable():
    return

def callable_with_args(*args):
    return

def callable_with_kwargs(**kwargs):
    return

def callable_with_args_and_kwargs(*args, **kwargs):
    return


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

class NamedCallable(object):
    __slots__ = ('__name__', 'handler')

    def __init__(self, name, handler):
        self.__name__ = name
        self.handler = handler

num = data.k100

def declare_no_name_partial_with_args():
    result = [
        partial(callable_with_args, 1,2,3,4,5,6)
        for _ in repeat(None, num)
    ]

def declare_no_name_partial_with_kwargs():
    result = [
        partial(callable_with_kwargs, a=1, b=2, c=3, d=4, e=5, f=6)
        for _ in repeat(None, num)
    ]

def declare_no_name_partial_with_args_and_kwargs():
    result = [
        partial(callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)
        for _ in repeat(None, num)
    ]

def declare_named_partial_with_args():
    result = [
        InheritFromPartial('someName', callable_with_args, 1,2,3,4,5,6)
        for _ in repeat(None, num)
    ]

def declare_named_partial_with_kwargs():
    result = [
        InheritFromPartial('someName', callable_with_kwargs, a=1,b=2,c=3,d=4,e=5,f=6)
        for _ in repeat(None, num)
    ]

def declare_named_partial_with_args_and_kwargs():
    result = [
        InheritFromPartial('someName', callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)
        for _ in repeat(None, num)
    ]

def declare_in_house_partial_with_args():
    result = [
        InHousePartial('SomeName', callable_with_args, 1,2,3,4,5,6)
        for _ in repeat(None, num)
    ]

def declare_in_house_partial_with_kwargs():
    result = [
        InHousePartial('SomeName', callable_with_kwargs, a=1,b=2,c=3,d=4,e=5,f=6)
        for _ in repeat(None, num)
    ]

def declare_in_house_partial_with_args_and_kwargs():
    result = [
        InHousePartial('someName', callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)
        for _ in repeat(None, num)
    ]


if __name__ == '__main__':
    tester(
        (
            declare_no_name_partial_with_args,
            declare_no_name_partial_with_kwargs,
            declare_no_name_partial_with_args_and_kwargs,
            declare_named_partial_with_args,
            declare_named_partial_with_kwargs,
            declare_named_partial_with_args_and_kwargs,
            declare_in_house_partial_with_args,
            declare_in_house_partial_with_kwargs,
            declare_in_house_partial_with_args_and_kwargs,
        )
    )

    tester(
        (
            declare_no_name_partial_with_args,
            declare_no_name_partial_with_kwargs,
            declare_no_name_partial_with_args_and_kwargs,
            declare_named_partial_with_args,
            declare_named_partial_with_kwargs,
            declare_named_partial_with_args_and_kwargs,
            declare_in_house_partial_with_args,
            declare_in_house_partial_with_kwargs,
            declare_in_house_partial_with_args_and_kwargs,
        ),
        testing_what='memories'
    )

"""
Conclusion:
    - When it comes to memory the main problem is dict, which is
    very expensive, i.e. kwargs. 
    
    - For speed of declaration inheriting from partial seems to
    cause a significant slowdown
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        declare_named_partial_with_args_and_kwargs      0.5108   100  
        declare_in_house_partial_with_args_and_kwargs   0.441    86   
        declare_named_partial_with_kwargs               0.4144   81   
        declare_in_house_partial_with_kwargs            0.4004   78   
        declare_no_name_partial_with_args_and_kwargs    0.3044   60   
        declare_no_name_partial_with_kwargs             0.3008   59   
        declare_named_partial_with_args                 0.2842   56   
        declare_in_house_partial_with_args              0.2136   42   
        declare_no_name_partial_with_args               0.1768   35   

        Testing memories mean of 5 rounds: 
        Name                                            Mibs      %    
        declare_in_house_partial_with_args_and_kwargs   87.0117   100  
        declare_named_partial_with_args_and_kwargs      76.707    88   
        declare_in_house_partial_with_kwargs            75.7695   87   
        declare_no_name_partial_with_args_and_kwargs    71.207    82   
        declare_named_partial_with_kwargs               67.6797   78   
        declare_in_house_partial_with_args              42.6602   49   
        declare_named_partial_with_args                 33.7813   39   
        declare_no_name_partial_with_kwargs             9.4961    11   
        declare_no_name_partial_with_args               3.8984    4    
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        declare_named_partial_with_args_and_kwargs      0.4687   100  
        declare_named_partial_with_kwargs               0.3539   76   
        declare_in_house_partial_with_args_and_kwargs   0.3258   70   
        declare_named_partial_with_args                 0.3085   66   
        declare_in_house_partial_with_kwargs            0.2753   59   
        declare_no_name_partial_with_args_and_kwargs    0.2001   43   
        declare_in_house_partial_with_args              0.176    38   
        declare_no_name_partial_with_kwargs             0.1598   34   
        declare_no_name_partial_with_args               0.1515   32   
        
        Testing memories mean of 5 rounds: 
        Name                                            Mibs      %    
        declare_named_partial_with_args_and_kwargs      40.625    100  
        declare_in_house_partial_with_args_and_kwargs   39.3047   97   
        declare_no_name_partial_with_kwargs             36.6875   90   
        declare_named_partial_with_kwargs               30.125    74   
        declare_in_house_partial_with_kwargs            29.3047   72   
        declare_no_name_partial_with_args_and_kwargs    28.0781   69   
        declare_in_house_partial_with_args              17.9375   44   
        declare_no_name_partial_with_args               16.0664   40   
        declare_named_partial_with_args                 10.4922   26   

    Python310:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        declare_named_partial_with_args_and_kwargs      0.3865   100  
        declare_named_partial_with_kwargs               0.3268   85   
        declare_in_house_partial_with_args_and_kwargs   0.3217   83   
        declare_in_house_partial_with_kwargs            0.2838   73   
        declare_named_partial_with_args                 0.2587   67   
        declare_no_name_partial_with_args_and_kwargs    0.2223   57   
        declare_in_house_partial_with_args              0.1746   45   
        declare_no_name_partial_with_kwargs             0.1713   44   
        declare_no_name_partial_with_args               0.125    32   
        
        Testing memories mean of 5 rounds: 
        Name                                            Mibs      %    
        declare_named_partial_with_args_and_kwargs      30.9062   100  
        declare_in_house_partial_with_args_and_kwargs   25.1211   81   
        declare_in_house_partial_with_kwargs            22.875    74   
        declare_no_name_partial_with_args_and_kwargs    22.6602   73   
        declare_named_partial_with_kwargs               21.4805   70   
        declare_no_name_partial_with_kwargs             18.8281   61   
        declare_no_name_partial_with_args               14.0      45   
        declare_named_partial_with_args                 11.7812   38   
        declare_in_house_partial_with_args              9.332     30   

    Python312:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        declare_named_partial_with_args_and_kwargs      0.4469   100  
        declare_in_house_partial_with_args_and_kwargs   0.3425   77   
        declare_named_partial_with_kwargs               0.316    71   
        declare_named_partial_with_args                 0.2624   59   
        declare_in_house_partial_with_kwargs            0.2534   56   
        declare_no_name_partial_with_args_and_kwargs    0.2196   49   
        declare_in_house_partial_with_args              0.1664   37   
        declare_no_name_partial_with_kwargs             0.154    34   
        declare_no_name_partial_with_args               0.1442   32   
        
        Testing memories mean of 5 rounds: 
        Name                                            Mibs      %    
        declare_no_name_partial_with_args_and_kwargs    32.2891   100  
        declare_in_house_partial_with_args_and_kwargs   31.1484   96   
        declare_named_partial_with_args_and_kwargs      30.2969   94   
        declare_no_name_partial_with_kwargs             24.1523   75   
        declare_named_partial_with_kwargs               21.1953   66   
        declare_named_partial_with_args                 13.3906   41   
        declare_in_house_partial_with_args              13.0664   40   
        declare_no_name_partial_with_args               12.5547   39   
        declare_in_house_partial_with_kwargs            12.3555   38   

"""

