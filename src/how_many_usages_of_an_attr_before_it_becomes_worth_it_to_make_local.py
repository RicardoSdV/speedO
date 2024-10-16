from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M

class Class(object):
    __slots__ = ('attr',)

    def __init__(self):
        self.attr = 1

    def declare_local_1_use(self):
        for _ in repeat(None, num):
            _attr = self.attr
            name = _attr

    def no_declare_local_1_use(self):
        for _ in repeat(None, num):
            name = self.attr

    def declare_local_2_use(self):
        for _ in repeat(None, num):
            _attr = self.attr
            name1 = _attr
            name2 = _attr

    def no_declare_local_2_use(self):
        for _ in repeat(None, num):
            name1 = self.attr
            name2 = self.attr

    def declare_local_4_use(self):
        for _ in repeat(None, num):
            _attr = self.attr
            name1 = _attr
            name2 = _attr
            name3 = _attr
            name4 = _attr

    def no_declare_local_4_use(self):
        for _ in repeat(None, num):
            name1 = self.attr
            name2 = self.attr
            name3 = self.attr
            name4 = self.attr

    def declare_local_8_use(self):
        for _ in repeat(None, num):
            _attr = self.attr
            name1 = _attr
            name2 = _attr
            name3 = _attr
            name4 = _attr
            name5 = _attr
            name6 = _attr
            name7 = _attr
            name8 = _attr

    def no_declare_local_8_use(self):
        for _ in repeat(None, num):
            name1 = self.attr
            name2 = self.attr
            name3 = self.attr
            name4 = self.attr
            name5 = self.attr
            name6 = self.attr
            name7 = self.attr
            name8 = self.attr

    def declare_local_16_use(self):
        for _ in repeat(None, num):
            _attr = self.attr
            name1 = _attr
            name2 = _attr
            name3 = _attr
            name4 = _attr
            name5 = _attr
            name6 = _attr
            name7 = _attr
            name8 = _attr
            name9 = _attr
            name10 = _attr
            name11 = _attr
            name12 = _attr
            name13 = _attr
            name14 = _attr
            name15 = _attr
            name16 = _attr

    def no_declare_local_16_use(self):
        for _ in repeat(None, num):
            name1 = self.attr
            name2 = self.attr
            name3 = self.attr
            name4 = self.attr
            name5 = self.attr
            name6 = self.attr
            name7 = self.attr
            name8 = self.attr
            name9 = self.attr
            name10 = self.attr
            name11 = self.attr
            name12 = self.attr
            name13 = self.attr
            name14 = self.attr
            name15 = self.attr
            name16 = self.attr

obj = Class()

tester(
    (
        obj.declare_local_1_use,
        obj.no_declare_local_1_use,
    ),
    print_rounds = False,
)
tester(
    (
        obj.declare_local_2_use,
        obj.no_declare_local_2_use,
    ),
    print_rounds = False,
)
tester(
    (
        obj.declare_local_4_use,
        obj.no_declare_local_4_use,
    ),
    print_rounds = False,
)
tester(
    (
        obj.declare_local_8_use,
        obj.no_declare_local_8_use,
    ),
    print_rounds=False,
)
tester(
    (
        obj.declare_local_16_use,
        obj.no_declare_local_16_use,
    ),
    print_rounds=False,
)

"""
Conclusion:
    - Normally becomes worth it at 2 usages except in Python312, there at 4
    
    - To be fair memory & deletion speeds are not being measured, im sure there are
    some hidden costs to declaring locals all over the place
    
    - Somehow theres is a diminishing improvement the more usages in later versions
    
    Python27:
        - Becomes faster at 2 usages
    Name                     Secs     %   
    declare_local_1_use      0.018    100  
    no_declare_local_1_use   0.0156   87   
    
    no_declare_local_2_use   0.0266   100  
    declare_local_2_use      0.0204   77   
    
    no_declare_local_4_use   0.0492   100  
    declare_local_4_use      0.0258   52   
    
    no_declare_local_8_use   0.108    100  
    declare_local_8_use      0.0428   40   
    
    no_declare_local_16_use   0.1942   100  
    declare_local_16_use      0.0618   32   
    
    Python38:
        - Becomes faster at 2 usages
    Name                     Secs     %    
    declare_local_1_use      0.0132   100  
    no_declare_local_1_use   0.0104   79   
    
    no_declare_local_2_use   0.0179   100  
    declare_local_2_use      0.0161   90   
    
    no_declare_local_4_use   0.0319   100  
    declare_local_4_use      0.0204   64   
    
    no_declare_local_8_use   0.0614   100  
    declare_local_8_use      0.0304   50   

    no_declare_local_16_use   0.1213   100  
    declare_local_16_use      0.0566   47   
    
    Python310:
        - Becomes worth it at 2 usages
    Name                     Secs     %    
    declare_local_1_use      0.015    100  
    no_declare_local_1_use   0.0124   83   
    
    no_declare_local_2_use   0.0212   100  
    declare_local_2_use      0.0177   84   
    
    no_declare_local_4_use   0.0393   100  
    declare_local_4_use      0.0223   56   
    
    no_declare_local_8_use   0.0757   100  
    declare_local_8_use      0.0404   53   
    
    no_declare_local_16_use   0.1578   100  
    declare_local_16_use      0.0606   38   
    
    Python312:
        - Becomes worth it at 4 usages
    Name                     Secs     %    
    declare_local_1_use      0.0096   100  
    no_declare_local_1_use   0.0074   77   
    
    declare_local_2_use      0.0113   100  
    no_declare_local_2_use   0.0111   99   
    
    no_declare_local_4_use   0.0186   100  
    declare_local_4_use      0.014    75   
    
    no_declare_local_8_use   0.0363   100  
    declare_local_8_use      0.0209   57   
    
    no_declare_local_16_use   0.0806   100  
    declare_local_16_use      0.0371   46   

"""

