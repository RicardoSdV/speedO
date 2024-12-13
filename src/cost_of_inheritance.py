from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Level0:
    def meth(self): pass

class Level1(Level0): pass

class Level2(Level1): pass

class Level3(Level2): pass

class Level4(Level3): pass

class Level5(Level4): pass

class Level6(Level5): pass


num = data.M10

def inst_level0():
    for _ in repeat(None, num):
        obj = Level0()

def inst_level1():
    for _ in repeat(None, num):
        obj = Level1()

def inst_level2():
    for _ in repeat(None, num):
        obj = Level2()

def inst_level3():
    for _ in repeat(None, num):
        obj = Level3()

def inst_level4():
    for _ in repeat(None, num):
        obj = Level4()

def inst_level5():
    for _ in repeat(None, num):
        obj = Level5()

def inst_level6():
    for _ in repeat(None, num):
        obj = Level6()


if __name__ == '__main__':
    tester(
        (
            inst_level0,
            inst_level1,
            inst_level2,
            inst_level3,
            inst_level4,
            inst_level5,
            inst_level6,
        )
    )

def call_level0():
    obj = Level0()
    for _ in repeat(None, num):
        obj.meth()

def call_level1():
    obj = Level1()
    for _ in repeat(None, num):
        obj.meth()

def call_level2():
    obj = Level2()
    for _ in repeat(None, num):
        obj.meth()

def call_level3():
    obj = Level3()
    for _ in repeat(None, num):
        obj.meth()

def call_level4():
    obj = Level4()
    for _ in repeat(None, num):
        obj.meth()

def call_level5():
    obj = Level5()
    for _ in repeat(None, num):
        obj.meth()

def call_level6():
    obj = Level6()
    for _ in repeat(None, num):
        obj.meth()


if __name__ == '__main__':
    tester(
        (
            call_level0,
            call_level1,
            call_level2,
            call_level3,
            call_level4,
            call_level5,
            call_level6,
        )
    )

"""
Conclusion:
    In python3 the differences seem to be irrelevant, however, in python2
    a deep enough inheritance hierarchy might noticeably slow down things, 
    specially if calling lots of methods "far away" in the mro.
    
    Somehow Python310 got slower yet, python312 got way faster for calling
    but somewhat slower for instantiating

    Python27:
    
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        inst_level2   0.7218   100  
        inst_level1   0.6114   85   
        inst_level0   0.5056   70   
        
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        call_level2   0.5444   100  
        call_level1   0.485    89   
        call_level0   0.4246   78   
        
    Python38:
    
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        inst_level1   0.2816   100  
        inst_level2   0.2707   96   
        inst_level0   0.2565   91   
        
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        call_level0   0.2477   100  
        call_level2   0.2476   100  
        call_level1   0.2471   100  
    
    Python310:
    
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        inst_level2   0.3071   100  
        inst_level0   0.3015   98   
        inst_level1   0.2954   96   
        
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        call_level2   0.3219   100  
        call_level0   0.3158   98   
        call_level1   0.3083   96   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        inst_level2   0.3458   100  
        inst_level1   0.3363   97   
        inst_level0   0.3361   97   
        
        Testing times mean of 5 rounds: 
        Name          Secs     %    
        call_level2   0.172    100  
        call_level0   0.1688   98   
        call_level1   0.1614   94   
    

"""

