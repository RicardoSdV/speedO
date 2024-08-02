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
            name = self.attr
            for _ in repeat(None, 1):
                _name = name

    def no_declare_local_1_use(self):
        for _ in repeat(None, num):
            for _ in repeat(None, 1):
                _name = self.attr


    def declare_local_2_use(self):
        for _ in repeat(None, num):
            name = self.attr
            for _ in repeat(None, 2):
                _name = name

    def no_declare_local_2_use(self):
        for _ in repeat(None, num):
            for _ in repeat(None, 2):
                _name = self.attr


    def declare_local_4_use(self):
        for _ in repeat(None, num):
            name = self.attr
            for _ in repeat(None, 4):
                _name = name

    def no_declare_local_4_use(self):
        for _ in repeat(None, num):
            for _ in repeat(None, 4):
                _name = self.attr


    def declare_local_8_use(self):
        for _ in repeat(None, num):
            name = self.attr
            for _ in repeat(None, 8):
                _name = name

    def no_declare_local_8_use(self):
        for _ in repeat(None, num):
            for _ in repeat(None, 8):
                _name = self.attr


    def declare_local_16_use(self):
        for _ in repeat(None, num):
            name = self.attr
            for _ in repeat(None, 16):
                _name = name

    def no_declare_local_16_use(self):
        for _ in repeat(None, num):
            for _ in repeat(None, 16):
                _name = self.attr

obj = Class()

tester(
    (
        obj.declare_local_1_use,
        obj.no_declare_local_1_use,
        obj.declare_local_2_use,
        obj.no_declare_local_2_use,
        obj.declare_local_4_use,
        obj.no_declare_local_4_use,
        obj.declare_local_8_use,
        obj.no_declare_local_8_use,
        obj.declare_local_16_use,
        obj.no_declare_local_16_use,
    )
)

"""
Conclusion:
    - Normally becomes worth it at 2 usages except in Python312, there at 4
    
    - To be fair memory & deletion speeds are not being measured, im sure there are
    some hidden costs to declaring locals all over the place   
    
    Python27:
        - Becomes worth it at 2 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.3508   100  
        no_declare_local_8_use    0.2172   62   
        declare_local_16_use      0.2114   60   
        declare_local_8_use       0.1528   44   
        no_declare_local_4_use    0.1448   41   
        declare_local_4_use       0.1192   34   
        no_declare_local_2_use    0.111    32   
        declare_local_2_use       0.105    30   
        declare_local_1_use       0.0964   27   
        no_declare_local_1_use    0.0948   27   
    
    Python38:
        - Becomes worth it at 2 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.2424   100  
        declare_local_16_use      0.1636   67   
        no_declare_local_8_use    0.144    59   
        declare_local_8_use       0.1133   47   
        no_declare_local_4_use    0.0991   41   
        declare_local_4_use       0.0861   36   
        no_declare_local_2_use    0.0764   32   
        declare_local_2_use       0.0733   30   
        declare_local_1_use       0.0671   28   
        no_declare_local_1_use    0.0639   26   
    
    Python310:
        - Becomes worth it at 2 usages
        
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.2856   100  
        declare_local_16_use      0.1882   66   
        no_declare_local_8_use    0.1688   59   
        declare_local_8_use       0.1295   45   
        no_declare_local_4_use    0.1099   38   
        declare_local_4_use       0.0967   34   
        no_declare_local_2_use    0.0847   30   
        declare_local_2_use       0.0812   28   
        declare_local_1_use       0.0728   25   
        no_declare_local_1_use    0.0671   23   
    
    Python312:
        - Becomes worth it at 4 usages
    
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        no_declare_local_16_use   0.1849   100  
        declare_local_16_use      0.162    88   
        no_declare_local_8_use    0.1192   64   
        declare_local_8_use       0.1095   59   
        no_declare_local_4_use    0.0859   46   
        declare_local_4_use       0.0835   45   
        declare_local_2_use       0.0729   39   
        no_declare_local_2_use    0.0711   38   
        declare_local_1_use       0.0654   35   
        no_declare_local_1_use    0.0624   34   
"""

