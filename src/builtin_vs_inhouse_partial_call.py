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


no_name_partial_with_args = partial(callable_with_args, 1,2,3,4,5,6)
no_name_partial_with_kwargs = partial(callable_with_kwargs, a=1,b=2,c=3,d=4,e=5,f=6)
no_name_partial_with_args_and_kwargs = partial(callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)

named_partial_with_args = InheritFromPartial('someName', callable_with_args, 1,2,3,4,5,6)
named_partial_with_kwargs = InheritFromPartial('someName', callable_with_kwargs, a=1,b=2,c=3,d=4,e=5,f=6)
named_partial_with_args_and_kwargs = InheritFromPartial('someName', callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)

in_house_partial_with_args = InHousePartial('SomeName', callable_with_args, 1,2,3,4,5,6)
in_house_partial_with_kwargs = InHousePartial('SomeName', callable_with_kwargs, a=1,b=2,c=3,d=4,e=5,f=6)
in_house_partial_with_args_and_kwargs = InHousePartial('someName', callable_with_args_and_kwargs, 1,2,3,4,5,6, a=1,b=2,c=3,d=4,e=5,f=6)

num = data.M

def call_no_name_partial_with_args():
    for _ in repeat(None, num):
        no_name_partial_with_args()

def call_no_name_partial_with_kwargs():
    for _ in repeat(None, num):
        no_name_partial_with_kwargs()

def call_no_name_partial_with_args_and_kwargs():
    for _ in repeat(None, num):
        no_name_partial_with_args_and_kwargs()

def call_named_partial_with_args():
    for _ in repeat(None, num):
        named_partial_with_args()

def call_named_partial_with_kwargs():
    for _ in repeat(None, num):
        named_partial_with_kwargs()

def call_named_partial_with_args_and_kwargs():
    for _ in repeat(None, num):
        named_partial_with_args_and_kwargs()

def call_in_house_partial_with_args():
    for _ in repeat(None, num):
        in_house_partial_with_args()

def call_in_house_partial_with_kwargs():
    for _ in repeat(None, num):
        in_house_partial_with_kwargs()

def call_in_house_partial_with_args_and_kwargs():
    for _ in repeat(None, num):
        in_house_partial_with_args_and_kwargs()


tester(
    (
        call_no_name_partial_with_args,
        call_no_name_partial_with_kwargs,
        call_no_name_partial_with_args_and_kwargs,
        call_named_partial_with_args,
        call_named_partial_with_kwargs,
        call_named_partial_with_args_and_kwargs,
        call_in_house_partial_with_args,
        call_in_house_partial_with_kwargs,
        call_in_house_partial_with_args_and_kwargs,
    )
)

"""
Conclusion:
    This test was specially inprecise, bc the hardware and multiple processes
    going on at the same time but there are two main slow down factors,
    using an in-house partial and kwargs. And the difference is not small

    Python27:
        Name                                         Secs     %    
        call_in_house_partial_with_args_and_kwargs   1.4444   100  
        call_no_name_partial_with_args_and_kwargs    1.401    97   
        call_in_house_partial_with_kwargs            1.291    89   
        call_no_name_partial_with_kwargs             1.2396   86   
        call_named_partial_with_kwargs               1.2166   84   
        call_named_partial_with_args_and_kwargs      1.169    81   
        call_in_house_partial_with_args              0.7814   54   
        call_no_name_partial_with_args               0.2636   18   
        call_named_partial_with_args                 0.238    16   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                                         Secs     %    
        call_in_house_partial_with_args_and_kwargs   0.7917   100  
        call_in_house_partial_with_kwargs            0.7707   97   
        call_no_name_partial_with_args_and_kwargs    0.7592   96   
        call_named_partial_with_args_and_kwargs      0.6652   84   
        call_named_partial_with_kwargs               0.6363   80   
        call_in_house_partial_with_args              0.4429   56   
        call_no_name_partial_with_args               0.1875   24   
        call_named_partial_with_args                 0.1754   22   
        call_no_name_partial_with_kwargs             0.0788   10   

    Python310:
        Testing times mean of 5 rounds: 
        Name                                         Secs     %    
        call_in_house_partial_with_args_and_kwargs   2.529    100  
        call_in_house_partial_with_kwargs            1.4013   55   
        call_no_name_partial_with_args_and_kwargs    1.1255   45   
        call_no_name_partial_with_kwargs             0.9677   38   
        call_named_partial_with_args_and_kwargs      0.8427   33   
        call_named_partial_with_kwargs               0.8034   32   
        call_in_house_partial_with_args              0.5965   24   
        call_no_name_partial_with_args               0.4121   16   
        call_named_partial_with_args                 0.2362   9    
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                                         Secs     %    
        call_in_house_partial_with_args_and_kwargs   0.755    100  
        call_in_house_partial_with_kwargs            0.7277   96   
        call_no_name_partial_with_args_and_kwargs    0.6452   85   
        call_named_partial_with_args_and_kwargs      0.5868   78   
        call_named_partial_with_kwargs               0.5776   77   
        call_no_name_partial_with_kwargs             0.543    72   
        call_in_house_partial_with_args              0.3508   46   
        call_named_partial_with_args                 0.1466   19   
        call_no_name_partial_with_args               0.1303   17   

"""

