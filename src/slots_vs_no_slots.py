from itertools import repeat

from src.z_data import data
from src.z_tester import autoTester


class _Slots(object):
    __slots__ = ('a1', )
    def __init__(self):
        self.a1 = 1
    @property
    def prop(self): return
    def meth(self): return
    @classmethod
    def clsMeth(cls): return
    @staticmethod
    def statMeth(): return


class _NoSlots(object):
    def __init__(self):
        self.a1 = 1
    @property
    def prop(self): return
    def meth(self): return
    @classmethod
    def clsMeth(cls): return
    @staticmethod
    def statMeth(): return

slots = _Slots()
no_slots = _NoSlots()

num = data.M10

def call_slots_attr():
    _slots = slots
    for _ in repeat(None, num):
        _slots.a1

def call_no_slots_attr():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.a1

def call_slots_prop():
    _slots = slots
    for _ in repeat(None, num):
        _slots.prop

def call_no_slots_prop():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.prop

def call_slots_meth():
    _slots = slots
    for _ in repeat(None, num):
        _slots.meth()

def call_no_slots_meth():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.meth()

def call_slots_clsMeth():
    _slots = slots
    for _ in repeat(None, num):
        _slots.clsMeth()

def call_no_slots_clsMeth():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.clsMeth()

def call_slots_statMeth():
    _slots = slots
    for _ in repeat(None, num):
        _slots.statMeth()

def call_no_slots_statMeth():
    _no_slots = no_slots
    for _ in repeat(None, num):
        _no_slots.statMeth()


autoTester(print_rounds=False, segregator='end')

"""
Conclusion:
    - Slots always faster, from a bit to 20%
    
    Python27:
        Name                 Secs     %    
        call_no_slots_attr   0.1668   100  
        call_slots_attr      0.1612   97   
        
        Name                    Secs     %    
        call_no_slots_clsMeth   0.4402   100  
        call_slots_clsMeth      0.3614   82   
        
        Name                 Secs     %    
        call_no_slots_meth   0.4308   100  
        call_slots_meth      0.3552   82   
        
        Name                 Secs     %    
        call_slots_prop      0.604    100  
        call_no_slots_prop   0.6026   100  
        
        Name                     Secs     %    
        call_no_slots_statMeth   0.399    100  
        call_slots_statMeth      0.3248   81   

    Python38:
        Name                 Secs     %    
        call_no_slots_attr   0.1045   100  
        call_slots_attr      0.0995   95   
        
        Name                    Secs     %    
        call_no_slots_clsMeth   0.3227   100  
        call_slots_clsMeth      0.2947   91   
        
        Name                 Secs     %    
        call_no_slots_meth   0.2626   100  
        call_slots_meth      0.2453   93   
        
        Name                 Secs     %    
        call_slots_prop      0.2523   100  
        call_no_slots_prop   0.2515   100  
        
        Name                     Secs     %    
        call_no_slots_statMeth   0.2575   100  
        call_slots_statMeth      0.2468   96   

        
    Python310:
        Name                 Secs     %    
        call_no_slots_attr   0.1301   100  
        call_slots_attr      0.1235   95   
        
        Name                    Secs     %    
        call_no_slots_clsMeth   0.4032   100  
        call_slots_clsMeth      0.3869   96   
        
        Name                 Secs     %    
        call_no_slots_meth   0.3007   100  
        call_slots_meth      0.2907   97   
        
        Name                 Secs     %    
        call_slots_prop      0.289    100  
        call_no_slots_prop   0.2885   100  
        
        Name                     Secs     %    
        call_no_slots_statMeth   0.2957   100  
        call_slots_statMeth      0.2783   94   

    Python312:
        Name                 Secs     %    
        call_slots_attr      0.0691   100  
        call_no_slots_attr   0.0685   99   
        
        Name                    Secs     %    
        call_no_slots_clsMeth   0.3456   100  
        call_slots_clsMeth      0.3331   96   
        
        Name                 Secs     %    
        call_no_slots_meth   0.1608   100  
        call_slots_meth      0.1592   99   
        
        Name                 Secs     %    
        call_no_slots_prop   0.1459   100  
        call_slots_prop      0.1458   100  
        
        Name                     Secs    %    
        call_no_slots_statMeth   0.213   100  
        call_slots_statMeth      0.2     94   

"""
