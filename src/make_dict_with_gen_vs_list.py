from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

ints = data.ten_ints
num = data.M

class _DictList(dict):
    def __init__(self):
        seq = [(i, i) for i in ints]
        super(_DictList, self).__init__(seq)


class _DictGen(dict):
    def __init__(self):
        gen = ((i, i) for i in ints)
        super(_DictGen, self).__init__(gen)


def makeWithGen(DictGen=_DictGen):
    for _ in repeat(None, num):
        DictGen()

def makeWithList(DictList=_DictList):
    for _ in repeat(None, num):
        DictList()


auto_tester()


"""
Conclusion:
- Pretty specific test, should probably redo with 
different sizes and different ways of making a dict.

Python27:
    Name           Secs     %    
    makeWithList   0.9226   100  
    makeWithGen    0.9024   98  
    
Python38:
    Name           Secs     %    
    makeWithGen    0.6374   100  
    makeWithList   0.5578   88  
    
Python310:
    Name           Secs     %    
    makeWithGen    0.6989   100  
    makeWithList   0.6589   94   
    
Python312:
    Name           Secs     %    
    makeWithGen    0.6405   100  
    makeWithList   0.5236   82   

"""
